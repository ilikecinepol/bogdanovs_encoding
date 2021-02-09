import time as tm

from collections import OrderedDict


nums = '0123456789'

data = []
with open('result.txt', 'r') as file:
    for line in file:
        data.append(line)
print(data)
def decode_key(data):
    full_key = str(data)
    print(type(full_key))
    str_key = full_key[23:42]
    print(str_key)
    t = tm.strptime(str_key, '%Y-%m-%d %H:%M:%S')
    print(t)
    unix_time = tm.mktime(t)
    key = "".join(OrderedDict.fromkeys(str(unix_time)))
    print(key)

def decode_data():
    #y = key[x]
    z = 0               #для индекса
    for x in range(len(mes)):
        try:
            #print(mes[x])
            #print(key[x])
            #print(water[int(key[x])])

            y = int(key[x - 1]) + int(key[x])
            water[y] = mes[z]
            #y = y + int(key[x+1])
            #y += int(key[x+1])
            z+=1
        except IndexError:
            break

decode_key(data[1])