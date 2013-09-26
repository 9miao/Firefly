#coding:utf8
'''
Created on 2011-10-17

@author: lan (www.9miao.com)
'''
from utils import services
from distributed.node import RemoteObject
from twisted.internet import reactor
from twisted.python import util,log
import sys

log.startLogging(sys.stdout)

reactor = reactor

addr = ('localhost',1000)#目标主机的地址
remote = RemoteObject('test_node')#实例化远程调用对象

service = services.Service('reference',services.Service.SINGLE_STYLE)#实例化一条服务对象
remote.addServiceChannel(service)


def serviceHandle(target):
    '''服务处理
    @param target: func Object
    '''
    service.mapTarget(target)

@serviceHandle
def printOK(data):
    print data
    print "############################"
    return "call printOK_01"
    
def apptest(commandID,*args,**kw):
    d = remote.callRemote(commandID,*args,**kw)
    d.addCallback(lambda a:util.println(a))
    return d

def startClient():
    reactor.callLater(1,apptest,'printData1',u"node测试1",u"node测试2")
    remote.connect(addr)#连接远程主机
    reactor.run()

if __name__=='__main__':
    startClient()

