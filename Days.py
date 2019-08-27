import numpy as np
from sklearn import preprocessing

class Days:

    def __init__(self):
        self._date      = []
        self._precip    = []
        self._moist_2   = []

    def add_day(self, _index, _date, _precip, _moist_2):
        if (_index +1 >= len(self._date) ):
            self._date.append( [_date] )
            self._precip.append( [_precip] )
            self._moist_2.append( [_moist_2] )
    
        else:
            self._date[_index].append( _date )
            self._precip[_index].append( _precip )
            self._moist_2[_index].append( _moist_2 )
    
    def get_date(self):
        return np.array(self._date)

    def get_precip(self):
        _tmp = self.norm(self._precip)
        return _tmp
    
    def get_moist_2(self):
        _tmp = self.norm(self._moist_2)
        return _tmp
    def get_moist_2_labels(self):
        return np.array(self._moist_2).reshape(-1, 1)

    def norm(self, x):
        _tmp = np.array(x).reshape(-1, 1)
        
        _res = []
        for i in _tmp:
            _res.append(_tmp)
        return np.array(_res)


    def get_data(self, _ratio):

        # How many days need for prediction 
        _pre = 3

        _tx = [ [], [] ]
        _ty = [ [] ]
        _vx = [ [], [] ]
        _vy = [ [] ]
        
        # Create a set for each station
        for _in in range(0, len(self._date)):

            """
                We split the data into two parts, based on the ratio input given
                in the function. The _ti variable is how many of the data values 
                in each station will be used as testing while the vi variable
                represents the testing values.
            """
            _ti = int( len(self._date[_in]) * _ratio )
            _vi = int( len(self._date[_in]) * (1 - _ratio) )

            # We always need 3 days
            while (_ti % _pre != 0 ): _ti -= 1
            while (_vi % _pre != 0 ): _vi -= 1

            # Create testing set
            for i in range( 0, int( (_ti / _pre) - _pre ) ):
                _xb1 = []
                _xb2 = []
                _yb  = []

                # Starting point
                for k in range(i*_pre, i*_pre + _pre):
                    _xb1.append( [self._moist_2[_in][k]] )
                    _xb2.append( [self._precip[_in][k]] )
                    _yb.append( [self._moist_2[_in][k +_pre]] )

                _tx[0].append(_xb1)
                _tx[1].append(_xb2)
                _ty[0].append(_yb) # Validate on the next day moisture

            # Create validation set
            for i in range( _ti +1, int( _ti + (_vi / _pre) - _pre ) ):
                _xb1 = []
                _xb2 = []
                _yb  = []

                # Starting point
                for k in range(i, i + _pre):
                    _xb1.append( [self._moist_2[_in][k]] )
                    _xb2.append( [self._precip[_in][k]] )
                    _yb.append( [self._moist_2[_in][k +_pre]] )
                    
                _vx[0].append(_xb1)
                _vx[1].append(_xb2)
                _vy[0].append(_yb) 

       
        # Declare values
        _train = {
            'x':  _tx,
            'y': _ty
        }

        _test = {
            'x': _vx,
            'y': _vy
        }
        
        return {
            'train': _train,
            'test': _test
        }
