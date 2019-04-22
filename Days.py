class Days:

    def __init__(self):
        self._date      = []
        self._precip    = []
        self._moist_2   = []

    def add_day(self, _date, _precip, _moist_2):
        self._date.append( _date )
        self._precip.append( _precip )
        self._moist_2.append( _moist_2 )
    
    # TODO: Add normalisation?
    def get_date(self):
        return self._date

    # TODO: Add normalisation?
    def get_precip(self):
        return self._precip
    
    # TODO: Add normalisation?
    def get_moist_2(self):
        return self._moist_2
