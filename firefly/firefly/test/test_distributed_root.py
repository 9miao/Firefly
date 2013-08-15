#coding:utf8
'''
Created on 2011-10-17

@author: lan
'''
import services
from distributed.root import PBRoot,BilateralFactory
from twisted.internet import reactor
from twisted.python import log
import sys
reactor = reactor
log.startLogging(sys.stdout)
    
root = PBRoot()
ser = services.Service('test')
root.addServiceChannel(ser)


def serviceHandle(target):
    '''服务处理
    @param target: func Object
    '''
    ser.mapTarget(target)

@serviceHandle
def printData1(data,data1):
    print data,data1
    print "############################"
#    d = root.callChildByName("test_node",1,u'Root测试')
    return data

@serviceHandle
def printData2(data,data1):
    print data,data1
    print "############################"
#    d = root.callChildByName("test_node",1,u'Root测试')
    return data

if __name__=='__main__':
    reactor.listenTCP(8800, BilateralFactory(root))
    reactor.callLater(5,root.callChildByName,'test_node','printOK','asdfawefasdf')
    reactor.run()
