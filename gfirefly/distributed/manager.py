#coding:utf8
'''
Created on 2013-8-14

@author: lan (www.9miao.com)
'''
from gtwisted.utils import log

class ChildsManager(object):
    '''子节点管理器'''
    
    def __init__(self):
        '''初始化子节点管理器'''
        self._childs = {}
    
    def getChild(self,childname):
        '''根据节点的名称获取节点实例'''
        for key,child in self._childs.items():
            if child.getName() == childname:
                return self._childs[key]
        return None
        
    def addChild(self,child):
        '''添加一个child节点\n
        @param child: Child object
        '''
        key = child.getName()
        if self._childs.has_key(key):
            raise "child node %s exists"% key
        self._childs[key] = child
        
    def dropChild(self,child):
        '''删除一个child 节点\n
        @param child: Child Object 
        '''
        key = child.getName()
        try:
            del self._childs[key]
        except Exception,e:
            log.msg(str(e))
            
    def dropChildByID(self,childId):
        '''删除一个child 节点\n
        @param childId: Child ID 
        '''
        try:
            del self._childs[childId]
        except Exception,e:
            log.msg(str(e))
            
    def callChild(self,childname,*args,**kw):
        '''调用子节点的接口\n
        @param childname: str 子节点的名称
        '''
        child = self.getChild(childname)
        if not child:
            log.err("child %s doesn't exists"%childname)
            return
        return child.callbackChild(*args,**kw)
    
    def callChildNotForResult(self,childname,*args,**kw):
        '''调用子节点的接口\n
        @param childname: str 子节点的名称
        '''
        child = self._childs.get(childname,None)
        if not child:
            log.err("child %s doesn't exists"%childname)
            return
        child.callbackChildNotForResult(*args,**kw)
    
    def getChildBYSessionId(self, session_id):
        """根据sessionID获取child节点信息
        """
        for child in self._childs.values():
            if child._transport.transport.sessionno == session_id:
                return child
        return None

        