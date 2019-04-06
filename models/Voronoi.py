from scipy.spatial import Voronoi as V
from shapely.geometry.polygon import Polygon
from shapely.geometry.point import Point
from models.Station import SCAN, Weather
import numpy as np
import math


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
                # print(_polygon)
                if _polygon.contains( _point ):  # if weather station is inside cell
                    _cell._weather_stations.append( _station )  # Add weather station to cell

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
        if _weather_stations is None:
            _weather_stations = [Weather]
        self._scan = _scan
        self._weather_stations = _weather_stations

        for station in self._weather_stations:
            station.loadData()

        _delta = 3650

        # Loop each day and add weighted average
        _weighted_average = []
        for _index in range(0, _delta):
            _v = self.calculate_weighted_average(_index)
            print(_v)
            _weighted_average.append(_v)
        
        # TODO: Store values in databasee

    """
        Should download raw weather data and create an weighted average  
    """


    """
        Calculate weighted average for one day.

        day : int 
            Is the index of the current day
    """

    # TODO: Skip days with null value in measeure data 
    def calculate_weighted_average(self, day):
        _sum = 0  # Total sum of all stations
        _distance = 0  # Distance from weather_station to scan_station station
        _all_distances = []
        _max_distance = 10
        _station_weight = 0
        _total_weights = 0

        for station in self._weather_stations:
            # TODO: Add value times distance from SCAN station to _sum
            scan_lat = self._scan._coord.lat
            scan_lng = self._scan._coord.lng
            station_lat = station._coord.lat
            station_lng = station._coord.lng
            _distance = math.sqrt((scan_lat - scan_lng) ** 2 + (station_lat - station_lng) ** 2)
            
            print(_distance)
            # TODO: we need to find weights
            if _distance < _max_distance:
                weight = _distance*(-(1/_max_distance))+1
                _sum += station._value[day]*weight
                _total_weights += 1

        if _total_weights > 0:
            return _sum / _total_weights

        return 0
