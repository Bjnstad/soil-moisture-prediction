from datetime import datetime
import urllib.request, json

class Coord():
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

class Station():
    def __init__( self, _id: str, _coord: Coord ):
        self._id = _id
        self._coord = _coord
        self._values = []

    """
        Validates dates and fill in empty rows
        # TODO: need fill
    """
    def validateValues():
        pass


class Weather(Station):
    def __init__( self, _id: str, _coord: Coord ):
        super().__init__(_id, _coord)
        self._url = "http://3.122.118.248/get.php?station=" + _id
        self._value = [] 
    """
        Load raw data from database
    """
    def loadData(self):
        self._value.append(0)
        """
        try:
            with urllib.request.urlopen(self._url, timeout=120) as url:
                data = json.loads(url.read().decode('utf-8'))
                try:
                    for station in data:
                        self._values.append([
                            datetime.strptime( station['date'] ).
                            station['value']
                        ])
                except:
                    return False
            self.validateValues();
            return res          
        except urllib.error.URLError as e:
            print('--- failour ---')
            print(e.reason)
            return "failed"
        except:
            print("Some error");
        """


class SCAN(Station):
    def __init__( self, _id: str, _coord: Coord ):
        super().__init__(_id, _coord)
