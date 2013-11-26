#coding:utf8
'''
Created on 2013-8-8

@author: lan (www.9miao.com)
'''
import sys,os
startmasterfile =['#coding:utf8\n', '\n', 'import os\n', "if os.name!='nt' and os.name!='posix':\n", '    from twisted.internet import epollreactor\n', '    epollreactor.install()\n', '\n', 'if __name__=="__main__":\n', '    from firefly.master.master import Master\n', '    master = Master()\n', "    master.config('config.json','appmain.py')\n", '    master.start()\n', '    \n', '    ']
configfile = ['{\n', 
              '"master":{"roothost":"localhost","rootport":9999,"webport":9998},\n',
               '"servers":{\n', '"net":{"netport":1000,"name":"gate","remoteport":[{"rootport":20001,"rootname":"gate"}],"app":"app.apptest"},\n',
               '"gate":{"rootport":20001,"name":"gate"}\n',
                '},\n', '"db":{\n', '"host":"localhost",\n',
                 '"user":"root",\n', '"passwd":"111",\n',
                  '"port":3306,\n',
                   '"db":"test",\n',
                    '"charset":"utf8"\n',
                     '},\n',
                     '"memcached":{\n',
                     '"urls":["127.0.0.1:11211"],\n',
                     '"hostname":"test"\n',
                     '}\n',
                      '}\n']
appmainfile = ['#coding:utf8\n', '\n','import os\n', "if os.name!='nt' and os.name!='posix':\n", '    from twisted.internet import epollreactor\n', '    epollreactor.install()\n', '\n', 'import json,sys\n', 'from firefly.server.server import FFServer\n', '\n', 'if __name__=="__main__":\n', '    args = sys.argv\n', '    servername = None\n', '    config = None\n', '    if len(args)>2:\n', '        servername = args[1]\n', "        config = json.load(open(args[2],'r'))\n", '    else:\n', '        raise ValueError\n', "    dbconf = config.get('db')\n", "    memconf = config.get('memcached')\n", "    sersconf = config.get('servers',{})\n", "    masterconf = config.get('master',{})\n", '    serconfig = sersconf.get(servername)\n', '    ser = FFServer()\n', '    ser.config(serconfig, servername=servername, dbconfig=dbconf, memconfig=memconf, masterconf=masterconf)\n', '    ser.start()\n', '    \n', '    ']
apptestfile = ['#coding:utf8\n', '\n', 'from firefly.server.globalobject import netserviceHandle\n', '\n', '@netserviceHandle\n', 'def echo_1(_conn,data):\n', '    return data\n', '\n', '    \n', '\n', '\n']
clientfile = ['#coding:utf8\n', '\n', 'import time\n', '\n', 'from socket import AF_INET,SOCK_STREAM,socket\n', 'from thread import start_new\n', 'import struct\n', "HOST='localhost'\n", 'PORT=1000\n', 'BUFSIZE=1024\n', 'ADDR=(HOST , PORT)\n', 'client = socket(AF_INET,SOCK_STREAM)\n', 'client.connect(ADDR)\n', '\n', 'def sendData(sendstr,commandId):\n', '    HEAD_0 = chr(0)\n', '    HEAD_1 = chr(0)\n', '    HEAD_2 = chr(0)\n', '    HEAD_3 = chr(0)\n', '    ProtoVersion = chr(0)\n', '    ServerVersion = 0\n', '    sendstr = sendstr\n', "    data = struct.pack('!sssss3I',HEAD_0,HEAD_1,HEAD_2,\\\n", '                       HEAD_3,ProtoVersion,ServerVersion,\\\n', '                       len(sendstr)+4,commandId)\n', '    senddata = data+sendstr\n', '    return senddata\n', '\n', 'def resolveRecvdata(data):\n', "    head = struct.unpack('!sssss3I',data[:17])\n", '    lenght = head[6]\n', '    data = data[17:17+lenght]\n', '    return data\n', '\n', 's1 = time.time()\n', '\n', 'def start():\n', '    for i in xrange(10):\n', "        client.sendall(sendData('asdfe',1))\n", '\n', 'for i in range(10):\n', '    start_new(start,())\n', 'while True:\n', '    pass\n', '\n']


def createfile(rootpath,path,filecontent):
    '''
    '''
    mfile = open(rootpath+'/'+path,'w')
    mfile.writelines(filecontent)
    mfile.close()


def execute(*args):
    if not args:
        sys.stdout.write("command error \n")
    projectname = args[0]
    sys.stdout.write("create dir %s \n"%projectname)
    rootpath = projectname
    os.mkdir(rootpath)
    createfile(rootpath,'startmaster.py',startmasterfile)
    createfile(rootpath,'config.json',configfile)
    createfile(rootpath,'appmain.py',appmainfile)
    
    rootpath = projectname+'/'+'app'
    os.mkdir(rootpath)
    createfile(rootpath,'__init__.py',[])
    createfile(rootpath,'apptest.py',apptestfile)
    
    rootpath = projectname+'/'+'tool'
    os.mkdir(rootpath)
    createfile(rootpath,'__init__.py',[])
    createfile(rootpath,'clienttest.py',clientfile)
    
    sys.stdout.write("create success \n")
    
    