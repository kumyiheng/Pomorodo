import tkinter as tk
import setting as s
from datetime import date
import json

import pomodoro as pmd
import stopwatch as stw
import countdown as cnt
import todolist as tdl
import Calendar as cld

mother = tk.Tk()

mother.state('zoomed')
mother.title('Study assistant')
mother.resizable(False, False)
screenw = mother.winfo_screenwidth() - 60
screenh = mother.winfo_screenheight() - 63
mother.iconbitmap('study.ico')

width = screenw//10

pmdframe = tk.LabelFrame(mother,width=screenw//3,height=screenh//2)
stwframe = tk.LabelFrame(mother,width=screenw//3,height=screenh//2)
ctdframe = tk.LabelFrame(mother,width=screenw//3,height=screenh//2)
cldframe = tk.LabelFrame(mother,width=screenw//2,height=screenh//2)
tdlframe = tk.LabelFrame(mother,width=screenw//2,height=screenh//2)

pmdframe.grid(row=0,column=0,padx=10,pady=10,columnspan=2)
stwframe.grid(row=0,column=2,padx=10,pady=10,columnspan=2)
ctdframe.grid(row=0,column=4,padx=10,pady=10,columnspan=2)
cldframe.grid(row=1,column=0,padx=10,pady=10,columnspan=3)
tdlframe.grid(row=1,column=3,padx=10,pady=10,columnspan=3)

pmdframe.grid_propagate(False)
stwframe.grid_propagate(False)
ctdframe.grid_propagate(False)
cldframe.grid_propagate(False)
tdlframe.grid_propagate(False)

font=('microsoft yahei', 12)

pmdframe.config(labelanchor='n',text='pomodoro',font=font)
stwframe.config(labelanchor='n',text='stopwatch',font=font)
ctdframe.config(labelanchor='n',text='countdown',font=font)
cldframe.config(labelanchor='n',text='calendar',font=font)
tdlframe.config(labelanchor='n',text='todolist',font=font)

#pomodoro
w = width//8
pmdbtn = tk.Button(pmdframe,text="start pomodoro",font=font,width=(width//8),
    command=lambda:pmd.countdown(pmdframe,w)
)
pmdbtn.grid(row=0,column=0,pady=10)

pmdstop = tk.Button(pmdframe,text='stop pomodoro',font=font,width=(width//8),
    command=lambda:pmd.stop(pmdframe)
)
pmdstop.grid(row=0,column=1,pady=10)

pmdtime = tk.Label(pmdframe, text='',width=width//8,font=('microsoft yahei', 30))
pmdtime.grid(row=1,column=0,columnspan=2,padx=20,pady=20)

with open('pomodoro_setting.json') as pmdfile:
    pmddata = json.load(pmdfile)

workval = tk.StringVar(value=pmddata['pomodoro time'])
shortval = tk.StringVar(value=pmddata['short break time'])
longval = tk.StringVar(value=pmddata['long break time'])
circval = tk.StringVar(value=pmddata['circulation'])

worklabel = tk.Label(pmdframe, text='work time :',font=font)
shortlabel = tk.Label(pmdframe, text='short break time :',font=font)
longlabel = tk.Label(pmdframe, text='long break time :',font=font)
circlabel = tk.Label(pmdframe, text='circulation :',font=font)

workentry = tk.Entry(pmdframe, textvariable=workval,font=font)
shortentry = tk.Entry(pmdframe, textvariable=shortval,font=font)
longentry = tk.Entry(pmdframe, textvariable=longval,font=font)
circentry = tk.Entry(pmdframe, textvariable=circval,font=font)

worklabel.grid(row=2,column=0,pady=3)
workentry.grid(row=3,column=0,pady=3)
shortlabel.grid(row=2,column=1,pady=3)
shortentry.grid(row=3,column=1,pady=3)
longlabel.grid(row=4,column=0,pady=3)
longentry.grid(row=5,column=0,pady=3)
circlabel.grid(row=4,column=1,pady=3)
circentry.grid(row=5,column=1,pady=3)

setbtn = tk.Button(pmdframe,text='set pomodoro',font=font,width=(width//7)*2,
    command=lambda:s.pomodoro_set(workentry.get(), shortentry.get(), longentry.get(), circentry.get())
)
setbtn.grid(row=6,column=0,columnspan=2,pady=10)
#pomodoro

#stopwatch
stwlabel = tk.Label(stwframe,text='0 : 0 : 0',font=('microsoft yahei', 30),width=width//8)
stwlabel.grid(row=0,column=0,columnspan=3,padx=20,pady=100)

stwstart = tk.Button(stwframe,text='start',font=font, state=tk.NORMAL,width=width//10,
    command=lambda:stw.stopwatch_start(stwlabel, stwstart, stwpause, stwreset)
)
stwstart.grid(row=1,column=0,pady=10)

stwpause = tk.Button(stwframe, text='pause',font=font, state=tk.DISABLED,width=width//10,
    command=lambda:stw.stopwatch_pause(stwlabel, stwstart, stwpause, stwreset)
)
stwpause.grid(row=1,column=1,pady=10)

stwreset = tk.Button(stwframe,text='reset',font=font, state=tk.DISABLED,width=width//10,
    command=lambda:stw.stopwatch_reset(stwlabel, stwstart, stwpause, stwreset)
)
stwreset.grid(row=1,column=2,pady=10)
#stopwatch

#countdown
hrtext = tk.StringVar()
mntext = tk.StringVar()
sctext = tk.StringVar()

hrtext.set('0')
mntext.set('0')
sctext.set('0')

ctdentry_hr = tk.Entry(ctdframe, textvariable=hrtext, font=font, width=width//9)
ctdentry_mn = tk.Entry(ctdframe, textvariable=mntext, font=font, width=width//9)
ctdentry_sc = tk.Entry(ctdframe, textvariable=sctext, font=font, width=width//9)

ctdentry_hr.grid(row=0,column=0,pady=10)
ctdentry_mn.grid(row=0,column=1,pady=10)
ctdentry_sc.grid(row=0,column=2,pady=10)

ctdbtn = tk.Button(ctdframe,text="countdown",font=font,width=(width//3)-4,
    command=lambda:cnt.countdown(frame=ctdframe,
        hr=ctdentry_hr.get(),
        mn=ctdentry_mn.get(),
        sc=ctdentry_sc.get(),
    )
)
ctdbtn.grid(row=1,column=0,padx=10,pady=10,columnspan=3)
#countdown

#calendar
today = str(date.today())
year = today[:4]
month = today[5:7]
day = today[8:]

cld.show(int(year), int(month), cldframe)
#calendar

#todolist
tdlent = tk.Entry(tdlframe,font=font,width=width//2)
tdlent.grid(row=0,column=0,padx=10,pady=10,columnspan=2)

with open("todo.json") as todofile:
    tdldata = json.load(todofile)

tdlbox = tk.Listbox(tdlframe, selectmode=tk.MULTIPLE,font=font,width=width//2)
for i in tdldata:
    tdlbox.insert(tk.END, i)
tdlbox.grid(row=1,column=0,padx=10,pady=10,columnspan=2)

tdladd = tk.Button(tdlframe,text='add',font=font, width=width//5,
    command=lambda:tdl.todolist_add(tdlent.get(), tdlbox, tdlent)
)
tdladd.grid(row=2,column=0)

tdlrem = tk.Button(tdlframe,text='remove',font=font, width=width//5,
    command=lambda:tdl.todolist_rem(tdlbox)
)
tdlrem.grid(row=2,column=1)
#todolist

mother.mainloop()