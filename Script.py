from tkinter import *
import Intro

window=Tk()
window.title("Tic Tac Toe")
f=open("Name.txt","r")
l=f.readlines()[0]

s1=l[:l.index(',')]
s2=l[l.index(',')+2:]

def playable():
    if button1['text']!="" and button2['text']!="" and button3['text']!="" and button4['text']!="" and button5['text']!="" and button6['text']!="" and button7['text']!="" and button8['text']!="" and button9['text']!="":
        l1['text']="Match is Drawn"
        disabler()
        return False
    else:
        return True
def clicked1():
    z=s1+"'s Turn"
    if button1['text']=="":
        if l1['text']==z:
            button1['text']="X"
            if playable()==True:
                l1['text']=s2+"'s Turn"
        else:
            button1['text']='O'
            l1['text']=s1+"'s Turn"
        gameplay()
def clicked2():
    z=s1+"'s Turn"
    if button2['text']=="":
        if l1['text']==z:
            button2['text']="X"
            if playable()==True:
                l1['text']=s2+"'s Turn"
        else:
            button2['text']="O"
            l1['text']=s1+"'s Turn"
        gameplay()
def clicked3():
    z=s1+"'s Turn"
    if button3['text']=="":
        if l1['text']==z:
            button3['text']="X"
            if playable()==True:
                l1['text']=s2+"'s Turn"
        else:
            button3['text']="O"
            l1['text']=s1+"'s Turn"
        gameplay()
def clicked4():
    z=s1+"'s Turn"
    if button4['text']=="":
        if l1['text']==z:
            button4['text']="X"
            if playable()==True:
                l1['text']=s2+"'s Turn"
        else:
            button4['text']="O"
            l1['text']=s1+"'s Turn"
        gameplay()
def clicked5():
    z=s1+"'s Turn"
    if button5['text']=="":
        if l1['text']==z:
            button5['text']="X"
            if playable()==True:
                l1['text']=s2+"'s Turn"
        else:
            button5['text']="O"
            l1['text']=s1+"'s Turn"
        gameplay()
def clicked6():
    z=s1+"'s Turn"
    if button6['text']=="":
        if l1['text']==z:
            button6['text']="X"
            if playable()==True:
                l1['text']=s2+"'s Turn"
        else:
            button6['text']="O"
            l1['text']=s1+"'s Turn"
        gameplay()
def clicked7():
    z=s1+"'s Turn"
    if button7['text']=="":
        if l1['text']==z:
            button7['text']="X"
            if playable()==True:
                l1['text']=s2+"'s Turn"
        else:
            button7['text']="O"
            l1['text']=s1+"'s Turn"
        gameplay()
def clicked8():
    z=s1+"'s Turn"
    if button8['text']=="":
        if l1['text']==z:
            button8['text']="X"
            if playable()==True:
                l1['text']=s2+"'s Turn"
        else:
            button8['text']="O"
            l1['text']=s1+"'s Turn"
        gameplay()
def clicked9():
    z=s1+"'s Turn"
    if button9['text']=="":
        if l1['text']==z:
            button9['text']="X"
            if playable()==True:
                l1['text']=s2+"'s Turn"
        else:
            button9['text']="O"
            l1['text']=s1+"'s Turn"
        gameplay()
def disabler():
    button1['state']=DISABLED
    button2['state']=DISABLED
    button3['state']=DISABLED
    button4['state']=DISABLED
    button5['state']=DISABLED
    button6['state']=DISABLED
    button7['state']=DISABLED
    button8['state']=DISABLED
    button9['state']=DISABLED
def gameplay():
    if button1['text']==button2['text'] and button1['text']==button3['text'] and button1['text']!="":
        button1['bg']="green"
        button2['bg']="green"
        button3['bg']="green"
        if button1['text']=="X":
            l1['text']=s1+" Wins"
        else:
            l1['text']=s2+" Wins"
        disabler()
    elif button4['text']==button5['text'] and button4['text']==button6['text'] and button4['text']!="":
        button4['bg']="green"
        button5['bg']="green"
        button6["bg"]="green"
        if button4['text']=="X":
            l1['text']=s1+" Wins"
        else:
            l1['text']=s2+" Wins"
        disabler()
    elif button7['text']==button8['text'] and button7['text']==button9['text'] and button7['text']!="":
        button7['bg']="green"
        button8['bg']="green"
        button9["bg"]="green"
        if button7['text']=="X":
            l1['text']=s1+" Wins"
        else:
            l1['text']=s2+" Wins"
        disabler()
    elif button1['text']==button4['text'] and button1['text']==button7['text'] and button1['text']!="":
        button1['bg']="green"
        button4['bg']="green"
        button7["bg"]="green"
        if button7['text']=="X":
            l1['text']=s1+" Wins"
        else:
            l1['text']=s2+" Wins"
        disabler()
    elif button2['text']==button5['text'] and button2['text']==button8['text'] and button2['text']!="":
        button2['bg']="green"
        button5['bg']="green"
        button8["bg"]="green"
        if button2['text']=="X":
            l1['text']=s1+" Wins"
        else:
            l1['text']=s2+" Wins"
        disabler()
    elif button3['text']==button6['text'] and button3['text']==button9['text'] and button3['text']!="":
        button3['bg']="green"
        button6['bg']="green"
        button9["bg"]="green"
        if button3['text']=="X":
            l1['text']=s1+" Wins"
        else:
            l1['text']=s2+" Wins"
        disabler()
    elif button1['text']==button5['text'] and button1['text']==button9['text'] and button1['text']!="":
        button1['bg']="green"
        button5['bg']="green"
        button9["bg"]="green"
        if button1['text']=="X":
            l1['text']=s1+" Wins"
        else:
            l1['text']=s2+" Wins"
        disabler()
    elif button3['text']==button5['text'] and button3['text']==button7['text'] and button3['text']!="":
        button3['bg']="green"
        button5['bg']="green"
        button7["bg"]="green"
        if button7['text']=="X":
            l1['text']=s1+" Wins"
        else:
            l1['text']=s2+" Wins"
        disabler()
button1=Button(window,text="",width=10,height=5,command=clicked1,font=("10"))
button1.grid(row=0,column=0)
button2=Button(window,text="",width=10,height=5,command=clicked2,font=("10"))
button2.grid(row=0,column=1)
button3=Button(window,text="",width=10,height=5,command=clicked3,font=("10"))
button3.grid(row=0,column=2)
button4=Button(window,text="",width=10,height=5,command=clicked4,font=("10"))
button4.grid(row=1,column=0)
button5=Button(window,text="",width=10,height=5,command=clicked5,font=("10"))
button5.grid(row=1,column=1)
button6=Button(window,text="",width=10,height=5,command=clicked6,font=("10"))
button6.grid(row=1,column=2)
button7=Button(window,text="",width=10,height=5,command=clicked7,font=("10"))
button7.grid(row=2,column=0)
button8=Button(window,text="",width=10,height=5,command=clicked8,font=("10"))
button8.grid(row=2,column=1)
button9=Button(window,text="",width=10,height=5,command=clicked9,font=("10"))
button9.grid(row=2,column=2)
dd=s1+"'s Turn"
l1=Label(window,text=dd)
l1.grid(row=3,column=0,columnspan=3)

window.mainloop()
