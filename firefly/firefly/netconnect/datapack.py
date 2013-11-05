#coding:utf8
'''
Created on 2013-8-1

@author: lan (www.9miao.com)
'''
from twisted.python import log
import struct

class DataPackError(Exception):
    """An error occurred binding to an interface"""

    def __str__(self):
        s = self.__doc__
        if self.args:
            s = '%s: %s' % (s, ' '.join(self.args))
        s = '%s.' % s
        return s

class DataPackProtoc:
    """数据包协议
    """
    def __init__(self,HEAD_0 = 0,HEAD_1=0,HEAD_2=0,HEAD_3=0,protoVersion= 0,serverVersion=0):
        '''初始化
        @param HEAD_0: int 协议头0
        @param HEAD_1: int 协议头1
        @param HEAD_2: int 协议头2
        @param HEAD_3: int 协议头3
        @param protoVersion: int 协议头版本号
        @param serverVersion: int 服务版本号
        '''
        self.HEAD_0 = HEAD_0
        self.HEAD_1 = HEAD_1
        self.HEAD_2 = HEAD_2
        self.HEAD_3 = HEAD_3
        self.protoVersion = protoVersion
        self.serverVersion = serverVersion
        
    def setHEAD_0(self, HEAD_0):
        self.HEAD_0 = HEAD_0
        
    def setHEAD_1(self, HEAD_1):
        self.HEAD_1 = HEAD_1
    
    def setHEAD_2(self, HEAD_2):
        self.HEAD_2 = HEAD_2
        
    def setHEAD_3(self, HEAD_3):
        self.HEAD_3 = HEAD_3
        
    def setprotoVersion(self, protoVersion):
        self.protoVersion = protoVersion
    
    def setserverVersion(self, serverVersion):
        self.serverVersion = serverVersion
        
    def getHeadLenght(self):
        """获取数据包的长度
        """
        return 17
        
    def unpack(self,dpack):
        '''解包
        '''
        try:
            ud = struct.unpack('!sssss3I',dpack)
        except DataPackError,de:
            log.err(de)
            return {'result':False,'command':0,'lenght':0}
        HEAD_0 = ord(ud[0])
        HEAD_1 = ord(ud[1])
        HEAD_2 = ord(ud[2])
        HEAD_3 = ord(ud[3])
        protoVersion = ord(ud[4])
        serverVersion = ud[5]
        lenght = ud[6]-4
        command = ud[7]
        if HEAD_0 <>self.HEAD_0 or HEAD_1<>self.HEAD_1 or\
             HEAD_2<>self.HEAD_2 or HEAD_3<>self.HEAD_3 or\
              protoVersion<>self.protoVersion or serverVersion<>self.serverVersion:
            return {'result':False,'command':0,'lenght':0}
        return {'result':True,'command':command,'lenght':lenght}
        
    def pack(self,response,command):
        '''打包数据包
        '''
        HEAD_0 = chr(self.HEAD_0)
        HEAD_1 = chr(self.HEAD_1)
        HEAD_2 = chr(self.HEAD_2)
        HEAD_3 = chr(self.HEAD_3)
        protoVersion = chr(self.protoVersion)
        serverVersion = self.serverVersion
        lenght = response.__len__()+4
        commandID = command
        data = struct.pack('!sssss3I',HEAD_0,HEAD_1,HEAD_2,HEAD_3,\
                           protoVersion,serverVersion,lenght,commandID)
        data = data + response
        return data
        
    
    