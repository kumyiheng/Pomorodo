import tkinter as tk
from pygame import mixer
import threading

def music_play():
    mixer.init()
    mixer.music.load('1.mp3')
    mixer.music.play()
    while mixer.music.get_busy(): pass

def count(frame, t, c):
    hr = c // 3600
    mn = (c % 3600) // 60
    sc = c % 60
    t['text'] = f'{hr} : {mn} : {sc}'

    if c > 0:
        frame.after(1000, count, frame, t, c - 1)
    else:
        t['text'] = '0 : 0 : 0'
        threading.Thread(target=music_play).start()

def countdown(frame, hr, mn, sc):
    hr = int(hr)
    mn = int(mn)
    sc = int(sc)
    time = hr*3600+mn*60+sc

    t = tk.Label(frame,width=20,font=('microsoft yahei', 30))
    t.grid(row=2,column=0,columnspan=3,pady=80)

    count(frame, t, time)