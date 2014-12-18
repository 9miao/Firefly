#coding:utf8
'''
Created on 2013-5-22

@author: lan (www.9miao.com)
'''
from gfirefly.utils.singleton import Singleton

class MAdminManager:
    """一个单例管理器。作为所有madmin的管理者
    """
    __metaclass__ = Singleton
    
    def __init__(self):
        """初始化所有管理的的madmin的集合，放在self.admins中
        """
        self.admins = {}
        
    def registe(self,admin):
        """注册一个madmin对象到管理中.

        >>> madmin = MAdmin('tb_registe','characterId',incrkey='id')
        >>> MAdminManager().registe(madmin)
        """

        self.admins[admin._name] = admin
        
    def dropAdmin(self,adminname):
        """移除一个madmin对象.

        >>> MAdminManager().dropAdmin(madmin)
        """
        if self.admins.has_key(adminname):
            del self.admins[adminname]
    
    def getAdmin(self,adminname):
        """根据madmin的名字获取madmin对象

        >>> madmin = MAdminManager().getAdmin('tb_registe')
        """
        return self.admins.get(adminname)
    
    def checkAdmins(self):
        """遍历所有的madmin，与数据库进行同步。

        >>>MAdminManager().checkAdmins()
        """
        for admin in self.admins.values():
            admin.checkAll()
    
    
    
        