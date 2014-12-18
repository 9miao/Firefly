#coding:utf8
'''
Created on 2013-8-8

@author: lan (www.9miao.com)
'''
from gfirefly import management
import sys

if __name__ == "__main__":
    args = sys.argv
    management.execute_commands(*args)