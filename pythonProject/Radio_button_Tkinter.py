from tkinter import *

def showinfo():
    print(var_esporte.get())
    EsporteLB['text'] = var_esporte.get()

app = Tk()
app.title("Radio F Button")
app.geometry("500x500")
app.configure(bg="#dee")

var_esporte = StringVar()
var_esporte.set("Selecione um Esporte")

lb_esportes = Label(app, text="Esportes")
lb_esportes.pack()

rb_futebol = Radiobutton(app, text="Futebol", value="Futebol", variable=var_esporte)
rb_futebol.pack()

rb_volei = Radiobutton(app, text="Vôlei", value="Vôlei", variable=var_esporte)
rb_volei.pack()

rb_basquete = Radiobutton(app, text="Basquete", value="Basquete", variable=var_esporte)
rb_basquete.pack()

btn = Button(app, text="Esporte Selecionado", command=showinfo)
btn.pack()

EsporteLB = Label(app, text=f"{var_esporte.get()}", bg="#fff")
EsporteLB.pack(ipadx=50, ipady=20, anchor="center", pady=10)

app.mainloop()
