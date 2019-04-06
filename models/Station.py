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

    """
        Load raw data from database
    """
    def loadData(self):
        self._values = []


class SCAN(Station):
    def __init__( self, _id: str, _coord: Coord ):
        super().__init__(_id, _coord)
