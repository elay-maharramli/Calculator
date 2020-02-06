from tkinter import *

tk = Tk()
tk.wm_iconbitmap('icon.ico')
tk.title('Simple Calculator')
tk.configure(bg="grey")
tk.minsize(570,500)
tk.maxsize(570,500)

while True:
    
    def add():
        result.configure(text=str(int(nument.get()) + int(nument2.get())))
    def sub():
        result.configure(text=str(int(nument.get()) - int(nument2.get())))
    def mul():
        result.configure(text=str(int(nument.get()) * int(nument2.get())))
    def div():
        result.configure(text=str(int(int(nument.get()) / int(nument2.get()))))
    def clean():
        nument.delete(0,'end')
        nument2.delete(0,'end')
        result.configure(text="")


    
    caltxt = Label(text="Kalkulyator",bg="grey",fg="blue",font=("Arial", 23))
    numtxt = Label(text="Birinci ədəd:",bg="grey",font=("Arial", 15))
    numtxt2 = Label(text="İkinci ədəd:",bg="grey",font=("Arial", 15))
    resulttxt = Label(text="Nəticə:",bg="grey",font=("Arial",16))
    nument = Entry()
    nument2 = Entry()
    add = Button(text="+",bg="green",width=5,command=add)
    sub = Button(text="-",bg="green",width=5,command=sub)
    mul = Button(text="x",bg="green",width=5,command=mul)
    div = Button(text="/",bg="green",width=5,command=div)
    clean = Button(text="C",bg="orange",width=5,command=clean)
    result = Label(text="",bg="grey",font=("Arial", 16))
    



    add.place(x = 150,y = 220)
    sub.place(x = 220,y = 220)
    mul.place(x = 290,y = 220)
    div.place(x = 360,y = 220)
    clean.place(x = 330,y = 300)
    nument.place(x = 275,y = 115)
    nument2.place(x = 275,y = 155)
    numtxt.place(x = 130,y=110)
    numtxt2.place(x = 130,y=150)
    caltxt.place(x = 210,y = 40)
    resulttxt.place(x = 130,y = 300)
    result.place(x = 230,y = 300)
    tk.mainloop()
