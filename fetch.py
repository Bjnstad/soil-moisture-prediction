import urllib.request, json
import datetime

weather_api = "https://api-ak.wunderground.com/api/d8585d80376a429e/history_"
moisture_api = "https://www.drought.gov/drought/soil_moisture/scan/"

def moisture(station_id):
    with urllib.request.urlopen( moisture_link(station_id) ) as url:
        data = json.loads(url.read().decode())
        return serilize_data(data)


def weather(station_name, start, end):
    current = start

    res = []
    url4 = weather_api + start.strftime('%Y%m%d') + end.strftime('%Y%m%d') + '/lang:EN/units:english/bestfct:1/v:2.0/q/' + station_name +'.json'
    
    url5 = url4.encode('ascii', 'ignore').decode('ascii')
    try:
        with urllib.request.urlopen(url5, timeout=120) as url2:
            data = json.loads(url2.read().decode('utf-8'))
            try:
                days = data['history']['days']
                for day in days:
                    _date = datetime.datetime.fromtimestamp( day['summary']['date']['epoch'] ).strftime('%Y-%m-%d')
                    res.append([  _date, day['summary']['precip'] ])
            except:
                return False
        return res          
    except urllib.error.URLError as e:
        print('--- failour ---')
        print(e.reason)
        return "failed"


def moisture_link(station_id):
    res = moisture_api
    res += str(station_id) + '/'

    # Add selected sources
    first = True
    for source in data_sources:
        if not first: res += ','
        first = False
        res += source
    
    res += '/' + time_start + '/' + time_end
    return res
