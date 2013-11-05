#coding:utf8
'''
Created on 2013-7-31

@author: lan (www.9miao.com)
'''
from firefly.dbentrust.dbpool import dbpool
from firefly.dbentrust.madminanager import MAdminManager
from firefly.dbentrust import mmode 
from firefly.dbentrust.memclient import mclient
import time


if __name__=="__main__":

    
#    CREATE TABLE `tb_register` (
#   `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
#   `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '用户名',
#   `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '用户密码',
#   PRIMARY KEY (`id`,`username`)
#   ) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8
#
    hostname = "localhost"
    username = 'root'
    password = '111'
    dbname = 'test'
    charset = 'utf8'
    tablename = "tb_user"#

    mmanager = MAdminManager()
    mclient.connect(['127.0.0.1:11212'], 'localhost')
    mclient.set('a', 1)
    print mclient.get('a')

