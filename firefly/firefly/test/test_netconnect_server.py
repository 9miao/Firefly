#coding:utf8
'''
Created on 2011-10-3

@author: lan (www.9miao.com)
'''
import sys,os

if os.name!='nt':#对系统的类型的判断，如果不是NT系统的话使用epoll
    from twisted.internet import epollreactor
    epollreactor.install()
        
from twisted.internet import reactor
from twisted.python import log
from firefly.utils import services
from firefly.netconnect.protoc import LiberateFactory

reactor = reactor
service = services.CommandService("loginService",runstyle= services.Service.PARALLEL_STYLE)

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
    reactor.callLater(10,factory.pushObject,111,'asdfe',[0])
    reactor.callLater(15,factory.loseConnection,0)
    reactor.listenTCP(9090,factory)
    reactor.run()
    
@serviceHandle
def echo_111(_conn,data):
    return "欢迎"

if __name__ == "__main__":
    
    serverstart()

