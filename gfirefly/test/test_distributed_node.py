#coding:utf8
'''
Created on 2011-10-17

@author: lan (www.9miao.com)
'''
from gfirefly.utils import services
from gfirefly.distributed.node import RemoteObject
from gtwisted.core import reactor
from gtwisted.utils import log
import sys

log.startLogging(sys.stdout)

reactor = reactor

addr = ('localhost',9090)#目标主机的地址
remote = RemoteObject('test_node')#实例化远程调用对象

service = services.CommandService('reference')#实例化一条服务对象
remote.addServiceChannel(service)


def serviceHandle(target):
    '''服务处理
    @param target: func Object
    '''
    service.mapTarget(target)

@serviceHandle
def printOK_1(data):
    print data
    print "############################"
    return "call printOK_01"
    
def apptest(commandID,*args,**kw):
    d = remote.callRemote(commandID,*args,**kw)
    print "apptest result:",d
    return d

def startClient():
    reactor.callLater(3,apptest,'printData1',u"node测试1",u"node测试2")
    remote.connect(addr)#连接远程主机
    reactor.run()

if __name__=='__main__':
    startClient()

