class Coord():
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

class Station():
    def __init__( self, _id: str, _coord: Coord ):
        self._id = _id
        self._coord = _coord

class Weather(Station):
    def __init__( self, _id: str, _coord: Coord ):
        super().__init__(_id, _coord)
        self._values = []
   
   
   """
        Load raw data from database
    """
    def loadData(self):
        try:
            with urllib.request.urlopen(url5, timeout=120) as url2:
                data = json.loads(url2.read().decode('utf-8'))
                try:
                    days = data['history']['days']
                    for day in days:
                        _date = datetime.datetime.fromtimestamp( day['summary']['date']['epoch'] ).strftime('%Y-%m-%d')
                        res.append([  _date, day['summary']['precip'] ])
                except:
                    return False
            return res          
        except urllib.error.URLError as e:
            print('--- failour ---')
            print(e.reason)
            return "failed"



class SCAN(Station):
    def __init__( self, _id: str, _coord: Coord ):
        super().__init__(_id, _coord)
