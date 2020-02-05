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














    nument.place(x = 245,y = 115)
    nument2.place(x = 235,y = 155)
    numtxt.place(x = 100,y=110)
    numtxt2.place(x = 100,y=150)
    caltxt.place(x = 190,y = 40)
    tk.mainloop()
