from scipy.spatial import Voronoi as V
from shapely.geometry.polygon import Polygon
from shapely.geometry.point import Point
from Station import SCAN, Weather
from dateutil.parser import parse
import geopy.distance
import numpy as np
import math


class Voronoi:
    def __init__(self, _scans, _weather_stations):
        self._scan_stations = _scans
        self._weather_stations = _weather_stations
        self._cells = []
        self.map_cells()

    def map_cells(self):
        # Calculate Voronoi
        _voronoi = V(self.get_scan_coordinates())
        # Loop region
        _ri = 0  # Dont increment on empty region
        for i, reg in enumerate(_voronoi.regions):
            if len(reg) == 0:
                continue  # There will always be one empty region
            
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
                if _polygon.contains( _point ):  # if weather station is inside cell
                    _cell._weather_stations.append( _station )  # Add weather station to cell

            # Add cell to list
            self._cells.append( _cell )
            _cell.calculate()
            _ri += 1

    def get_scan_coordinates(self):
        _coords = []
        for _station in self._scan_stations:
            _coords.append([
                float(_station._coord.lng),
                float(_station._coord.lat)
            ])
        return _coords


class Cell:
    def __init__(self, _scan: SCAN, _weather_stations=[]):
        if _weather_stations is None:
            _weather_stations = [Weather]
        self._scan = _scan
        print("new cell")
        self._weather_stations = _weather_stations

    def calculate(self):
        for station in self._weather_stations:
            station.loadValues()
            station.validateValues( parse("2009-03-03"), parse("2019-03-03") )

        _delta = (parse("2009-03-03") - parse("2019-03-03")).days

        print('----- ' + station._id + '-----')

        # Loop each day and add weighted average
        _weighted_average = []
        for _index in range(0, _delta):
            _v = self.calculate_weighted_average(_index)
            _weighted_average.append(_v)
            if _v > -1:
                print(_v)
        # TODO: Store values in databasee

    # TODO: Skip days with null value in measeure data 
    def calculate_weighted_average(self, day):
        _sum = 0  # Total sum of all stations
        _total_weights = 0

        for station in self._weather_stations:
            scan_coords = [self._scan._coord.lat, self._scan._coord.lng]
            station_coords = [station._coord.lat, station._coord.lng]
            _distance = geopy.distance.distance(scan_coords, station_coords).km

            weight = 1/_distance
            # _sum += station._value[day]*weight
            _total_weights += weight

        if _total_weights > 0:
            return _sum / _total_weights

        return -1  # No value found
