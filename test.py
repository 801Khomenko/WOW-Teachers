from tkinter import *

def fact(event):
    n = int(input1.get())
    res = 1
    for i in range(1, n + 1):
        res *= i
    input1.delete(0)
    input1.insert(0, res)

def One(even):
    input1.insert(END, 1)

def Two(even):
    input1.insert(END, 2)

def Three(even):
    input1.insert(END, 3)

def Four(even):
    input1.insert(END, 4)

def Five(even):
    input1.insert(END, 5)

def Six(even):
    input1.insert(END, 6)

def Seven(even):
    input1.insert(END, 7)

def Eight(even):
    input1.insert(END, 8)

def Nine(even):
    input1.insert(END, 9)

def Zero(even):
    input1.insert(END, 0)

root = Tk()
#root.geometry('200x200')
root.title('Факторіал числа')

input1 = Entry(root, bd='0')

button1 = Button(root, text='n!', width=5, height=2, bg='#ffffff')
input1.grid(row=1, column=1, columnspan=5)
button1.grid(row=2, column=1)

one = Button(root, text='1', width=5, height=2 )
two = Button(root, text='2', width=5, height=2 )
three = Button(root, text='3', width=5, height=2 )
four = Button(root, text='4', width=5, height=2 )
five = Button(root, text='5', width=5, height=2 )
six = Button(root, text='6', width=5, height=2 )
seven = Button(root, text='7', width=5, height=2 )
eight = Button(root, text='8', width=5, height=2 )
nine = Button(root, text='9', width=5, height=2 )
zero = Button(root, text='0', width=5, height=2 )


button1.bind('<Button-1>', fact)
one.bind('<Button-1>', One)
two.bind('<Button-1>', Two)
three.bind('<Button-1>', Three)
four.bind('<Button-1>', Four)
five.bind('<Button-1>', Five)
six.bind('<Button-1>', Six)
seven.bind('<Button-1>', Seven)
eight.bind('<Button-1>', Eight)
nine.bind('<Button-1>', Nine)
zero.bind('<Button-1>', Zero)


button1.grid(row=6, column=4)
one.grid(row='3', column='2')
two.grid(row='3', column='3')
three.grid(row='3', column='4')
four.grid(row='4', column='2')
five.grid(row='4', column='3')
six.grid(row='4', column='4')
seven.grid(row='5', column='2')
eight.grid(row='5', column='3')
nine.grid(row='5', column='4')
zero.grid(row='6', column='3')


mainloop()