import json
import calendar
from datetime import date
import tkinter as tk

font=('microsoft yahei', 14)

def add(box, index, e, todo, year, month, frame):
    e.delete(0, tk.END)
    box.insert(tk.END, todo)
    f = open("note.json")
    data = json.load(f)
    try:
        data[index].append(todo)
    except KeyError:
        data[index] = []
        data[index].append(todo)
    f = open("note.json",'w')
    json.dump(data,f)
    f.close()
    show(year, month, frame)

def remove(box, index, year, month, frame):
    f = open("note.json")
    data = json.load(f)
    for i in tuple(reversed(box.curselection())):
        data[index].pop(i)
        box.delete(i)
    f = open("note.json",'w')
    json.dump(data,f)
    f.close()
    show(year, month, frame)

def task(year, month, day, cldframe):
    monthdict = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
    weekdict = {0:'Mon',1:'Tue',2:'Wed',3:'Thr',4:'Fri',5:'Sat',6:'Sun'}

    with open('note.json') as f:
        data = json.load(f)

    frame = tk.Tk()
    frame.title('calendar')
    frame.iconbitmap('study.ico')
    frame.attributes('-topmost', True)
    week = calendar.weekday(year, month, day)
    label = tk.Label(frame, text=f'{year}-{monthdict[month]}-{day}-{weekdict[week]}',font=font)
    label.pack(padx=10)

    box = tk.Listbox(frame,width=70,font=('microsoft yahei', 12))
    index = f'{year}-{monthdict[month]}-{day}-{weekdict[week]}'

    try:
        for i in data[index]:
            box.insert(tk.END, i)
    except KeyError:
        pass
    box.pack(padx=10,pady=10)

    rembtn = tk.Button(frame,text='remove selected event',font=('microsoft yahei', 12),width=60,
        command=lambda:remove(box, index, year, month, cldframe)
    )
    rembtn.pack(padx=10)

    addlabel = tk.Label(frame,text='add event :',font=font)
    addlabel.pack(padx=10,pady=10)

    addentry = tk.Entry(frame,font=('microsoft yahei', 12),width=70)
    addentry.pack()

    addbtn = tk.Button(frame,text='add',font=('microsoft yahei', 12),width=60,
        command=lambda:add(box, index, addentry, addentry.get(), year, month, cldframe)
    )
    addbtn.pack(padx=10,pady=10)

    frame.mainloop()

def show(year, month, frame):
    screenw = frame.winfo_screenwidth()//28
    width = screenw//7-1
    for i in frame.winfo_children():
        i.destroy()
    
    if month == 0:
        month = 12
        year -= 1
    if month == 13:
        month = 1
        year += 1

    label = tk.Label(frame,width=10)
    label.grid(row=0,column=0,rowspan=8)

    monthdict = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
    weekdict = {0:'Mon',1:'Tue',2:'Wed',3:'Thr',4:'Fri',5:'Sat',6:'Sun'}
    yearlabel = tk.Label(frame, text=year,font=font)
    yearlabel.grid(row=0,column=1,columnspan=7,padx=2)

    monthlabel = tk.Label(frame, text=monthdict[month],font=font)
    monthlabel.grid(row=1,column=1,columnspan=7,padx=2)

    tk.Label(frame,text='Sun',font=font).grid(row=2,column=1,padx=2)
    tk.Label(frame,text='Mon',font=font).grid(row=2,column=2,padx=2)
    tk.Label(frame,text='Tue',font=font).grid(row=2,column=3,padx=2)
    tk.Label(frame,text='Wed',font=font).grid(row=2,column=4,padx=2)
    tk.Label(frame,text='Thr',font=font).grid(row=2,column=5,padx=2)
    tk.Label(frame,text='Fri',font=font).grid(row=2,column=6,padx=2)
    tk.Label(frame,text='Sat',font=font).grid(row=2,column=7,padx=2)

    lastmonth = tk.Button(frame, text='<-',font=font, width=width, command=lambda:show(year, month-1, frame))
    lastmonth.grid(row=1,column=1)

    nextmonth = tk.Button(frame, text='->',font=font, width=width, command=lambda:show(year, month+1, frame))
    nextmonth.grid(row=1,column=7)

    cal = calendar.monthcalendar(year, month)
    for i in range(len(cal)):
        cal.extend(cal[i])
    cal = cal[6:]
    for i in reversed(range(len(cal))):
        if cal[i] == 0:cal.pop(i)
    btn = []
    week = calendar.weekday(year, month, 1)
    
    while True:
        btn.append(tk.Button(frame, text=1,font=font, width=width, command=lambda:task(year, month, 1, frame)))
        btn.append(tk.Button(frame, text=2,font=font, width=width, command=lambda:task(year, month, 2, frame)))
        btn.append(tk.Button(frame, text=3,font=font, width=width, command=lambda:task(year, month, 3, frame)))
        btn.append(tk.Button(frame, text=4,font=font, width=width, command=lambda:task(year, month, 4, frame)))
        btn.append(tk.Button(frame, text=5,font=font, width=width, command=lambda:task(year, month, 5, frame)))
        btn.append(tk.Button(frame, text=6,font=font, width=width, command=lambda:task(year, month, 6, frame)))
        btn.append(tk.Button(frame, text=7,font=font, width=width, command=lambda:task(year, month, 7, frame)))
        btn.append(tk.Button(frame, text=8,font=font, width=width, command=lambda:task(year, month, 8, frame)))
        btn.append(tk.Button(frame, text=9,font=font, width=width, command=lambda:task(year, month, 9, frame)))
        btn.append(tk.Button(frame, text=10,font=font, width=width, command=lambda:task(year, month, 10, frame)))
        btn.append(tk.Button(frame, text=11,font=font, width=width, command=lambda:task(year, month, 11, frame)))
        btn.append(tk.Button(frame, text=12,font=font, width=width, command=lambda:task(year, month, 12, frame)))
        btn.append(tk.Button(frame, text=13,font=font, width=width, command=lambda:task(year, month, 13, frame)))
        btn.append(tk.Button(frame, text=14,font=font, width=width, command=lambda:task(year, month, 14, frame)))
        btn.append(tk.Button(frame, text=15,font=font, width=width, command=lambda:task(year, month, 15, frame)))
        btn.append(tk.Button(frame, text=16,font=font, width=width, command=lambda:task(year, month, 16, frame)))
        btn.append(tk.Button(frame, text=17,font=font, width=width, command=lambda:task(year, month, 17, frame)))
        btn.append(tk.Button(frame, text=18,font=font, width=width, command=lambda:task(year, month, 18, frame)))
        btn.append(tk.Button(frame, text=19,font=font, width=width, command=lambda:task(year, month, 19, frame)))
        btn.append(tk.Button(frame, text=20,font=font, width=width, command=lambda:task(year, month, 20, frame)))
        btn.append(tk.Button(frame, text=21,font=font, width=width, command=lambda:task(year, month, 21, frame)))
        btn.append(tk.Button(frame, text=22,font=font, width=width, command=lambda:task(year, month, 22, frame)))
        btn.append(tk.Button(frame, text=23,font=font, width=width, command=lambda:task(year, month, 23, frame)))
        btn.append(tk.Button(frame, text=24,font=font, width=width, command=lambda:task(year, month, 24, frame)))
        btn.append(tk.Button(frame, text=25,font=font, width=width, command=lambda:task(year, month, 25, frame)))
        btn.append(tk.Button(frame, text=26,font=font, width=width, command=lambda:task(year, month, 26, frame)))
        btn.append(tk.Button(frame, text=27,font=font, width=width, command=lambda:task(year, month, 27, frame)))
        btn.append(tk.Button(frame, text=28,font=font, width=width, command=lambda:task(year, month, 28, frame)))
        if len(cal) == 28: break
        else:
            btn.append(tk.Button(frame, text=29,font=font, width=width, command=lambda:task(year, month, 29, frame)))
            if len(cal) == 29: break
            else:
                btn.append(tk.Button(frame, text=30,font=font, width=width, command=lambda:task(year, month, 30, frame)))
                if len(cal) == 30: break
                else:
                    btn.append(tk.Button(frame, text=31,font=font, width=width, command=lambda:task(year, month, 31, frame)))
                    break

    with open('note.json') as f:
        data = json.load(f)
    

    for i in range(len(cal)):
        weekday = calendar.weekday(year, month, cal[i])
        try:
            if data[f'{year}-{monthdict[month]}-{i+1}-{weekdict[weekday]}'][0] != None:
                btn[i].config(bg='lime')
        except:
            pass
        if year == date.today().year and month == date.today().month and i+1 == date.today().day:
            btn[i].config(fg='red')
        btn[i].grid(row=(i +1 + week)//7+3, column=(i + 1 + week)%7 + 1)