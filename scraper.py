import json
import math
import pandas as pd
import load
import requests

_s = load.scan()

i = 0
for station in _s:
    print(str(i/len(_s)*100) + str("%"))
    urlstring = "https://wcc.sc.egov.usda.gov/reportGenerator/view_csv/customMultipleStationReport,metric/daily/start_of_period/id="
    urlend = "%20AND%20network=%22SCAN%22%20AND%20outServiceDate=%222100-01-01%22%7Cname/1990-01-01,2019-01-01/stationId,name,PRCP::value,TAVG::value,TMAX::value,TMIN::value,SMS:-2:value:hourly%20MEAN,SMS:-4:value:hourly%20MEAN,SMS:-8:value:hourly%20MEAN,SMS:-20:value:hourly%20MEAN,SMS:-40:value:hourly%20MEAN,STO:-2:value:hourly%20MEAN,STO:-4:value:hourly%20MEAN,STO:-8:value:hourly%20MEAN,STO:-20:value:hourly%20MEAN,STO:-40:value:hourly%20MEAN,RHUM::value:hourly%20MEAN,LRADT::value?fitToScreen=false&sortBy=3%3A-1"
    urlstring += "%22" + str(station._id) + "%22"
    urlstring += urlend

    df = pd.read_csv(urlstring, comment='#', error_bad_lines=False, delimiter=",")

    df.to_csv("data2/" + str(station._id) + ".csv")
    i+=1
exit(0)













pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

counter = 0
empty = []
stations = []
days = []
len(_s)
start = 0
max = 1
index = 0
currentStation = 0


def post_station():
    urlstring = "https://wcc.sc.egov.usda.gov/reportGenerator/view_csv/customMultipleStationReport,metric/daily/start_of_period/id="
    urlend = "%20AND%20network=%22SCAN%22%20AND%20outServiceDate=%222100-01-01%22%7Cname/2009-01-01,2019-01-01/stationId,name,PRCP::value,TAVG::value,TMAX::value,TMIN::value,SMS:-2:value:hourly%20MEAN,SMS:-4:value:hourly%20MEAN,SMS:-8:value:hourly%20MEAN,SMS:-20:value:hourly%20MEAN,SMS:-40:value:hourly%20MEAN,STO:-2:value:hourly%20MEAN,STO:-4:value:hourly%20MEAN,STO:-8:value:hourly%20MEAN,STO:-20:value:hourly%20MEAN,STO:-40:value:hourly%20MEAN,RHUM::value:hourly%20MEAN,LRADT::value?fitToScreen=false&sortBy=3%3A-1"
    for index, station in enumerate(stations):
        print(station)
        if index in range(0, len(stations)-1):
            urlstring += "%22" + str(station) + "%22,"
        else:
            urlstring += "%22" + str(station) + "%22"
    urlstring += urlend
    print("\n" + urlstring + "\n")

    df = pd.read_csv(urlstring, comment='#', error_bad_lines=False, delimiter=",")

    for index, row in df.iterrows():
        stationId = int(row['Station Id'])
        if ( math.isnan(stationId) ): stationId = -1

        precip = float(row['Precipitation Increment (mm)'])
        if ( math.isnan(precip) ): precip = -1

        moisture = float(row['Soil Moisture Percent -2in (pct) Mean of Hourly Values'])
        if ( math.isnan(moisture) ): moisture = -1

        days.append({
            "stationId": stationId,
            "date": row['Date'] + " 12:00:00",
            "precip": precip,
            "moisture": moisture
        })
    r = requests.post(
        "http://192.168.10.183:8080/day",
        data=json.dumps(days),
        headers={'Content-type': 'application/json'}
    )
    print(r.status_code, r.reason)


while currentStation < len(_s):
    for i in _s:
        counter += 1
        print("Adding station: " + str(i._id) + " to list stations.", end='')
        print("\n")
        print("Currently Fetching data for station with id: "+ str(i._id), end='')
        print("\n")

        stations.append(int(i._id))
        if counter < 190:
            print("Station with id: " + str(stations) + " has already been processed")
        else:
            print("Posting station with id: " + str(stations))
            post_station()

        print("\n")
        print("Data fetched successfully: ")
        print("Station count = " + str(counter))
        currentStation += max
        index += 1
        stations.clear()


print("\n")
print(stations)
print(len(stations)-1)

"""""
    stations with only nan values: 2009, 2012, 2017, 2013, 2005
"""""
