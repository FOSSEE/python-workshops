import tkinter as tk
root = tk.Tk()
f = tk.Frame(master=root)
f.pack()
l = tk.Label(f, text='Hello world!')
l.pack()

def clicked():
    print("Hello")


b = tk.Button(f, text='Click me!', fg='red', command=clicked)
b.pack()

root.mainloop()
