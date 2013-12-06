#coding:utf8
'''
Created on 2013-8-14

@author: lan (www.9miao.com)
'''
from twisted.python import log

from zope.interface import Interface
from zope.interface import implements

class _ChildsManager(Interface):
    '''节点管理器接口'''
    
    def __init__(self):
        '''初始化接口'''
        
    def getChildById(self,childId):
        '''根据节点id获取节点实例'''
        
    def getChildByName(self,childname):
        '''根据节点的名称获取节点实例'''
        
    def addChild(self,child):
        '''添加一个child节点
        @param child: Child object
        '''
    
    def dropChild(self,*arg,**kw):
        '''删除一个节点'''
        
    def callChild(self,*args,**kw):
        '''调用子节点的接口'''
        
    def callChildByName(self,*args,**kw):
        '''调用子节点的接口
        @param childname: str 子节点的名称
        '''
    
    def dropChildByID(self,childId):
        '''删除一个child 节点
        @param childId: Child ID 
        '''
        
    def dropChildSessionId(self, session_id):
        """根据session_id删除child节点
        """

class ChildsManager(object):
    '''子节点管理器'''
    
    implements(_ChildsManager)
    
    def __init__(self):
        '''初始化子节点管理器'''
        self._childs = {}
        
    def getChildById(self,childId):
        '''根据节点的ID获取节点实例'''
        return self._childs.get(childId)
    
    def getChildByName(self,childname):
        '''根据节点的名称获取节点实例'''
        for key,child in self._childs.items():
            if child.getName() == childname:
                return self._childs[key]
        return None
        
    def addChild(self,child):
        '''添加一个child节点
        @param child: Child object
        '''
        key = child._id
        if self._childs.has_key(key):
            raise "child node %s exists"% key
        self._childs[key] = child
        
    def dropChild(self,child):
        '''删除一个child 节点
        @param child: Child Object 
        '''
        key = child._id
        try:
            del self._childs[key]
        except Exception,e:
            log.msg(str(e))
            
    def dropChildByID(self,childId):
        '''删除一个child 节点
        @param childId: Child ID 
        '''
        try:
            del self._childs[childId]
        except Exception,e:
            log.msg(str(e))
            
    def callChild(self,childId,*args,**kw):
        '''调用子节点的接口
        @param childId: int 子节点的id
        '''
        child = self._childs.get(childId,None)
        if not child:
            log.err("child %s doesn't exists"%childId)
            return
        return child.callbackChild(*args,**kw)
    
    def callChildByName(self,childname,*args,**kw):
        '''调用子节点的接口
        @param childname: str 子节点的名称
        '''
        child = self.getChildByName(childname)
        if not child:
            log.err("child %s doesn't exists"%childname)
            return
        return child.callbackChild(*args,**kw)
    
    def getChildBYSessionId(self, session_id):
        """根据sessionID获取child节点信息
        """
        for child in self._childs.values():
            if child._transport.broker.transport.sessionno == session_id:
                return child
        return child

        