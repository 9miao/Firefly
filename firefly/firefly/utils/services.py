#coding:utf8
'''
Created on 2011-1-3
服务类
@author: sean_lan
'''
import threading
from twisted.internet import defer,threads
from twisted.python import log


class Service(object):
    """A remoting service 
    
    attributes:
    ============
     * name - string, service name.
     * runstyle 
    """
    SINGLE_STYLE = 1
    PARALLEL_STYLE = 2

    def __init__(self, name,runstyle = SINGLE_STYLE):
        self._name = name
        self._runstyle = runstyle
        self.unDisplay = set()
        self._lock = threading.RLock()
        self._targets = {} # Keeps track of targets internally

    def __iter__(self):
        return self._targets.itervalues()
    
    def addUnDisplayTarget(self,command):
        '''Add a target unDisplay when client call it.'''
        self.unDisplay.add(command)

    def mapTarget(self, target):
        """Add a target to the service."""
        self._lock.acquire()
        try:
            key = target.__name__
            if self._targets.has_key(key):
                exist_target = self._targets.get(key)
                raise "target [%d] Already exists,\
                Conflict between the %s and %s"%(key,exist_target.__name__,target.__name__)
            self._targets[key] = target
        finally:
            self._lock.release()

    def unMapTarget(self, target):
        """Remove a target from the service."""
        self._lock.acquire()
        try:
            key = target.__name__
            if key in self._targets:
                del self._targets[key]
        finally:
            self._lock.release()
            
    def unMapTargetByKey(self,targetKey):
        """Remove a target from the service."""
        self._lock.acquire()
        try:
            del self._targets[targetKey]
        finally:
            self._lock.release()
            
    def getTarget(self, targetKey):
        """Get a target from the service by name."""
        self._lock.acquire()
        try:
            target = self._targets.get(targetKey, None)
        finally:
            self._lock.release()
        return target
    
    def callTarget(self,targetKey,*args,**kw):
        '''call Target
        @param conn: client connection
        @param targetKey: target ID
        @param data: client data
        '''
        if self._runstyle == self.SINGLE_STYLE:
            result = self.callTargetSingle(targetKey,*args,**kw)
        else:
            result = self.callTargetParallel(targetKey,*args,**kw)
        return result
    
    def callTargetSingle(self,targetKey,*args,**kw):
        '''call Target by Single
        @param conn: client connection
        @param targetKey: target ID
        @param data: client data
        '''
        target = self.getTarget(targetKey)
        
        self._lock.acquire()
        try:
            if not target:
                log.err('the command '+str(targetKey)+' not Found on service')
                return None
            if targetKey not in self.unDisplay:
                log.msg("call method %s on service[single]"%target.__name__)
            defer_data = target(*args,**kw)
            if not defer_data:
                return None
            if isinstance(defer_data,defer.Deferred):
                return defer_data
            d = defer.Deferred()
            d.callback(defer_data)
        finally:
            self._lock.release()
        return d
    
    def callTargetParallel(self,targetKey,*args,**kw):
        '''call Target by Single
        @param conn: client connection
        @param targetKey: target ID
        @param data: client data
        '''
        self._lock.acquire()
        try:
            target = self.getTarget(targetKey)
            if not target:
                log.err('the command '+str(targetKey)+' not Found on service')
                return None
            log.msg("call method %s on service[parallel]"%target.__name__)
            d = threads.deferToThread(target,*args,**kw)
        finally:
            self._lock.release()
        return d
    

class CommandService(Service):
    """A remoting service 
    According to Command ID search target
    """
    def mapTarget(self, target):
        """Add a target to the service."""
        self._lock.acquire()
        try:
            key = int((target.__name__).split('_')[-1])
            if self._targets.has_key(key):
                exist_target = self._targets.get(key)
                raise "target [%d] Already exists,\
                Conflict between the %s and %s"%(key,exist_target.__name__,target.__name__)
            self._targets[key] = target
        finally:
            self._lock.release()
            
    def unMapTarget(self, target):
        """Remove a target from the service."""
        self._lock.acquire()
        try:
            key = int((target.__name__).split('_')[-1])
            if key in self._targets:
                del self._targets[key]
        finally:
            self._lock.release()
    

    
    
    
            