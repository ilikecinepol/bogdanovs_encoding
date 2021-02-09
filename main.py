import time as tm
from collections import OrderedDict

# Получение unix-времени и времени в формате гггг-мм-дд чч:мм:сс
unix_time = int(tm.time())
print(unix_time)
str_date = tm.strftime('%Y-%m-%d %H:%M:%S', tm.localtime(unix_time))
# print(type(unix_time))
# print(str_date)
# Получение времени в формате гггг-мм-дд чч:мм:сс из unix
t = tm.strptime(str_date, '%Y-%m-%d %H:%M:%S')
# print(int(tm.mktime(t)))
key_list = []
key = "".join(OrderedDict.fromkeys(str(unix_time)))






# Читаем файл с секретным сообщением
message = open("message.txt")
mes = message.read()
# message.close()
mes = mes.split()
print(mes)
text = open('text.txt')

# Читаем файл с бессмысленным текстом-водой
content = text.read()
water = content.split()
print(water)
water.copy()
res_text = []

print(f'Key: {key}')
sep = ' '
# print(transmit)
ending = f'\n Сообщение отправлено: {str_date}'

'''
1. Проходим по всем элементам сообщения       x
2. Берём элемент сообщения - mes[x]
3. Находим элемент ключа с номером х - key[x] 

5. Находим элемент текста с номером  - water[int(key[x])]  
6. Вставляем элемент сообщения с номером х в текст по номеру     water[int(key[x])] = mes[x] 
7. Прибавляем key[x]   к номеру элемента текста     x =x+key[x]  

номер элемента ключа - x
элемент ключа - key[x]
элемент сообщения - mes[x]
номер элемента сообщения - water[int(key[x])]

'''
def encoding(key, water, mes):
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

    print(water)
    for i in range(len(water)):
        res_text.append(water[i])
        res_text.append(sep)
    print(f'Итоговое сообщение: {res_text}')

    with open('result.txt', 'w') as file:
        file.writelines(res_text)
        file.writelines(ending)
        #file.writelines(key)

encoding(key, water, mes)
