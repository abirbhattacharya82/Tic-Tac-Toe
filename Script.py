from tkinter import *
window=Tk()
window.title("Tic Tac Toe")
def playable():
    if button1['text']!="" and button2['text']!="" and button3['text']!="" and button4['text']!="" and button5['text']!="" and button6['text']!="" and button7['text']!="" and button8['text']!="" and button9['text']!="":
        l1['text']="Match is Drawn"
        disabler()
        return False
    else:
        return True
def clicked1():
    if button1['text']=="":
        if l1['text']=="Player 1's Turn":
            button1['text']="X"
            if playable()==True:
                l1['text']="Player 2's Turn"
        else:
            button1['text']='O'
            l1['text']="Player 1's Turn"
        gameplay()
def clicked2():
    if button2['text']=="":
        if l1['text']=="Player 1's Turn":
            button2['text']="X"
            if playable()==True:
                l1['text']="Player 2's Turn"
        else:
            button2['text']="O"
            l1['text']="Player 1's Turn"
        gameplay()
def clicked3():
    if button3['text']=="":
        if l1['text']=="Player 1's Turn":
            button3['text']="X"
            if playable()==True:
                l1['text']="Player 2's Turn"
        else:
            button3['text']="O"
            l1['text']="Player 1's Turn"
        gameplay()
def clicked4():
    if button4['text']=="":
        if l1['text']=="Player 1's Turn":
            button4['text']="X"
            if playable()==True:
                l1['text']="Player 2's Turn"
        else:
            button4['text']="O"
            l1['text']="Player 1's Turn"
        gameplay()
def clicked5():
    if button5['text']=="":
        if l1['text']=="Player 1's Turn":
            button5['text']="X"
            if playable()==True:
                l1['text']="Player 2's Turn"
        else:
            button5['text']="O"
            l1['text']="Player 1's Turn"
        gameplay()
def clicked6():
    if button6['text']=="":
        if l1['text']=="Player 1's Turn":
            button6['text']="X"
            if playable()==True:
                l1['text']="Player 2's Turn"
        else:
            button6['text']="O"
            l1['text']="Player 1's Turn"
        gameplay()
def clicked7():
    if button7['text']=="":
        if l1['text']=="Player 1's Turn":
            button7['text']="X"
            if playable()==True:
                l1['text']="Player 2's Turn"
        else:
            button7['text']="O"
            l1['text']="Player 1's Turn"
        gameplay()
def clicked8():
    if button8['text']=="":
        if l1['text']=="Player 1's Turn":
            button8['text']="X"
            if playable()==True:
                l1['text']="Player 2's Turn"
        else:
            button8['text']="O"
            l1['text']="Player 1's Turn"
        gameplay()
def clicked9():
    if button9['text']=="":
        if l1['text']=="Player 1's Turn":
            button9['text']="X"
            if playable()==True:
                l1['text']="Player 2's Turn"
        else:
            button9['text']="O"
            l1['text']="Player 1's Turn"
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
            l1['text']="Player 1 Wins"
        else:
            l1['text']="Player 2 Wins"
        disabler()
    elif button4['text']==button5['text'] and button4['text']==button6['text'] and button4['text']!="":
        button4['bg']="green"
        button5['bg']="green"
        button6["bg"]="green"
        if button4['text']=="X":
            l1["text"]="Player 1 Wins"
        else:
            l1['text']="Player 2 Wins"
        disabler()
    elif button7['text']==button8['text'] and button7['text']==button9['text'] and button7['text']!="":
        button7['bg']="green"
        button8['bg']="green"
        button9["bg"]="green"
        if button7['text']=="X":
            l1['text']="Player 1 Wins"
        else:
            l1['text']="PLayer 2 Wins"
        disabler()
    elif button1['text']==button4['text'] and button1['text']==button7['text'] and button1['text']!="":
        button1['bg']="green"
        button4['bg']="green"
        button7["bg"]="green"
        if button7['text']=="X":
            l1['text']="Player 1 Wins"
        else:
            l1['text']="PLayer 2 Wins"
        disabler()
    elif button2['text']==button5['text'] and button2['text']==button8['text'] and button2['text']!="":
        button2['bg']="green"
        button5['bg']="green"
        button8["bg"]="green"
        if button2['text']=="X":
            l1['text']="Player 1 Wins"
        else:
            l1['text']="PLayer 2 Wins"
        disabler()
    elif button3['text']==button6['text'] and button3['text']==button9['text'] and button3['text']!="":
        button3['bg']="green"
        button6['bg']="green"
        button9["bg"]="green"
        if button3['text']=="X":
            l1['text']="Player 1 Wins"
        else:
            l1['text']="PLayer 2 Wins"
        disabler()
    elif button1['text']==button5['text'] and button1['text']==button9['text'] and button1['text']!="":
        button1['bg']="green"
        button5['bg']="green"
        button9["bg"]="green"
        if button1['text']=="X":
            l1['text']="Player 1 Wins"
        else:
            l1['text']="PLayer 2 Wins"
        disabler()
    elif button3['text']==button5['text'] and button3['text']==button7['text'] and button3['text']!="":
        button3['bg']="green"
        button5['bg']="green"
        button7["bg"]="green"
        if button7['text']=="X":
            l1['text']="Player 1 Wins"
        else:
            l1['text']="PLayer 2 Wins"
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
l1=Label(window,text="Player 1's Turn")
l1.grid(row=3,column=0,columnspan=3)

window.mainloop()
