import csv, re

def moisture(stations):
    with open('stations.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        first = True
        for row in csv_reader:
            if first:
                first = False
                continue


            if float(row[3]) < -126:
                continue
        
            length = len(row[0])

            try:
                ID = int(row[0][-5:-1])
                name = row[0][:-6]
            except:
                ID = int(row[0][-4:-1])
                name = row[0][:-5]
            station = {
                "id": ID,
                "name": name,
                "startDate": row[1],
                "lat": float(row[2]),
                "lng": float(row[3]),
            }
            stations.append(station)

def weather(stations):
    with open('weather_stations.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        first = True
        for row in csv_reader:
            station = {
                "id": row[0],
                "lat": float( o_n(row[2]) ),
                "lng": float( o_n(row[3]) )
            }
            stations.append(station)

def o_n(_str):
    if _str == '' or _str == '#FIELD!': return 0
    return _str.replace(' ', '')
