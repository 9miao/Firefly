#coding:utf8
'''
Created on 2013-8-2

@author: lan (www.9miao.com)
'''
import subprocess,json,sys
from gtwisted.core import reactor
from gfirefly.utils import  services
from gfirefly.distributed.root import PBRoot,BilateralFactory
from gfirefly.server.globalobject import GlobalObject
from gtwisted.utils import log
from gfirefly.server.logobj import loogoo
from flask import Flask

reactor = reactor

MULTI_SERVER_MODE = 1
SINGLE_SERVER_MODE = 2
MASTER_SERVER_MODE = 3



class Master:
    """
    """
    
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
        
    def masterapp(self):
        """
        """
        config = json.load(open(self.configpath,'r'))
        GlobalObject().json_config = config
        mastercnf = config.get('master')
        rootport = mastercnf.get('rootport')
        webport = mastercnf.get('webport')
        masterlog = mastercnf.get('log')
        self.root = PBRoot()
        rootservice = services.Service("rootservice")
        self.root.addServiceChannel(rootservice)
        self.webroot = Flask("master")
        GlobalObject().root = self.root
        GlobalObject().webroot = self.webroot
        if masterlog:
            log.addObserver(loogoo(masterlog))#日志处理
        log.startLogging(sys.stdout)
        import webapp
        import rootapp
        reactor.listenWSGI(webport, self.webroot)
        reactor.listenTCP(rootport, BilateralFactory(self.root))
        
    def start(self):
        '''
        '''
        sys_args = sys.argv
        if len(sys_args)>2 and sys_args[1] == "single":
            server_name = sys_args[2]
            if server_name == "master":
                mode = MASTER_SERVER_MODE
            else:
                mode = SINGLE_SERVER_MODE
        else:
            mode = MULTI_SERVER_MODE
            server_name = ""
            
        if mode == MULTI_SERVER_MODE:
            self.masterapp()
            config = json.load(open(self.configpath,'r'))
            sersconf = config.get('servers')
            for sername in sersconf.keys():
                cmds = 'python %s %s %s'%(self.mainpath,sername,self.configpath)
                subprocess.Popen(cmds,shell=True)
            reactor.run()
        elif mode == SINGLE_SERVER_MODE:
            config = json.load(open(self.configpath,'r'))
            sername = server_name
            cmds = 'python %s %s %s'%(self.mainpath,sername,self.configpath)
            subprocess.Popen(cmds,shell=True)
        else:
            self.masterapp()
            reactor.run()
            
            
