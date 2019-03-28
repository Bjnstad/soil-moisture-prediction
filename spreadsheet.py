def create(data, start, end):
    delta = end - start
    data = [delta] + data
    
    for i in range(0, delta.days):
        big.append([])

    k = 1
    while delta.days > 0:
        big[k].append(start_date)
        
        k += 1
        start_date += datetime.timedelta(days=1)
        delta = end_date - start_date

