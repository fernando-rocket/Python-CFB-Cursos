from tkinter import *


def shownumber():
    print(scale_escala.get())


app = Tk()
app.title("Fernando Scale")
app.geometry("300x300")
app.configure(bg="#efede9")

label_valor = Label(app, text="Valor")
label_valor.pack()

scale_escala = Scale(app, from_=0, to=100, orient=HORIZONTAL)
scale_escala.set(50)
scale_escala.pack()

btn = Button(app, text="Show Number", command=shownumber)
btn.pack()

app.mainloop()
