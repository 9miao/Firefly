#coding:utf8
'''
Created on 2013-5-8

@author: lan (www.9miao.com)
'''
from memclient import mclient
from memobject import MemObject
import util
import time

MMODE_STATE_ORI = 0     #未变更
MMODE_STATE_NEW = 1     #创建
MMODE_STATE_UPDATE = 2  #更新
MMODE_STATE_DEL = 3     #删除



TIMEOUT = 1800

def _insert(args):
    record,pkname,mmname,cls =  args
    pk = record[pkname]
    mm = cls(mmname+':%s'%pk,pkname,data=record)
    mm.insert()
    return pk

class PKValueError(ValueError): 
    """
    """
    def __init__(self, data):
        ValueError.__init__(self)
        self.data = data
    def __str__(self):
        return "new record has no 'PK': %s" % (self.data)

class MMode(MemObject):
    """内存数据模型
    """
    def __init__(self, name,pk,data={}):
        """
        """
        MemObject.__init__(self, name, mclient)
        self._state = MMODE_STATE_ORI#对象的状态 0未变更  1新建 2更新 3删除
        self._pk = pk
        self.data = data
        self._time = time.time()
        
    def update(self, key, values):
        data = self.get_multi(['data','_state'])
        ntime = time.time()
        data['data'].update({key:values})
        if data.get('_state')==MMODE_STATE_NEW:
            props = {'data':data.get('data'),'_time':ntime}
        else:
            props = {'_state':MMODE_STATE_UPDATE,'data':data.get('data'),'_time':ntime}
        return MemObject.update_multi(self, props)
    
    def update_multi(self, mapping):
        ntime = time.time()
        data = self.get_multi(['data','_state'])
        data['data'].update(mapping)
        if data.get('_state')==MMODE_STATE_NEW:
            props = {'data':data.get('data'),'_time':ntime}
        else:
            props = {'_state':MMODE_STATE_UPDATE,'data':data.get('data'),'_time':ntime}
        return MemObject.update_multi(self, props)
    
    def get(self, key):
        ntime = time.time()
        MemObject.update(self, "_time", ntime)
        return MemObject.get(self, key)
    
    def get_multi(self, keys):
        ntime = time.time()
        MemObject.update(self, "_time", ntime)
        return MemObject.get_multi(self, keys)
    
    def delete(self):
        '''删除对象
        '''
        return MemObject.update(self,'_state',MMODE_STATE_DEL)
    
    def mdelete(self):
        """清理对象
        """
        self.syncDB()
        MemObject.mdelete(self)
    
    def IsEffective(self):
        '''检测对象是否有效
        '''
        if self.get('_state')==MMODE_STATE_DEL:
            return False
        return True
        
    def syncDB(self):
        """同步到数据库
        """
        state = self.get('_state')
        tablename = self._name.split(':')[0]
        if state==MMODE_STATE_ORI:
            return
        elif state==MMODE_STATE_NEW:
            props = self.get('data')
            pk = self.get('_pk')
            result = util.InsertIntoDB(tablename, props)
        elif state==MMODE_STATE_UPDATE:
            props = self.get('data')
            pk = self.get('_pk')
            prere = {pk:props.get(pk)}
            util.UpdateWithDict(tablename, props, prere)
            result = True
        else:
            pk = self.get('_pk')
            props = self.get('data')
            prere = {pk:props.get(pk)}
            result = util.DeleteFromDB(tablename,prere)
        if result:
            MemObject.update(self,'_state', MMODE_STATE_ORI)
            
    def checkSync(self,timeout=TIMEOUT):
        """检测同步
        """
        ntime = time.time()
        objtime = MemObject.get(self, '_time')
        if ntime  -objtime>=timeout and timeout:
            self.mdelete()
        else:
            self.syncDB()
        
        
class MFKMode(MemObject):
    """内存数据模型
    """
    def __init__(self, name,pklist = []):
        MemObject.__init__(self, name, mclient)
        self.pklist = pklist
        
class MAdmin(MemObject):
    
    def __init__(self, name,pk,timeout=TIMEOUT,**kw):
        MemObject.__init__(self, name, mclient)
        self._pk = pk
        self._fk = kw.get('fk','')
        self._incrkey = kw.get('incrkey','')
        self._incrvalue = kw.get('incrvalue',0)
        self._timeout = timeout
        
    def insert(self):
        if self._incrkey and not self.get("_incrvalue"):
            self._incrvalue = util.GetTableIncrValue(self._name)
        MemObject.insert(self)
        
    def load(self):
        '''读取数据到数据库中
        '''
        mmname = self._name
        recordlist = util.ReadDataFromDB(mmname)
        for record in recordlist:
            pk = record[self._pk]
            mm = MMode(self._name+':%s'%pk,self._pk,data=record)
            mm.insert()
    
    @property
    def madmininfo(self):
        keys = self.__dict__.keys()
        info = self.get_multi(keys)
        return info
    
    def getAllPkByFk(self,fk):
        '''根据外键获取主键列表
        '''
        name = '%s_fk:%s'%(self._name,fk)
        fkmm = MFKMode(name)
        pklist = fkmm.get('pklist')
        if pklist is not None:
            return pklist
        props = {self._fk:fk}
        dbkeylist = util.getAllPkByFkInDB(self._name, self._pk, props)
        name = '%s_fk:%s'%(self._name,fk)
        fkmm = MFKMode(name, pklist = dbkeylist)
        fkmm.insert()
        return dbkeylist
        
    def getObj(self,pk):
        '''
        '''
        mm = MMode(self._name+':%s'%pk,self._pk)
        if not mm.IsEffective():
            return None
        if mm.get('data'):
            return mm
        props = {self._pk:pk}
        record = util.GetOneRecordInfo(self._name,props)
        if not record:
            return None
        mm =  MMode(self._name+':%s'%pk,self._pk,data = record)
        mm.insert()
        return mm
    
    def getObjData(self,pk):
        '''
        '''
        mm = MMode(self._name+':%s'%pk,self._pk)
        if not mm.IsEffective():
            return None
        data = mm.get('data')
        if mm.get('data'):
            return data
        props = {self._pk:pk}
        record = util.GetOneRecordInfo(self._name,props)
        if not record:
            return None
        mm =  MMode(self._name+':%s'%pk,self._pk,data = record)
        mm.insert()
        return record
        
    
    def getObjList(self,pklist):
        '''
        '''
        _pklist = []
        objlist = []
        for pk in pklist:
            mm = MMode(self._name+':%s'%pk,self._pk)
            if not mm.IsEffective():
                continue
            if mm.get('data'):
                objlist.append(mm)
            else:
                _pklist.append(pk)
        if _pklist:
            recordlist = util.GetRecordList(self._name, self._pk,_pklist)
            for record in recordlist:
                pk = record[self._pk]
                mm =  MMode(self._name+':%s'%pk,self._pk,data = record)
                mm.insert()
                objlist.append(mm)
        return objlist
    
    def deleteMode(self,pk):
        '''
        '''
        mm = self.getObj(pk)
        if mm:
            if self._fk:
                data = mm.get('data')
                if data:
                    fk = data.get(self._fk,0)
                    name = '%s_fk:%s'%(self._name,fk)
                    fkmm = MFKMode(name)
                    pklist = fkmm.get('pklist')
                    if pklist and pk in pklist:
                        pklist.remove(pk)
                    fkmm.update('pklist', pklist)
            mm.delete()
        return True
    
    def checkAll(self):
        key = '%s:%s:'%(mclient._hostname,self._name)
        _pklist = util.getallkeys(key, mclient.connection)
        for pk in _pklist:
            mm = MMode(self._name+':%s'%pk,self._pk)
            if not mm.IsEffective():
                mm.mdelete()
                continue
            if not mm.get('data'):
                continue
            mm.checkSync(timeout=self._timeout)
        self.deleteAllFk()
        
    def deleteAllFk(self):
        """删除所有的外键
        """
        key = '%s:%s_fk:'%(mclient._hostname,self._name)
        _fklist = util.getallkeys(key, mclient.connection)
        for fk in _fklist:
            name = '%s_fk:%s'%(self._name,fk)
            fkmm = MFKMode(name)
            fkmm.mdelete()
        
    def new(self,data):
        """创建一个新的对象
        """
        incrkey = self._incrkey
        if incrkey:
            incrvalue = self.incr('_incrvalue', 1)
            data[incrkey] = incrvalue - 1 
            pk = data.get(self._pk)
            if pk is None:
                raise PKValueError(data)
            mm = MMode(self._name+':%s'%pk,self._pk,data=data)
            setattr(mm,incrkey,pk)
        else:
            pk = data.get(self._pk)
            mm = MMode(self._name+':%s'%pk,self._pk,data=data)
        if self._fk:
            fk = data.get(self._fk,0)
            name = '%s_fk:%s'%(self._name,fk)
            fkmm = MFKMode(name)
            pklist = fkmm.get('pklist')
            if pklist is None:
                pklist = self.getAllPkByFk(fk)
            pklist.append(pk)
            fkmm.update('pklist', pklist)
        setattr(mm,'_state',MMODE_STATE_NEW)
        mm.insert()
        return mm
        
