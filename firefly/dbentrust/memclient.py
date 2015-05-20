#coding:utf8
'''
Created on 2013-7-10
memcached client
@author: lan (www.9miao.com)
'''
import memcache

class MemConnError(Exception): 
    """
    """
    def __str__(self):
        return "memcache connect error"

class MemClient:
    '''memcached
    '''
    
    def __init__(self,timeout = 0):
        '''
        '''
        self._hostname = ""
        self._urls = []
        self.connection = None
        
    def connect(self,urls,hostname):
        '''memcached connect
        '''
        self._hostname = hostname
        self._urls = urls
        self.connection = memcache.Client(self._urls,debug=0)
        if not self.connection.set("__testkey__",1):
            raise MemConnError()
        
    def produceKey(self,keyname):
        '''
        '''
        if isinstance(keyname, basestring):
            return ''.join([self._hostname,':',keyname])
        else:
            raise "type error"
        
    def get(self,key):
        '''
        '''
        key = self.produceKey(key)
        return self.connection.get(key)
    
    def get_multi(self,keys):
        '''
        '''
        keynamelist = [self.produceKey(keyname) for keyname in keys]
        olddict = self.connection.get_multi(keynamelist)
        newdict = dict(zip([keyname.split(':')[-1] for keyname in olddict.keys()],
                              olddict.values()))
        return newdict
        
    def set(self,keyname,value):
        '''
        '''
        key = self.produceKey(keyname)
        result = self.connection.set(key,value)
        if not result:#如果写入失败
            self.connect(self._urls,self._hostname)#重新连接
            return self.connection.set(key,value)
        return result
    
    def set_multi(self,mapping):
        '''
        '''
        newmapping = dict(zip([self.produceKey(keyname) for keyname in mapping.keys()],
                              mapping.values()))
        result = self.connection.set_multi(newmapping)
        if result:#如果写入失败
            self.connect(self._urls,self._hostname)#重新连接
            return self.connection.set_multi(newmapping)
        return result
        
    def incr(self,key,delta):
        '''
        '''
        key = self.produceKey(key)
        return self.connection.incr(key, delta)
        
    def delete(self,key):
        '''
        '''
        key = self.produceKey(key)
        return self.connection.delete(key)
    
    def delete_multi(self,keys):
        """
        """
        keys = [self.produceKey(key) for key in keys]
        return self.connection.delete_multi(keys)
        
    def flush_all(self):
        '''
        '''
        self.connection.flush_all()
        
mclient = MemClient()


