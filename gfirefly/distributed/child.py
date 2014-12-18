#coding:utf8
'''
Created on 2013-8-14

@author: lan (www.9miao.com)
'''
class Child(object):
    '''子节点对象'''
    
    def __init__(self,name):
        '''初始化子节点对象
        '''
        self._name = name
        self._transport = None
        
    def getName(self):
        '''获取子节点的名称'''
        return self._name
        
    def setTransport(self,transport):
        '''设置子节点的通道'''
        self._transport = transport
        
    def callbackChild(self,*args,**kw):
        '''回调子节点的接口\n
        return a Defered Object (recvdata)
        '''
        return self.callbackChildForResult(*args,**kw)
    
    def callbackChildNotForResult(self,*args,**kw):
        '''回调子节点的接口\n
        return a Defered Object (recvdata)
        '''
        remote = self._transport.getRootObject()
        remote.callRemoteNotForResult('callChild',*args,**kw)
        
    def callbackChildForResult(self,*args,**kw):
        '''回调子节点的接口\n
        return a Defered Object (recvdata)
        '''
        remote = self._transport.getRootObject()
        recvdata = remote.callRemoteForResult('callChild',*args,**kw)
        return recvdata
        
        
        
        
        