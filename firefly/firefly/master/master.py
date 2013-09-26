#coding:utf8
'''
Created on 2013-8-2

@author: lan (www.9miao.com)
'''
import subprocess,json,sys
from twisted.internet import reactor
from firefly.utils import  services
from firefly.distributed.root import PBRoot,BilateralFactory
from firefly.server.globalobject import GlobalObject
from twisted.web import vhost
from firefly.web.delayrequest import DelaySite
from twisted.python import log
from firefly.server.logobj import loogoo

reactor = reactor

class Master:
    
    def __init__(self):
        """
        """
        self.configpath = None
        self.mainpath = None
        self.root = None
        self.webroot = None
        
    def config(self,configpath,mainpath):
        """
        """
        self.configpath = configpath
        self.mainpath = mainpath
        self.masterapp()
        
    def masterapp(self):
        config = json.load(open(self.configpath,'r'))
        mastercnf = config.get('master')
        rootport = mastercnf.get('rootport')
        webport = mastercnf.get('webport')
        masterlog = mastercnf.get('log')
        self.root = PBRoot()
        rootservice = services.Service("rootservice")
        self.root.addServiceChannel(rootservice)
        self.webroot = vhost.NameVirtualHost()
        self.webroot.addHost('0.0.0.0', './')
        GlobalObject().root = self.root
        GlobalObject().webroot = self.webroot
        if masterlog:
            log.addObserver(loogoo(masterlog))#日志处理
        log.startLogging(sys.stdout)
        import webapp
        import rootapp
        reactor.listenTCP(webport, DelaySite(self.webroot))
        reactor.listenTCP(rootport, BilateralFactory(self.root))
        
    def start(self):
        '''
        '''
        config = json.load(open(self.configpath,'r'))
        sersconf = config.get('servers')
        for sername in sersconf.keys():
            cmds = 'python %s %s %s'%(self.mainpath,sername,self.configpath)
            subprocess.Popen(cmds,shell=True)
        reactor.run()
            
