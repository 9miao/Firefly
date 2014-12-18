#coding:utf8
'''
Created on 2013-5-8

@author: lan (www.9miao.com)
'''
from DBUtils.PooledDB import PooledDB
import MySQLdb

DBCS = {'mysql':MySQLdb,}

class DBPool(object):
    '''数据库连接池
    '''
    
    def initPool(self,**kw):
        '''根据连接配置初始化连接池配置信息.

        >>> aa = {'host':"localhost",'user':'root','passwd':'111','db':'test','port':3306,'charset':'utf8'}
        >>> dbpool.initPool(**aa)
        '''
        self.config = kw
        creator = DBCS.get(kw.get('engine','mysql'),MySQLdb)
        self.pool = PooledDB(creator,5,**kw)
        
    def connection(self):
        return self.pool.connection()

#数据库连接池对象
dbpool = DBPool()

