from tkinter import *

app = Tk()
app.title("Fernando's Password")
app.geometry("200x200")
app.configure(bg="#efede9")

var_senha = StringVar()

p_senha = Entry(app, textvariable=var_senha, show="*")
p_senha.pack()


def mostrarsenha():
    if btn['text'] == "Mostrar Senha":
        p_senha["show"] = ""
        btn["text"] = "Esconder Senha"
    else:
        p_senha["show"] = "*"
        btn["text"] = "Mostrar Senha"
    print(p_senha.get())


btn = Button(app, text="Mostrar Senha", command=mostrarsenha)
btn.pack()

app.mainloop()
