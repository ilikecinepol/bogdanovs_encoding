import time as tm
from collections import OrderedDict

# Получение unix-времени и времени в формате гггг-мм-дд чч:мм:сс
unix_time = int(tm.time())
print(unix_time)
str_date = tm.strftime('%Y-%m-%d %H:%M:%S', tm.localtime(unix_time))
# print(type(unix_time))
print(str_date)
# Получение времени в формате гггг-мм-дд чч:мм:сс из unix
t = tm.strptime(str_date, '%Y-%m-%d %H:%M:%S')
# print(int(tm.mktime(t)))
key_list = []
key = "".join(OrderedDict.fromkeys(str(unix_time)))

print(key)

# Читаем файл с секретным сообщением
message = open("message.txt")
mes = message.read()
# message.close()
mes = mes.split()
print(mes)
text = open('text.txt')
message.close()

# Читаем файл с бессмысленным текстом-водой
content = text.read()
water = content.split()
print(water)
water.copy()
res_text = []

sep = ' '
# print(transmit)
ending = f'\n Сообщение отправлено: {str_date}'


def encoding(key, water, mes):
    for i in key:
        l = key.index(i)
        i = int(i)

        try:
            for k in range(len(water)):
                k = int(k)
                if i == k:
                    # print(mes[l])
                    water[k] = mes[l]
                    k = k + i


        except IndexError:
            break

    print(water)
    for i in range(len(water)):
        res_text.append(water[i])
        res_text.append(sep)
    print(f'Итоговое сообщение: {res_text}')

    with open('result.txt', 'w') as file:
        file.writelines(res_text)
        file.writelines(ending)

#generate_key(key)
#print(generate_key(key))
print(key)
#encoding(key, water, mes)
