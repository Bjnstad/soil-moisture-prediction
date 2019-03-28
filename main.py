#!/usr/local/bin/python3.7
import datetime, json
from dateutil.parser import parse
import requests
import load, fetch

# Time period
start_date  = "2009-03-03"
end_date    = "2019-03-03"

# Allowed http errors
allowed_errors = 10

# What moisture sensor data to collect
data_sources = [
    "moisture_2",
    "moisture_4",
    "moisture_8",
    "moisture_20",
    "moisture_40"
]

# Delacare station variables
moisture_stations = []
weather_stations = []

# Load stations from static csv
load.moisture(moisture_stations)
load.weather(weather_stations)

# Parse dates
start = parse(start_date)
end = parse(end_date)

# Number of days
days = (end - start).days

# Load data to
datas = []

c = 0
# Fetch data for each moisture station
"""
for station in moisture_stations:
    print(str(c / ( len(moisture_stations) + len(weather_stations) ) * 100) + '%') 
    data = fetch_moisture_data( station['id'])  
    if(data == False): continue 
    for source in data_sources: 
        big[0].append( str(station['id']) + '#' + source )
    for i in range(1, len(data[0])):
        for k in range(0, len(data_sources)): 
            tmp = data[k+1][i]
            big[i].append(tmp)
    c += 1
"""
for station in weather_stations:
    current = start
    tmp = []

    while ( (end - current).days > 0):
        diff = (end - current).days
        if (diff > 200):
            diff = 200 
        # print(str(diff) + ' / ' + str(days) )
        # Count failed requests
        json_failed = 0
        http_failed = 0
        while True:
            data = fetch.weather( str(station['id']), current, current + datetime.timedelta(days = diff -1))
            
            # Request error
            if (data == "failed"): 
                if (http_failed > allowed_errors):
                    break    
                else:
                    http_failed += 1
                    continue

            # Response error
            if (data == False): 
                if (json_failed > allowed_errors):
                    break    
                else:
                    json_failed += 1
                    continue
            
            for i in range(1, len(data)):
                tmp.append(data[i -1])
            break
        if(len(tmp) > 0): 
            current = current + datetime.timedelta(days = diff)
        else:
            break
    c += 1 
   
   
   
    if( len(tmp) > 0 ): 
        url = "http://localhost/post.php"
        print( len(tmp) )
        data = [
            str(station['id']),
            tmp
        ]
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)
       
        """ 
        datas.append([
            str(station['id']),
            tmp
        ])

        # Write json to file
        f = open('data.json', 'r+')
        f.truncate(0)
        
        f.write( json.dumps( [str( round(c / len(weather_stations)  * 100, 2) ) + '%    -   ' + str(len(datas)) + '/' + str(days) , datas], ensure_ascii=False))"""
        #      f.close()
        print(str( round(c / len(weather_stations)  * 100, 2) ) + '%    -   ' + str(len(datas)) + '/' + str(days) ) 
    
    else:
        print(str( round(c / len(weather_stations)  * 100, 2) ) + '%    -   failed') 


# Create spreadsheet
# my_df = pd.DataFrame(big)
# my_df.to_csv('sheet.csv', index=False, header=False, sep=';')
# print( big )

# Plot data frames
"""
# Get soil data
soil_data = fetch_moisture_data()
weather_data = fetch_weather_data()


# Plot data
#plt.plot(data[0], data[6])
fig, ax1 = plt.subplots()
ax1.plot(soil_data[0], soil_data[6], 'b-')
ax1.set_xlabel('date in Epoch')
ax1.set_ylabel('Soil moisture', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(soil_data[0], weather_data, 'r.')
ax2.set_ylabel('Precip', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()
plt.show()


#3plt.plot(soil_data[0], weather_data)
#plt.show()
"""
