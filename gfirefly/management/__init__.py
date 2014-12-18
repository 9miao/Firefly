#coding:utf8
'''
Created on 2013-8-8

@author: lan (www.9miao.com)
'''
from gfirefly.management import commands 
import sys

class CommandError(Exception): 
    """
    """
    def __str__(self):
        return "command error"

class Command:
    
    def __init__(self,subcommond,*args):
        '''工具类指令
        '''
        self.subcommond = subcommond
        self.args = args
        
    def execute(self):
        '''
        '''
        try:
            commmd = getattr(commands,self.subcommond )
            commmd.execute(*self.args)
        except:
            modes = dir(commands)
            lines = ["\t"+m+"\n" for m in modes if not m.startswith("_")]
            firstline = "args error\nargs:\n"
            print "".join([firstline,]+lines)
        
        
def execute_commands(*args):
    '''
    '''
    if len(args)<2:
        raise CommandError()
    subcommand = args[1]
    comm = Command(subcommand,*tuple(args[2:]))
    comm.execute()
    
    
    