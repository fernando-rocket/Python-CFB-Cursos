from tkinter import *

print(x)
def appFunc():
    def deletar():
        nome.delete(0, END)
    app = Tk()
    app.title("FForms")
    app.configure(bg="#dde")
    app.geometry("500x500")

    nome = Entry(app)
    nome.place(x=10, y=10, width=100, height=30)

    btn = Button(app, text="DELETAR", command=deletar)
    btn.place(x=10, y=50, width=100, height=30)

    app.mainloop()


appFunc()
