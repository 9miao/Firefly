#coding:utf8
'''
Created on 2013-5-8

@author: lan (www.9miao.com)
'''
from DBUtils.PooledDB import PooledDB
import MySQLdb

DBCS = {'mysql':MySQLdb,}

class DBPool(object):
    '''
    '''
    def initPool(self,**kw):
        '''
        '''
        self.config = kw
        self.pool = PooledDB(MySQLdb,5,host = kw.get("host"), user = kw.get("user"),
                            passwd = kw.get("passwd"),db = kw.get("db"),
                            port=kw.get("port"),charset=kw.get("charset"))
    def connection(self):
        return self.pool.connection()

dbpool = DBPool()


