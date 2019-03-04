from tkinter import*
from tkinter import messagebox

#функції
def choose(event):
    r1=res1.get()
    r2=res2.get()
    r3=res3.get()
    r4=res4.get()
    r5=res5.get()
    answer = ''
    if r1 == 1:
        answer += ' Главный босс этой качалки'
    if r2 == 1:
        answer += '  Якименко бутилочнік'
    if r3 == 1:
        answer += ' Блендер'
    if r4 == 1:
        answer += ' Інопланітянин(Влад)'
    if r5 == 1:
        answer += ' Чега'

    messagebox.showinfo('Слабаки', 'Рішили зайнятися ракетами' +answer)
root = Tk()
root.title('Вибір кольору')
root.geometry('300x200')

#Елементи
res1 = IntVar()
res2 = IntVar()
res3 = IntVar()
res4 = IntVar()
res5 = IntVar()

q = Label(root, text="Хто не дружить з гітом?")
v1 = Checkbutton(root, text="Главный босс этой качалки", variable=res1)
v2 = Checkbutton(root, text="Якименко бутилочнік", variable=res2)
v3 = Checkbutton(root, text="Блендер", variable=res3)
v4 = Checkbutton(root, text="Інопланітянин(Влад)", variable=res4)
v5 = Checkbutton(root, text="Чега", variable=res5)
choosebtn = Button(root, text='Ну попробуй')

#Розташування
q.pack()
v1.pack()
v2.pack()
v3.pack()
v4.pack()
v5.pack()
choosebtn.pack()
choosebtn.bind('<Button-1>', choose)
#Подія

root.mainloop()

