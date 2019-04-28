import load


_s = load.scan()

start = 0
max = 5
index = 0
for i in _s:
    if (index < start):
        index+=1
        continue;
    if (max + start == index): break
    print(str(i._id) + ',', end='')
    index += 1