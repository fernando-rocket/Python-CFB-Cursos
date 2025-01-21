from tkinter import *

app = Tk()
app.title("FFrame")
app.geometry("500x500")
app.configure(bg="#efede9")

frame1 = Frame(app, borderwidth=1, relief="raised")
frame1.place(x=10, y=10, width=300, height=100)

Label(frame1, bg="greenyellow", text="Frame teste").place(x=100, y=30, width=100, height=40)

app.mainloop()
