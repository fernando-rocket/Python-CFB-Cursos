from tkinter import *
import os

nome = "texto.txt"
caminho = "C:/Users/Fernando/Documents/code/"

if os.path.exists(caminho+nome):
    document_txt = open(caminho+nome, "at")
    print("DOCUMENTO EXISTENTE")
else:
    document_txt = open(caminho + nome, "x")
    print("DOCUMENTO CRIADO")

app = Tk()
app.title("Fernando's window")
app.geometry("500x500")
app.configure(bg="#dde")

Label(master=app, text="Nome", bg="#dde", foreground="#009").place(x=10, y=10, width=100, height=40)
name = Entry(app)
name.place(x=110, y=10, width=200, height=40)

Label(master=app, text="Email", bg="#dde", foreground="#009").place(x=10, y=60, width=100, height=40)
email = Entry(app)
email.place(x=110, y=60, width=200, height=40)

Label(master=app, text="Telefone", bg="#dde", foreground="#009").place(x=10, y=110, width=100, height=40)
tel = Entry(app)
tel.place(x=110, y=110, width=200, height=40)

Label(master=app, text="OBS", bg="#dde", foreground="#009").place(x=10, y=160, width=100, height=40)
text = Text(app, font="Arial")
text.place(x=110, y=160, width=300, height=80)


def showdata():
    print(f"Nome: {name.get()}")
    print(f"Email: {email.get()}")
    print(f"Telefone: {tel.get()}")
    print(f"OBS: {text.get(index1="1.0", index2=END)}")
    document_txt.write(f"""Nome: {name.get()}
Email: {email.get()}
Telefone: {tel.get()}
OBS: {text.get(index1="1.0", index2=END)}
""")


btn = Button(master=app, text="Imprimir", command=showdata)
btn.place(x=110, y=290, width=70, height=30)

app.mainloop()
document_txt.close()
