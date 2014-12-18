#coding:utf8
'''
Created on 2011-1-3
服务类
@author: sean_lan
'''
from gtwisted.utils import log


class Service(object):
    """A remoting service 
    
    attributes:
    ============
     * name - string, service name.
     * runstyle 
    """

    def __init__(self, name):
        self._name = name
        self.unDisplay = set()
        self._targets = {} # Keeps track of targets internally

    def __iter__(self):
        return self._targets.itervalues()
    
    def addUnDisplayTarget(self,command):
        '''Add a target unDisplay when client call it.'''
        self.unDisplay.add(command)

    def mapTarget(self, target):
        """Add a target to the service."""
        key = target.__name__
        if self._targets.has_key(key):
            exist_target = self._targets.get(key)
            raise "target [%d] Already exists,\
            Conflict between the %s and %s"%(key,exist_target.__name__,target.__name__)
        self._targets[key] = target

    def unMapTarget(self, target):
        """Remove a target from the service."""
        key = target.__name__
        if key in self._targets:
            del self._targets[key]
            
    def unMapTargetByKey(self,targetKey):
        """Remove a target from the service."""
        del self._targets[targetKey]
            
    def getTarget(self, targetKey):
        """Get a target from the service by name."""
        target = self._targets.get(targetKey, None)
        return target
    
    def callTarget(self,targetKey,*args,**kw):
        '''call Target
        @param conn: client connection
        @param targetKey: target ID
        @param data: client data
        '''
        target = self.getTarget(targetKey)
        if not target:
            log.err('the command '+str(targetKey)+' not Found on service')
            return None
        if targetKey not in self.unDisplay:
            log.msg("call method %s on service[single]"%target.__name__)
        response = target(*args,**kw)
        return response


class CommandService(Service):
    """A remoting service 
    According to Command ID search target
    """
    def mapTarget(self, target):
        """Add a target to the service.
        """
        key = int((target.__name__).split('_')[-1])
        if self._targets.has_key(key):
            exist_target = self._targets.get(key)
            raise "target [%d] Already exists,\
            Conflict between the %s and %s"%(key,exist_target.__name__,target.__name__)
        self._targets[key] = target
            
    def unMapTarget(self, target):
        """Remove a target from the service.
        """
        key = int((target.__name__).split('_')[-1])
        if key in self._targets:
            del self._targets[key]
    

    
    
    
            