#coding:utf8
'''
Created on 2013-8-6

@author: lan (www.9miao.com)
'''
from gtwisted.utils import log
from zope.interface import implements
import datetime


class loogoo:
    '''日志处理
    '''
    implements(log.ILogObserver)
    
    def __init__(self,logpath):
        '''配置日志路径
        '''
        self.file = file(logpath, 'w')
        
    def __call__(self, eventDict):
        '''日志处理
        '''
        if 'logLevel' in eventDict:
            level = eventDict['logLevel']
        elif eventDict['isError']:
            level = 'ERROR'
        else:
            level = 'INFO'
        text = log.textFromEventDict(eventDict)
        if text is None or level != 'ERROR':
            return
        nowdate = datetime.datetime.now()
        self.file.write('['+str(nowdate)+']\n'+str(level)+ '\n\t' + text + '\r\n')
        self.file.flush()
        
