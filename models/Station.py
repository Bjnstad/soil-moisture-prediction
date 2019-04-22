from datetime import datetime
import urllib.request, json, datetime, datetime

class Coord():
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

class Station():
    def __init__( self, _id: str, _coord: Coord ):
        self._id = _id
        self._coord = _coord
        self._values = []

    def validateValues(self, start, end):
        _delta = (end - start).days
        _current = start
        _i = 0
        while _i < _delta:
            if _i >= len(self._values):
                _current = _current + datetime.timedelta(days=1)
                _i += 1
                self._values.append(None)
                continue


            # print( str(_i) + " - " + str(len(self._values)) ) 
            _value = self._values[_i]
            if _value == None:
                self._values.append(None)
            else:
                self._values.insert(_i, None)    

            _current = _current + datetime.timedelta(days=1)
            _i += 1

        print(_i)

class Weather(Station):
    def __init__( self, _id: str, _coord: Coord ):
        super().__init__(_id, _coord)
        self._url = "http://3.122.118.248/get.php?station=" + _id

    def loadValues(self):
        try:
            with urllib.request.urlopen(self._url, timeout=120) as url:
                data = json.loads(url.read().decode('utf-8'))
                # Parse data
                for day in data:
                    self._values.append([
                        datetime.datetime.strptime( day['date'], "%Y-%m-%d %H:%M:%S" ),
                         day['value']
                    ])
        
        except urllib.error.URLError as e:
            print('--- failour ---')
            print(e.reason)
            return "failed"
        except Exception as e:
            print(e)

class SCAN(Station):
    def __init__( self, _id: str, _coord: Coord ):
        super().__init__(_id, _coord)
