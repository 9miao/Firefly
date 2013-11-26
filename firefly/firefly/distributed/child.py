#coding:utf8
'''
Created on 2013-8-14

@author: lan (www.9miao.com)
'''
class Child(object):
    '''子节点对象'''
    
    def __init__(self,cid,name):
        '''初始化子节点对象
        '''
        self._id = cid
        self._name = name
        self._transport = None
        
    def getName(self):
        '''获取子节点的名称'''
        return self._name
        
    def setTransport(self,transport):
        '''设置子节点的通道'''
        self._transport = transport
        
    def callbackChild(self,*args,**kw):
        '''回调子节点的接口
        return a Defered Object (recvdata)
        '''
        recvdata = self._transport.callRemote('callChild',*args,**kw)
        return recvdata
        
        
        
        
        