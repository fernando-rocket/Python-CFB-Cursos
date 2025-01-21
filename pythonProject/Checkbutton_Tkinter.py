from tkinter import *


def genericcommand():
    if var_futebol.get(): # Se ele valer 1
        print("Futebol")


app = Tk()
app.title("Fernando CheckButton")
app.geometry("500x500")
app.configure(bg="#efede9")

main_frame = Frame(app, borderwidth=1, relief="solid")
main_frame.place(x=10, y=10, width=100, height=75)

var_futebol = IntVar() # Fazer isso deixa a seleção mais limpa e não precisa ficar clicando várias vezes
var_volei = IntVar()
var_basquete = IntVar()

cb_futebol = Checkbutton(main_frame, text="Futebol", variable=var_futebol, onvalue=1, offvalue=0,  command=genericcommand)
cb_futebol.pack(side=TOP, anchor=W)
cb_volei = Checkbutton(main_frame, text="Vôlei", variable=var_volei, onvalue=1, offvalue=0)
cb_volei.pack(side=TOP, anchor=W)
cb_basquete = Checkbutton(main_frame, text="Basquete", variable=var_basquete, onvalue=1, offvalue=0)
cb_basquete.pack(side=TOP, anchor=W)


app.mainloop()
