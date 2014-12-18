#coding:utf8
'''
Created on 2013-8-2

@author: lan (www.9miao.com)
'''
from gfirefly.utils.singleton import Singleton

class GlobalObject:
    """单例，存放了服务中的netfactory，root节点，所有的remote节点的句柄。
    """
    
    __metaclass__ = Singleton
    
    def __init__(self):
        self.netfactory = None#net前端
        self.root = None#分布式root节点
        self.remote = {}#remote节点
        self.db = None
        self.stophandler = None
        self.webroot = None
        self.masterremote = None
        self.reloadmodule = None
        self.remote_connect = None
        self.json_config = {}
        self.remote_map = {}
        
    def config(self,netfactory=None,root = None,remote=None,db=None):
        """配置存放的对象实例
        """
        self.netfactory = netfactory
        self.root = root
        self.remote = remote
        self.db = db
        
def masterserviceHandle(target):
    """供master调用的接口描述符
    """
    GlobalObject().masterremote._reference._service.mapTarget(target)
        
def netserviceHandle(target):
    """供客户端连接调用的接口描述符
    """
    GlobalObject().netfactory.service.mapTarget(target)
        
def rootserviceHandle(target):
    """作为root节点，供remote节点调用的接口描述符
    """
    GlobalObject().root.service.mapTarget(target)
    
class webserviceHandle:
    """这是一个修饰符对象,修饰http接口的连接地址。
    """
    
    def __init__(self,url,**kw):
        """
        @param url: str http 访问的路径
        """
        self._url = url
        self.kw = kw
        
    def __call__(self,cls):
        """
        """
        if self._url:
            child_name = self._url
        else:
            child_name = cls.__name__
        return GlobalObject().webroot.route(child_name,**self.kw)(cls)
    

    
class remoteserviceHandle:
    """作为remote节点，供某个root节点调用的接口描述符
    """
    def __init__(self,remotename):
        """
        """
        self.remotename = remotename
        
    def __call__(self,target):
        """
        """
        GlobalObject().remote[self.remotename]._reference._service.mapTarget(target)
        
