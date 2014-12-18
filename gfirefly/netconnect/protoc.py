#coding:utf8
'''
Created on 2014-2-23
登陆服务器协议
@author: lan (www.9miao.com)
'''
from gtwisted.core import protocols,reactor
from gtwisted.utils import log
from gfirefly.netconnect.manager import ConnectionManager
from gfirefly.netconnect.datapack import DataPackProtoc
reactor = reactor

class LiberateProtocol(protocols.BaseProtocol):
    '''协议'''
    
    buff = ""
    
    def connectionMade(self):
        '''连接建立处理
        '''
        address = self.transport.getAddress()
        log.msg('Client %d login in.[%s,%d]'%(self.transport.sessionno,\
                address[0],address[1]))
        self.factory.connmanager.addConnection(self)
        self.factory.doConnectionMade(self)
        
    def connectionLost(self,reason):
        '''连接断开处理
        '''
        log.msg('Client %d login out.'%(self.transport.sessionno))
        self.factory.doConnectionLost(self)
        self.factory.connmanager.dropConnectionByID(self.transport.sessionno)
        
    def safeToWriteData(self,data,command):
        '''线程安全的向客户端发送数据
        @param data: str 要向客户端写的数据
        '''
        if data is None:
            return
        senddata = self.factory.produceResult(data,command)
        self.transport.sendall(senddata)
        
    def dataReceived(self, data):
        
        '''数据到达处理
        @param data: str 客户端传送过来的数据
        '''
        length = self.factory.dataprotocl.getHeadlength()#获取协议头的长度
        self.buff += data
        while self.buff.__len__() >= length: 
            unpackdata = self.factory.dataprotocl.unpack(self.buff[:length])
            if not unpackdata.get('result'):
                log.msg('illegal data package --')
                self.factory.connmanager.loseConnection(self.transport.sessionno)
                break
            command = unpackdata.get('command')
            rlength = unpackdata.get('length')
            request = self.buff[length:length+rlength]
            if request.__len__()< rlength:
                log.msg('some data lose')
                break
            self.buff = self.buff[length+rlength:]
            response = self.factory.doDataReceived(self,command,request)
            if not response:
                continue
            self.safeToWriteData(response, command)
            
class LiberateFactory(protocols.ServerFactory):
    '''协议工厂'''
    
    protocol = LiberateProtocol
    
    def __init__(self,dataprotocl=DataPackProtoc()):
        '''初始化
        '''
        protocols.ServerFactory.__init__(self)
        self.service = None
        self.connmanager = ConnectionManager()
        self.dataprotocl = dataprotocl
        
    def setDataProtocl(self,dataprotocl):
        '''
        '''
        self.dataprotocl = dataprotocl
        
    def doConnectionMade(self,conn):
        '''当连接建立时的处理'''
        pass
    
    def doConnectionLost(self,conn):
        '''连接断开时的处理'''
        pass
    
    def addServiceChannel(self,service):
        '''添加服务通道'''
        self.service = service
    
    def doDataReceived(self,conn,commandID,data):
        '''数据到达时的处理'''
        response = self.service.callTarget(commandID,conn,data)
        return response
    
    def produceResult(self,command,response):
        '''产生客户端需要的最终结果
        @param response: str 分布式客户端获取的结果
        '''
        return self.dataprotocl.pack(command,response)
    
    def loseConnection(self,connID):
        """主动端口与客户端的连接
        """
        self.connmanager.loseConnection(connID)
    
    def pushObject(self,topicID , msg, sendList):
        '''服务端向客户端推消息
        @param topicID: int 消息的主题id号
        @param msg: 消息的类容，protobuf结构类型
        @param sendList: 推向的目标列表(客户端id 列表)
        '''
        self.connmanager.pushObject(topicID, msg, sendList)
        

