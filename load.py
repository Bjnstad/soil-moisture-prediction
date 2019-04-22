from models.Station import SCAN, Weather, Coord
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
    
    with open('2057.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first = True
        
        _days = Days.Days()
        
        i = 0
        for row in csv_reader:
            # Skip first row
            if first:
                first = False
                continue
            """ 
            _date                   = row[0],
            _id                     = row[1],
            _name                   = row[2],
            _p_increment            = row[3], # Inches
            _air_temp_average       = row[4], # Fahrenheit
            _air_temp_max           = row[5], # Fahrenheit
            _air_temp_min           = row[6], # Fahrenheit
            _moist_2                = row[7],
            _moist_4                = row[8],
            _moist_8                = row[9],
            _moist_20               = row[10],
            _moist_40               = row[11],
            _temp_2                 = row[12],
            _temp_4                 = row[13],
            _temp_8                 = row[14],
            _temp_20                = row[15],
            _temp_40                = row[16],
            _humid                  = row[17],
            _precip_accumulation    = row[19]
            """
            
            _days.add_day(i, float( o_n(row[3]) ), float( o_n(row[7]) ))
            i += 1

        return _days
