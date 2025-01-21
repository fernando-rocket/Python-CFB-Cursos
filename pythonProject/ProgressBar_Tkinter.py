from tkinter import *
from tkinter import ttk
from time import sleep


def valor_barra():
    for c in range(0, 101):
        sleep(0.01)
        var_barra.set(c)
        label_pc['text'] = f"{var_barra.get()}%"
        app.update()
    app.quit()


app = Tk()
app.title("Fernando's ProgressBar")
app.configure(bg="#efede9")
app.geometry("500x500")

var_barra = DoubleVar()
var_barra.set(0)

pb = ttk.Progressbar(app, variable=var_barra, maximum=100)
pb.pack(ipadx=100)

btn = Button(app, text="Valor Barra", command=valor_barra)
btn.pack()

label_pc = Label(app, text="0%")
label_pc.pack()

app.mainloop()
