import numpy as np
from sklearn import preprocessing

class Days:

    def __init__(self):
        self._date      = []
        self._precip    = []
        self._moist_2   = []

    def add_day(self, _date, _precip, _moist_2):
        self._date.append( _date )
        self._precip.append( _precip )
        self._moist_2.append( _moist_2 )
    
    def get_date(self):
        return np.array(self._date)

    def get_precip(self):
        _tmp = self.norm(self._precip)
        return _tmp
    
    def get_moist_2(self):
        _tmp = self.norm(self._moist_2)
        return _tmp

    def norm(self, x):
        _tmp = np.array(x).reshape(-1, 1)
        
        _res = []
        for i in _tmp:
            _res.append(_tmp)
        return np.array(_res)
