#coding:utf8
'''
Created on 2013-7-10
memcached client
@author: lan (www.9miao.com)
'''
import memcache

class MemConnError(Exception): 
    """memcached 连接错误
    """
    
    def __str__(self):
        return "memcache connect error"

class MemClient:
    '''memcached 连接类，对通过它存储到memcached中的key，定义了新的key的生成规则，避免key的冲突。\n
    @param _hostname: str 这个连接的命名空间。新生成的key的规则会是  _hostname:key。\n
    @param _urls: []list memcached的连接的配置\n
    @param connection: memcached的连接实例。\n
    >>> mclient = MemClient()
    '''
    
    def __init__(self,timeout = 0):
        '''
        '''
        self._hostname = ""
        self._urls = []
        self.connection = None
        
    def connect(self,urls,hostname):
        '''memcached 建立连接，配置连接信息

        >>> mclient.connect(['127.0.0.1:11211'], "test")
        '''
        self._hostname = hostname
        self._urls = urls
        self.connection = memcache.Client(self._urls,debug=0)
        if not self.connection.set("__testkey__",1):
            raise MemConnError()
        
    def produceKey(self,keyname):
        '''重新生成新的key，规则是 _hostname:key

        >>> mclient.produceKey('name')
        test:name
        '''
        if isinstance(keyname, basestring):
            return str(''.join([self._hostname,':',keyname]))
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


