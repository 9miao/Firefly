#coding:utf8
'''
Created on 2012-7-10
memcached 关系对象
通过key键的名称前缀来建立
各个key-value 直接的关系
@author: lan (www.9miao.com)
'''

class MemObject:
    '''memcached 关系对象
    '''
    
    def __init__(self,name,mc):
        '''
        @param name: str 对象的名称
        @param _lock: int 对象锁  为1时表示对象被锁定无法进行修改
        '''
        self._client = mc
        self._name = name
        self._lock = 0
        
    def produceKey(self,keyname):
        '''重新生成key
        '''
        if isinstance(keyname, basestring):
            return ''.join([self._name,':',keyname])
        else:
            raise "type error"
        
    def locked(self):
        '''检测对象是否被锁定
        '''
        key = self.produceKey('_lock')
        return self._client.get(key)
    
    def lock(self):
        '''锁定对象
        '''
        key = self.produceKey('_lock')
        self._client.set(key, 1)
        
    def release(self):
        '''释放锁
        '''
        key = self.produceKey('_lock')
        self._client.set(key, 0)
        
    def get(self,key):
        '''获取对象值
        '''
        key = self.produceKey(key)
        return self._client.get(key)
    
    def get_multi(self,keys):
        '''一次获取多个key的值
        @param keys: list(str) key的列表
        '''
        keynamelist = [self.produceKey(keyname) for keyname in keys]
        olddict = self._client.get_multi(keynamelist)
        newdict = dict(zip([keyname.split(':')[-1] for keyname in olddict.keys()],
                              olddict.values()))
        return newdict

    def update(self,key,values):
        '''修改对象的值
        '''
        if self.locked():
            return False
        key = self.produceKey(key)
        return self._client.set(key,values)
            
    def update_multi(self,mapping):
        '''同时修改多个key值
        '''
        if self.locked():
            return False
        newmapping = dict(zip([self.produceKey(keyname) for keyname in mapping.keys()],
                              mapping.values()))
        return self._client.set_multi(newmapping)
        
    def mdelete(self):
        '''删除memcache中的数据
        '''
        nowdict = dict(self.__dict__)
        del nowdict['_client']
        keys = nowdict.keys()
        keys = [self.produceKey(key) for key in keys]
        self._client.delete_multi(keys)
            
    def incr(self, key, delta):
        '''自增
        '''
        key = self.produceKey(key)
        return self._client.incr( key, delta)
        
    def insert(self):
        '''插入对象记录
        '''
        nowdict = dict(self.__dict__)
        del nowdict['_client']
        newmapping = dict(zip([self.produceKey(keyname) for keyname in nowdict.keys()],
                              nowdict.values()))
        self._client.set_multi(newmapping)
        
        
        
        
