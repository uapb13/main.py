from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

f = open('Student_list.txt', 'a')
def swrite(event):
    f.write(f'{strF2.get()} {strF3.get()} {strF.get()} - {radiost.get()}\n')
    f.close()

prog = ttk.Frame()
labelF = ttk.Label(text='Фамилия')
labelF.grid(column=0, row=0)

strF = StringVar()
editF = ttk.Entry(textvariable=strF)
editF.grid(column=0, row=1)

labelF2 = ttk.Label(text='Имя')
labelF2.grid(column=0, row=2)

strF2 = StringVar()
editF2 = ttk.Entry(textvariable=strF2)
editF2.grid(column=0, row=3)

bts = ttk.Button(text='Записать')
bts.bind('<Button-1>', swrite)
bts.grid(column=0, row=9)

prog.mainloop()
