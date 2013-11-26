#coding:utf8
'''
Created on 2013-8-14

@author: lan (www.9miao.com)
'''
from twisted.spread import pb
from twisted.internet import reactor
reactor = reactor
from reference import ProxyReference

def callRemote(obj,funcName,*args,**kw):
    '''远程调用
    @param funcName: str 远程方法
    '''
    return obj.callRemote(funcName, *args,**kw)
    
    
class RemoteObject(object):
    '''远程调用对象'''
    
    def __init__(self,name):
        '''初始化远程调用对象
        @param port: int 远程分布服的端口号
        @param rootaddr: 根节点服务器地址
        '''
        self._name = name
        self._factory = pb.PBClientFactory()
        self._reference = ProxyReference()
        self._addr = None
        
    def setName(self,name):
        '''设置节点的名称'''
        self._name = name
        
    def getName(self):
        '''获取节点的名称'''
        return self._name
        
    def connect(self,addr):
        '''初始化远程调用对象'''
        self._addr = addr
        reactor.connectTCP(addr[0], addr[1], self._factory)
        self.takeProxy()
        
    def reconnect(self):
        '''重新连接'''
        self.connect(self._addr)
        
    def addServiceChannel(self,service):
        '''设置引用对象'''
        self._reference.addService(service)
        
    def takeProxy(self):
        '''像远程服务端发送代理通道对象
        '''
        deferedRemote = self._factory.getRootObject()
        deferedRemote.addCallback(callRemote,'takeProxy',self._name,self._reference)
    
    def callRemote(self,commandId,*args,**kw):
        '''远程调用'''
        deferedRemote = self._factory.getRootObject()
        return deferedRemote.addCallback(callRemote,'callTarget',commandId,*args,**kw)
    
    
    
    