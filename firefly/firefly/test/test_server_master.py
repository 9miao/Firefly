#coding:utf8
'''
Created on 2013-8-2

@author: lan
'''
import os
if os.name!='nt':
    from twisted.internet import epollreactor
    epollreactor.install()
    
def println(a):
    print a

if __name__=="__main__":
    from firefly.master.master import Master
    master = Master()
    master.config('config.json','test_server_main.py')
    master.start()
    
    