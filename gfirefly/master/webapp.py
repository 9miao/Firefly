#coding:utf8
'''
Created on 2013-8-7

@author: lan (www.9miao.com)
'''
from gtwisted.core import reactor
from gfirefly.server.globalobject import webserviceHandle,GlobalObject
reactor = reactor

@webserviceHandle('/stop')
def stop():
    '''stop service
    '''
    for child in GlobalObject().root.childsmanager._childs.values():
        child.callbackChildNotForResult('serverStop')
    reactor.callLater(0.5,reactor.stop)
    return "stop"

@webserviceHandle('/reloadmodule')
def reloadmodule():
    '''reload module
    '''
    for child in GlobalObject().root.childsmanager._childs.values():
        child.callbackChildNotForResult('sreload')
    return "reload"




