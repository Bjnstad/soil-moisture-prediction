import json

f= open("reults.mm","w+")
with open('data.json') as _file:
    _data = json.load(_file)

    for _e in _data[1]:
        
        # Start with station id
        f.write("$" + _e[0] + ':')

        # Loop data measurements
        for _m in _e[1]:
            f.write(str( _m[0] ) + '%' + str( _m[1] ) + ',')
    
        
