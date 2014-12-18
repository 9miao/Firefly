#coding:utf8
'''
Created on 2013-8-2

@author: lan (www.9miao.com)
'''
    
def println(a):
    print a

if __name__=="__main__":
    from gfirefly.master.master import Master
    master = Master()
    master.config('config.json','test_server_main.py')
    master.start()
    
    