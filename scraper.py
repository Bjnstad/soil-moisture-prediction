import pandas as pd
import load

_s = load.scan()
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


stations = []
start = 0
max = 1
index = 0
for i in _s:
    if (index < start):
        index+=1
        continue;
    if (max + start == index): break
    print(str(i._id) + ',', end='')
    stations.append(int(i._id))
    index += 1
print("\n")
print(stations)
print(len(stations)-1)

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
print(df)