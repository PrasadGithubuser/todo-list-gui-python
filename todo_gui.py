import tkinter as tk
from tkinter import messagebox
import os

tasks=[]

FILENAME='tasks.txt'

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME,'r') as file:
            for line in file:
                task,status=line.strip().split('||')
                tasks.append((task,status))
        update_listbox()

def save_tasks():
    with open(FILENAME,'w') as file:
        for task,status in tasks:
            file.write(f'{task}||{status}\n')

def add_task():
    task=entry.get().strip()
    if task=='':
        messagebox.showwarning('Input Error','Task cannot be empty!')
        return
    tasks.append((task,'Incomplete'))
    entry.delete(0,tk.END)
    update_listbox()
    save_tasks()

def delete_task():
    selected=listbox.curselection()
    if not selected:
        messagebox.showwarning('Select Task','Please select task to delete.')
        return
    index=selected[0]
    del tasks[index]
    update_listbox()
    save_tasks()

def toggle_status():
    selected=listbox.curselection()
    if not selected:
        messagebox.showerror('Select Task','Please select a task to mark as complete/incomplete')
        return
    index=selected[0]
    task,status=tasks[index]
    new_status='Completed' if status=='Incomplete' else 'Incomplete'
    tasks[index]=(task,new_status)
    update_listbox()
    save_tasks()

def update_listbox():
    listbox.delete(0,tk.END)
    for task,status in tasks:
        display=f'[👍]{task}' if status == 'Completed' else f'[]{task}'
        listbox.insert(tk.END,display)

root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x550")
root.config(bg='#f0f0f0')

title=tk.Label(root,text='To-Do List',font=('Arial',20,'bold'),bg='#f0f0f0',fg="#333")
title.pack(pady=10)

entry=tk.Entry(root,width=30,bg='#f0f0f0')
entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack()

add_button = tk.Button(button_frame, text="Add Task", width=12, command=add_task, bg="#4CAF50", fg="white")
add_button.grid(row=0, column=0, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete Task", width=12, command=delete_task, bg="#f44336", fg="white")
delete_button.grid(row=0, column=1, padx=5, pady=5)

status_button = tk.Button(button_frame, text="Toggle Status", width=12, command=toggle_status, bg="#2196F3", fg="white")
status_button.grid(row=0, column=2, padx=5, pady=5)


listbox=tk.Listbox(root,width=50,height=15,font=('Arial',12))
listbox.pack(pady=20)

load_tasks()

root.mainloop()