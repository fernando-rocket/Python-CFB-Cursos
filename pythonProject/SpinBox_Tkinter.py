from tkinter import *
from tkinter import messagebox


def spinbox_get():
    if 0 < int(valores.get()) < 101:
        print(valores.get())
    else:
        messagebox.showerror(title="Invad Number", message="Número Inválido! Tente entre 1 e 100.")


app = Tk()
app.title("Fernando SpinBox")
app.configure(bg="#efede9")
app.geometry("400x400")

valor = IntVar()

valores = Spinbox(app, from_=1, to=100, textvariable=valor)
valores.pack()

btn = Button(app, text="Show Number", command=spinbox_get)
btn.pack()

valores2 = Spinbox(app, values=(1,2,3))
valores2.pack(pady=50)

app.mainloop()
