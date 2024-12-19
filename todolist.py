import tkinter as tk
import json

def todolist_add(todo, box:tk.Listbox, e:tk.Entry):
    e.delete(0, tk.END)
    box.insert(tk.END, todo)
    f = open("todo.json")
    data = json.load(f)
    data.append(todo)
    f = open("todo.json",'w')
    json.dump(data,f)

def todolist_rem(box:tk.Listbox):
    f = open("todo.json")
    data = json.load(f)
    for i in tuple(reversed(box.curselection())):
        data.pop(i)
        box.delete(i)
    f = open("todo.json",'w')
    json.dump(data,f)