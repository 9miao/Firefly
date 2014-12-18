#coding:utf8
'''
Created on 2013-10-17

@author: lan (www.9miao.com)
'''
from __future__ import division, absolute_import
from zope.interface import Interface


class IDataPackProtoc(Interface):
    
    def getHeadlength():
        """获取数据包的长度
        """
        pass
        
    def unpack():
        '''解包
        '''
        
    def pack():
        '''打包数据包
        '''
        
    
    

