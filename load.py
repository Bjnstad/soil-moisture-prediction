from models.Station import SCAN, Weather, Coord
import csv, re

def scan():
    stations = []
    with open('scan_stations.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        first = True
        for row in csv_reader:
            # Skip first row
            if first:
                first = False
                continue
            
            # Removed if in Alaska
            if float(row[3]) < -126:
                continue
            
            try:
                ID = int(row[0][-5:-1])
                name = row[0][:-6]
            except:
                ID = int(row[0][-4:-1])
                name = row[0][:-5]
            
            _coord = Coord(float(row[2]), float(row[3]))
            stations.append( SCAN(ID, _coord) )
    return stations

def weather():
    stations = []
    with open('weather_stations.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        first = True
        for row in csv_reader:
            _coord = Coord(float( o_n(row[2]) ), float( o_n(row[2])))
            stations.append( Weather( row[0], _coord) )
    return stations

def o_n(_str):
    if _str == '' or _str == '#FIELD!': return 0
    return _str.replace(' ', '')
