from tkinter import *
from tkinter import ttk

app = Tk()
app.title("Fernando abas e notebook")
app.configure(bg="#efede9")
app.geometry("600x600")

nb = ttk.Notebook(app)
nb.place(x=0, y=0, width=500, height=300)

tb1 = Frame(nb, borderwidth=1, relief="solid")
nb.add(tb1, text="Frame 1")

tb2 = Frame(nb, borderwidth=1, relief="solid")
nb.add(tb2, text="Frame 2")

lbl1 = Label(tb1, text="Texto 1", bg="greenyellow")
lbl1.pack()

lbl2 = Label(tb2, text="Texto 2", bg="blue")
lbl2.pack()

app.mainloop()
