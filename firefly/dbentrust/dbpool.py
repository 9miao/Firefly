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
        creator = DBCS.get(kw.get('engine','mysql'),MySQLdb)
        self.pool = PooledDB(creator,5,**kw)
        
    def connection(self):
        return self.pool.connection()

dbpool = DBPool()

