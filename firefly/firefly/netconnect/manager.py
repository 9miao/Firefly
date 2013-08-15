#coding:utf8
'''
Created on 2010-12-31
连接管理器
@author: sean_lan
'''

from twisted.python import log
from connection import Connection

class ConnectionManager:
    ''' 连接管理器
    @param _connections: dict {connID:conn Object}管理的所有连接
    '''
    
    def __init__(self):
        '''初始化
        @param _connections: dict {connID:conn Object}
        '''
        self._connections = {}
        
    def getNowConnCnt(self):
        '''获取当前连接数量'''
        return len(self._connections.items())
    
    def addConnection(self, conn):
        '''加入一条连接
        @param _conn: Conn object
        '''
        _conn = Connection(conn)
        if self._connections.has_key(_conn.id):
            raise Exception("系统记录冲突")
        self._connections[_conn.id] = _conn
            
    def dropConnectionByID(self, connID):
        '''更加连接的id删除连接实例
        @param connID: int 连接的id
        '''
        try:
            del self._connections[connID]
        except Exception as e:
            log.msg(str(e))
        
    def getConnectionByID(self, connID):
        """根据ID获取一条连接
        @param connID: int 连接的id
        """
        return self._connections.get(connID,None)
    
    def loseConnection(self,connID):
        """根据连接ID主动端口与客户端的连接
        """
        conn = self.getConnectionByID(connID)
        if conn:
            conn.loseConnection()
        
    def pushObject(self,topicID , msg, sendList):
        """主动推送消息
        """
        for target in sendList:
            try:
                conn = self.getConnectionByID(target)
                if conn:
                    conn.safeToWriteData(topicID,msg)
            except Exception,e:
                log.err(str(e))


