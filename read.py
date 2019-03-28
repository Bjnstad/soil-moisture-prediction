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
            "lat": row[2],
            "lng": row[3],
        }
        moisture_stations.append(station)

# Read weather stations
with open('weather_stations.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    first = True
    for row in csv_reader:
        station = {
            "id": row[0],
            "lat": row[1],
            "lng": row[2]
        }
        weather_stations.append(station) 
        
