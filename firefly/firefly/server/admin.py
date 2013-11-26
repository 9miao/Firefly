#coding:utf8
'''
Created on 2013-8-12

@author: lan (www.9miao.com)
'''
from globalobject import GlobalObject,masterserviceHandle
from twisted.internet import reactor
from twisted.python import log

reactor = reactor


@masterserviceHandle
def serverStop():
    """
    """
    log.msg('stop')
    if GlobalObject().stophandler:
        GlobalObject().stophandler()
    reactor.callLater(0.5,reactor.stop)
    return True

@masterserviceHandle
def sreload():
    """
    """
    log.msg('reload')
    if GlobalObject().reloadmodule:
        reload(GlobalObject().reloadmodule)
    return True

@masterserviceHandle
def remote_connect(rname, rhost):
    """
    """
    GlobalObject().remote_connect(rname, rhost)

