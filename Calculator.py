from tkinter import *

tk = Tk()
tk.wm_iconbitmap('icon.ico')
tk.title('Simple Calculator')
tk.configure(bg="grey")
tk.minsize(570,530)
tk.maxsize(570,530)

while True:
    caltxt = Label(text="Kalkulyator",bg="grey",fg="blue",font=("Arial", 23))
    numtxt = Label(text="Birinci ədəd:",bg="grey",font=("Arial", 15))
    numtxt2 = Label(text="İkinci ədəd:",bg="grey",font=("Arial", 15))
    nument = Entry()
    nument2 = Entry()
    add = Button(text="+",bg="green",width=5)
    sub = Button(text="-",bg="green",width=5)
    mul = Button(text="x",bg="green",width=5)
    div = Button(text="/",bg="green",width=5)












    add.place(x = 110,y = 200)
    sub.place(x = 180,y = 200)
    mul.place(x = 250,y = 200)
    div.place(x = 320,y = 200)
    nument.place(x = 245,y = 115)
    nument2.place(x = 245,y = 155)
    numtxt.place(x = 100,y=110)
    numtxt2.place(x = 100,y=150)
    caltxt.place(x = 190,y = 40)
    tk.mainloop()
