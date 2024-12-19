import json
import tkinter as tk
import threading

def getval():
    with open('pomodoro_setting.json') as f:
        data = json.load(f)
    return data

time = 0
cnt = int(0)
flag1, flag2, flag3 = 'after#0', 'after#0', 'after#0'

def stop(frame: tk.Frame):
    global flag1, flag2, flag3
    frame.after_cancel(flag1)
    frame.after_cancel(flag2)
    frame.after_cancel(flag3)

def count_w(frame, t, c, text):
    global time, cnt, short_break, long_break, work, circulation
    time = c
    min = time // 60
    sec = time % 60
    t['text'] = f'{min} : {sec}  {text}'
    time -= 1
    global flag1  
    if time >= 0:
        flag1 = frame.after(1000, count_w, frame, t, time, text)
    else:
        flag1 = 'after#0'
        if cnt == circulation:
            time = long_break
            count_l(frame,t,time,"long break")
        else:
            cnt += 1
            time = short_break
            count_s(frame,t,time,"short break")

def count_s(frame, t, c, text):
    global time, work, circulation
    time = c
    min = time // 60
    sec = time % 60
    t['text'] = f'{min} : {sec}  {text}'
    time -= 1
    global flag2
    if time >= 0:
        flag2 = frame.after(1000, count_s, frame, t, time, text)
    else:
        flag2 = 'after#0'
        time = work
        count_w(frame, t, time, "work")

def count_l(frame, t, c, text):
    global time, work, circulation, cnt
    time = c
    min = time // 60
    sec = time % 60
    t['text'] = f'{min} : {sec}  {text}'
    time -= 1
    global flag3
    if time >= 0:
        flag3 = frame.after(1000, count_l, frame, t, time, text)
    else:
        cnt = 0
        flag3 = 'after#0'
        time = work
        count_w(frame, t, time, "work")
        
def countdown(frame,width):
    global work, short_break, long_break, circulation, time

    work = int(getval()['pomodoro time'] * 60)
    short_break = int(getval()['short break time'] * 60)
    long_break = int(getval()['long break time'] * 60)
    circulation = getval()['circulation']

    t = tk.Label(frame, width=width,font=('microsoft yahei', 30))
    t.grid(row=1,column=0,columnspan=2,padx=20,pady=20)

    global flag1, flag2, flag3
    if flag1[6:] != '0' or flag1 == flag2 == flag3 == 'after#0':
        time = work
        target = count_w
        args=(frame,t,time,"work")
    elif flag2[6:] != '0':
        target = count_s
        args=(frame,t,time,"short break")
    elif flag3[6:] != '0':
        target = count_l
        args=(frame,t,time,"long break")

    p1 = threading.Thread(target=target,args=args)
    p1.start()