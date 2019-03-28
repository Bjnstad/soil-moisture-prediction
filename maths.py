def validate(data, start, end):
    total_days = (start - end).days
    current = start

    for _e in data:
        _t = _e[0] # Epoch timestamp
        _v = _e[1] # Value

        # Convert epoch to datetime
        _date = datetime.datetime.fromtimestamp(float(_t)/1000.)
        
        # If not a match we are missing data and will use interpolation to populate data
        if _date.day != current.day:
             

        # Interate data with 1 day
        current = current + datetime.timedelta(days=1)




def interpolation(values, last, lastest):
    :
