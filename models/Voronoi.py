from scipy.spatial import Voronoi as V
from shapely.geometry.polygon import Polygon
from shapely.geometry.point import Point
from models.Station import SCAN, Weather

class Voronoi():
    """
    This create a Voronoi map of Scan and weather stations.
    ...

    Attributes
    ----------
    _scan : list[SCAN]
        List of scan stations
    _weather : list[Weather]
        List of weather stations
        _
    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    _cells = []

    def __init__(self, _scans, _weather_stations):
        self._scan_stations = _scans
        self._weather_stations = _weather_stations
        self.map_cells()


    def map_cells(self):
        # Calculate Voronoi
        _voronoi = V(self.get_scan_coordinates())
        # Loop region
        _ri = 0 # Dont increment on empty region 
        for i, reg in enumerate(_voronoi.regions):
            if len(reg) == 0: continue # There will always be one empty region
            
            # Create cell
            _cell = Cell(self._scan_stations[_ri])

            # Get all vertices for region
            _vertices = []
            for vertex in reg:
                _p = _voronoi.vertices[vertex]
                _vertices.append((_p[1], _p[0]))

            # Polygon of Voronoi cell 
            _polygon = Polygon(_vertices)

            # Loop weather stations and add them to cell
            for _station in self._weather_stations:
                _point = Point( _station._coord.lat, _station._coord.lng )
                if _polygon.contains( _point ): # if weather station is inside cell
                    _cell._weather_stations.append( _station ) # Add weather station to cell

            # Add cell to list
            self._cells.append( _cell ) 
            _ri += 1
    
    
    def get_scan_coordinates(self):
        _coords = []
        for _station in self._scan_stations:
            _coords.append([
                float(_station._coord.lng),
                float(_station._coord.lat)
            ])
        return _coords


class Cell():
    """
    This is an cell in a Vorronoi Tessolation map.
    ...

    Attributes
    ----------
    _soil : Soil
        SCAN station that is relevant for the 
    """

    def __init__(self, _scan: SCAN, _weather_stations=[]):
        self._scan = _scan
        self._weather_stations = _weather_stations
