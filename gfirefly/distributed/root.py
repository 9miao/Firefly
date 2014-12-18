#coding:utf8
'''
Created on 2013-8-14
分布式根节点
@author: lan (www.9miao.com)
'''
from gtwisted.utils import log
from gtwisted.core import rpc
from manager import ChildsManager
from child import Child

class BilateralBroker(rpc.PBServerProtocl):
    
    def connectionLost(self, reason):
        clientID = self.transport.sessionno
        log.msg("node [%d] lose"%clientID)
        self.factory.root.dropChildSessionId(clientID)
    
    def remote_takeProxy(self,name):
        '''设置代理通道
        @param name: 根节点的名称
        '''
        self.factory.root.remote_takeProxy(name,self)
        
    def remote_callTarget(self,command,*args,**kw):
        '''远程调用方法
        @param commandId: int 指令号
        @param data: str 调用参数
        '''
        data = self.factory.root.remote_callTarget(command,*args,**kw)
        return data
        
    
class BilateralFactory(rpc.PBServerFactory):
    
    protocol = BilateralBroker
    
    def __init__(self,root):
        rpc.PBServerFactory.__init__(self)
        self.root = root

class PBRoot:
    '''PB 协议
    '''
    
    def __init__(self,dnsmanager = ChildsManager()):
        '''初始化根节点
        '''
        self.service = None
        self.childsmanager = dnsmanager
    
    def addServiceChannel(self,service):
        '''添加服务通道
        @param service: Service Object(In bilateral.services)
        '''
        self.service = service
    
    def remote_takeProxy(self,name,transport):
        '''设置代理通道
        @param name: 根节点的名称
        '''
        log.msg('node [%s] takeProxy ready'%name)
        child = Child(name)
        self.childsmanager.addChild(child)
        child.setTransport(transport)
        self.doChildConnect(name, transport)
        
    def doChildConnect(self,name,transport):
        """当node节点连接时的处理
        """
        pass
        
    def remote_callTarget(self,command,*args,**kw):
        '''远程调用方法
        @param commandId: int 指令号
        @param data: str 调用参数
        '''
        data = self.service.callTarget(command,*args,**kw)
        return data
    
    def dropChild(self,*args,**kw):
        '''删除子节点记录'''
        self.childsmanager.dropChild(*args,**kw)
        
    def dropChildByID(self,childId):
        '''删除子节点记录
        '''
        self.doChildLostConnect(childId)
        self.childsmanager.dropChildByID(childId)
        
    def dropChildSessionId(self, session_id):
        '''删除子节点记录'''
        child = self.childsmanager.getChildBYSessionId(session_id)
        if not child:
            return
        childname = child.getName()
        self.doChildLostConnect(childname)
        self.childsmanager.dropChildByID(childname)
        
    def doChildLostConnect(self,childname):
        """当node节点连接时的处理
        """
        pass
    
    def callChild(self,key,*args,**kw):
        '''调用子节点的接口
        @param childId: int 子节点的id
        return Defered Object
        '''
        return self.childsmanager.callChild(key,*args,**kw)
    
    def callChildNotForResult(self,childname,*args,**kw):
        '''调用子节点的接口
        @param childId: int 子节点的id
        return Defered Object
        '''
        self.childsmanager.callChildNotForResult(childname,*args,**kw)
