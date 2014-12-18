#coding:utf8
'''
Created on 2014-2-23

@author: lan (www.9miao.com)
'''

class Connection:
    '''
    '''
    def __init__(self, _conn):
        '''
        id 连接的ID
        transport 连接的通道
        '''
        self.id = _conn.transport.sessionno
        self.instance = _conn
        
    def loseConnection(self):
        '''断开与客户端的连接
        '''
        self.instance.transport.close()
    
    def safeToWriteData(self,topicID,msg):
        """发送消息
        """
        self.instance.safeToWriteData(msg,topicID)
        
        
        