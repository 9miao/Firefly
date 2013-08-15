#coding:utf8
'''
Created on 2013-8-8

@author: lan
'''
from firefly.management import commands 
import sys

class Command:
    
    def __init__(self,subcommond,*args):
        '''工具类指令
        '''
        self.subcommond = subcommond
        self.args = args
        
    def execute(self):
        '''
        '''
        commmd = getattr(commands,self.subcommond )
        commmd.execute(*self.args)
        
        
def execute_commands(*args):
    '''
    '''
    if len(args)<2:
        sys.stdout.write("command error")
    subcommand = args[1]
    comm = Command(subcommand,*tuple(args[2:]))
    comm.execute()
    
    
    