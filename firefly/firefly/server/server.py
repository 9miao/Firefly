#coding:utf8
'''
Created on 2013-8-2

@author: lan (www.9miao.com)
'''
from firefly.netconnect.protoc import LiberateFactory
from twisted.web import vhost
from firefly.web.delayrequest import DelaySite
from firefly.distributed.root import PBRoot,BilateralFactory
from firefly.distributed.node import RemoteObject
from firefly.dbentrust.dbpool import dbpool
from firefly.dbentrust.memclient import mclient
from logobj import loogoo
from globalobject import GlobalObject
from twisted.python import log
from twisted.internet import reactor
from firefly.utils import services
import os,sys,affinity

reactor = reactor

def serverStop():
    log.msg('stop')
    if GlobalObject().stophandler:
        GlobalObject().stophandler()
    reactor.callLater(0.5,reactor.stop)
    return True

class FFServer:
    
    def __init__(self):
        '''
        '''
        self.netfactory = None#net前端
        self.root = None#分布式root节点
        self.webroot = None#http服务
        self.remote = {}#remote节点
        self.master_remote = None
        self.db = None
        self.mem = None
        self.servername = None
        self.remoteportlist = []
        
    def config(self, config, servername=None, dbconfig=None,
                memconfig=None, masterconf=None):
        '''配置服务器
        '''
        GlobalObject().json_config = config
        netport = config.get('netport')#客户端连接
        webport = config.get('webport')#http连接
        rootport = config.get('rootport')#root节点配置
        self.remoteportlist = config.get('remoteport',[])#remote节点配置列表
        if not servername:
            servername = config.get('name')#服务器名称
        logpath = config.get('log')#日志
        hasdb = config.get('db')#数据库连接
        hasmem = config.get('mem')#memcached连接
        app = config.get('app')#入口模块名称
        cpuid = config.get('cpu')#绑定cpu
        mreload = config.get('reload')#重新加载模块名称
        self.servername = servername
        if masterconf:
            masterport = masterconf.get('rootport')
            masterhost = masterconf.get('roothost')
            self.master_remote = RemoteObject(servername)
            addr = ('localhost',masterport) if not masterhost else (masterhost,masterport)
            self.master_remote.connect(addr)
            GlobalObject().masterremote = self.master_remote
            
        if netport:
            self.netfactory = LiberateFactory()
            netservice = services.CommandService("netservice")
            self.netfactory.addServiceChannel(netservice)
            reactor.listenTCP(netport,self.netfactory)
            
        if webport:
            self.webroot = vhost.NameVirtualHost()
            GlobalObject().webroot = self.webroot
            reactor.listenTCP(webport, DelaySite(self.webroot))
            
        if rootport:
            self.root = PBRoot()
            rootservice = services.Service("rootservice")
            self.root.addServiceChannel(rootservice)
            reactor.listenTCP(rootport, BilateralFactory(self.root))
            
        for cnf in self.remoteportlist:
            rname = cnf.get('rootname')
            self.remote[rname] = RemoteObject(self.servername)
            
        if hasdb and dbconfig:
            log.msg(str(dbconfig))
            dbpool.initPool(**dbconfig)
            
        if hasmem and memconfig:
            urls = memconfig.get('urls')
            hostname = str(memconfig.get('hostname'))
            mclient.connect(urls, hostname)
            
        if logpath:
            log.addObserver(loogoo(logpath))#日志处理
        log.startLogging(sys.stdout)
        
        if cpuid:
            affinity.set_process_affinity_mask(os.getpid(), cpuid)
        GlobalObject().config(netfactory = self.netfactory, root=self.root,
                    remote = self.remote)
        if app:
            __import__(app)
        if mreload:
            GlobalObject().reloadmodule = __import__(mreload)
        GlobalObject().remote_connect = self.remote_connect
        import admin
        
    def remote_connect(self, rname, rhost):
        """
        """
        for cnf in self.remoteportlist:
            _rname = cnf.get('rootname')
            if rname == _rname:
                rport = cnf.get('rootport')
                if not rhost:
                    addr = ('localhost',rport)
                else:
                    addr = (rhost,rport)
                self.remote[rname].connect(addr)
                break
        
    def start(self):
        '''启动服务器
        '''
        log.msg('%s start...'%self.servername)
        log.msg('%s pid: %s'%(self.servername,os.getpid()))
        reactor.run()
        
        
