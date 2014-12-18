#coding:utf8
'''
Created on 2013-8-14

@author: lan (www.9miao.com)
'''
from gfirefly.utils.services import Service


class ProxyReference:
    '''代理通道'''
    
    def __init__(self):
        '''初始化'''
        self._service = Service('proxy')
        
    def addService(self,service):
        '''添加一条服务通道'''
        self._service = service
    
    def remote_callChild(self, command,*arg,**kw):
        '''代理发送数据
        '''
        return self._service.callTarget(command,*arg,**kw)
    
    
    
        