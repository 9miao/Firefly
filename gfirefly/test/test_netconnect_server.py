#coding:utf8
'''
Created on 2011-10-3

@author: lan (www.9miao.com)
'''
import sys
from gtwisted.core import reactor
        
from gtwisted.utils import log
from gfirefly.utils import services
from gfirefly.netconnect.protoc import LiberateFactory

# reactor = reactor
service = services.CommandService("loginService")

def serviceHandle(target):
    '''服务处理
    @param target: func Object
    '''
    service.mapTarget(target)
    
factory = LiberateFactory()

def doConnectionLost(conn):
    print conn.transport

factory.doConnectionLost = doConnectionLost

def serverstart():
    '''服务配置
    '''
    log.startLogging(sys.stdout)
    factory.addServiceChannel(service)
    reactor.callLater(10,factory.pushObject,111,'asdfe',[0,1])
#     reactor.callLater(15,factory.loseConnection,0)
    reactor.listenTCP(1000,factory)
    reactor.run()
    
a = 0
    
@serviceHandle
def echo_1(_conn,data):
    global a
    a+=1
    print a
    return "0"

if __name__ == "__main__":
    
    serverstart()

