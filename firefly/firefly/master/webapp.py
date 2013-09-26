#coding:utf8
'''
Created on 2013-8-7

@author: lan (www.9miao.com)
'''
from twisted.web import resource
from twisted.internet import reactor
from firefly.server.globalobject import GlobalObject
root = GlobalObject().webroot
reactor = reactor
def ErrorBack(reason):
    pass

def masterwebHandle(cls):
    '''
    '''
    root.putChild(cls.__name__, cls())

@masterwebHandle
class stop(resource.Resource):
    '''stop service'''
    
    def render(self, request):
        '''
        '''
        for child in GlobalObject().root.childsmanager._childs.values():
            d = child.callbackChild('serverStop')
            d.addCallback(ErrorBack)
        reactor.callLater(0.5,reactor.stop)
        return "stop"

@masterwebHandle
class reloadmodule(resource.Resource):
    '''reload module'''
    
    def render(self, request):
        '''
        '''
        for child in GlobalObject().root.childsmanager._childs.values():
            d = child.callbackChild('sreload')
            d.addCallback(ErrorBack)
        return "reload"




