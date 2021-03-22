from tkinter import *
from tkinter import ttk, messagebox
import time as tm
from collections import OrderedDict
number_of_words = 64
def picture():
    # Читаем файл с секретным сообщением
    message = open("result.txt")
    mes = message.read()
    message.close()
    mes = mes.split()
    #mes = mes[:-4]
    print('FDSFAFD',len(mes))

    tk = Tk()
    tk.title("Поздравляем с Днём ВМФ!")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 0)
    canvas = Canvas(tk, width=1200, height=686, highlightthickness=0)

    # tk.update()
    canvas_height = 1200
    canvas_width = 686
    bg = PhotoImage(file="pictures/bg2.gif")
    w = bg.width()
    h = bg.height()

    for x in range(0, 5):
        for y in range(0, 5):
            canvas.create_image(x * w, y * h, image=bg, anchor='nw')
            sprites = []
            running = True

    def figure1():
        frames = [Frame(tk) for x in range(10)]
        y = 100
        k = 0
        labels = [x for x in range(100)]
        for i in range(len(frames)):
            frames[i].place(x=575, y=y) #575-1075
            y += 25
            for j in range(7):
                l = Label(frames[i],text = mes[k], font=('Times New Roman','15'), fg='#0F0', bg='white')
                #labels.append(l)
                l.pack(side=LEFT)
                k += 1

            k += 1
        print(labels)
    def figure2():

        frames = [Frame(tk) for x in range(number_of_words)]
        y = 100
        x = 575
        k = 0
        labels = [x for x in range(number_of_words)]
        for i in range(len(frames)):
            frames[i].place(x=x, y=y) #x=[575-1075]
            x += 100
            size = 100/len(mes[k])
            if size > 50:
                size = 50
            print(size)
            if i == 0:
                anc = 'nw'
            elif i == 4:
                anc = 'ne'
            elif i < 5 or i > 17:
                anc = 'n'
            elif i % 4 == 0:
                anc = 'e'
            elif i>27:
                anc = 's'
            else:
                anc = 'center'
            l = Label(frames[i],text = mes[k], font=('Times New Roman',str(round(size))), fg='blue', bg='white', justify='center', anchor=anc)
            sizes = []
            sizes.append(size)
            #labels.append(l)
            l.pack(side=LEFT)
            #k += 1
            if (i+1) % 5 == 0 and i != 0:
                y += 75
                x = 575
            k += 1
            if y > 600:
                break
        print(labels)

    def figure3():


        frames = [Frame(tk) for x in range(number_of_words)]
        y = 100
        x = 575
        k = 0
        labels = [x for x in range(number_of_words)]
        for i in range(len(frames)):
            frames[i].place(x=x, y=y) #x=[575-1075]
            x += 100
            size = 100/len(mes[k])
            if size > 50:
                size = 50
            print(size)
            if i == 0:
                anc = 'nw'
            elif i == 4:
                anc = 'ne'
            elif i < 5 or i > 17:
                anc = 'n'
            elif i % 4 == 0:
                anc = 'e'
            elif i>27:
                anc = 's'
            else:
                anc = 'center'
            l = Label(frames[i],text = mes[k], font=('Times New Roman',str(round(size))), fg='blue', bg='white', justify='center', anchor=anc)
            sizes = []
            sizes.append(size)
            #labels.append(l)
            l.pack(side=LEFT)
            #k += 1
            if (i+1) % 5 == 0 and i != 0:
                y += 75
                x = 575
            k += 1
            if y > 600:
                break
        print(labels)

    figure3()
    canvas.pack()

    mainloop()