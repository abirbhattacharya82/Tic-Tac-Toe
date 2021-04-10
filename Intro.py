from tkinter import *

window=Tk()
window.resizable(0,0)
window.title("Tic Tac Toe")

def Close():
    s1=e1.get()
    s2=e2.get()
    lines=s1+", "+s2
    f=open("Name.txt",'w')
    f.writelines(lines)
    f.close()
    window.destroy()
    
l1=Label(window,text="Player 1: ",font=("20"))
l1.grid(row=0,column=0)

l2=Label(window,text="Player 2: ",font=("20"))
l2.grid(row=1,column=0)

a=StringVar()
e1=Entry(window,textvariable=a,font=("20"))
e1.grid(row=0,column=1)

b=StringVar()
e2=Entry(window,textvariable=b,font=("20"))
e2.grid(row=1,column=1)

b=Button(window,text="Lessgo",height=2,width=10,command=Close)
b.grid(row=2,column=0,columnspan=2)

window.mainloop()
