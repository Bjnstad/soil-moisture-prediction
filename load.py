from models.Station import SCAN, Weather, Coord
import urllib.request, json
import csv, re
import Days

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
            _coord = Coord(float( o_n(row[2]) ), float( o_n(row[3])))
            stations.append( Weather( row[0], _coord) )
    return stations

def o_n(_str):
    if _str == '' or _str == '#FIELD!': return 0
    return _str.replace(' ', '')



def new():
    _days = Days.Days()

    with urllib.request.urlopen("http://localhost:8080/station") as url:
        data = json.loads(url.read().decode())
        
        i = 0
        for station in data:
            with urllib.request.urlopen("http://localhost:8080/day/" + str(station['id'])) as url2:
                data2 = json.loads(url2.read().decode())
                for day in data2:
                    _days.add_day(i, day['date'], day['precip'], day['moisture'])
            i += 1;
    return _days
