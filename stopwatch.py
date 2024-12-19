import tkinter as tk

time = 0
font=('microsoft yahei', 12)

def count(t):
    global time
    hr = time // 3600
    mn = (time % 3600) // 60
    sc = time % 60
    t['text'] = f'{hr} : {mn} : {sc}'
    time += 1
    global timer
    timer = t.after(1000, count, t)

def stopwatch_start(label, start, pause, reset):
    global time
    count(label)
    start['state'] = tk.DISABLED
    pause['state'] = tk.NORMAL
    reset['state'] = tk.NORMAL
    

def stopwatch_pause(label, start, pause, reset):
    global timer
    label.after_cancel(timer)
    start['state'] = tk.NORMAL
    pause['state'] = tk.DISABLED
    reset['state'] = tk.NORMAL

def stopwatch_reset(label, start, pause, reset):
    global timer
    label.after_cancel(timer)
    global time
    time = 0
    label['text'] = '0 : 0 : 0'
    start['state'] = tk.NORMAL
    pause['state'] = tk.DISABLED
    reset['state'] = tk.DISABLED