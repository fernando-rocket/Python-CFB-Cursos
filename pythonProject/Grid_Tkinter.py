from tkinter import *

app = Tk()
app.title("Fernando Griddy")
app.geometry("500x500")
app.configure(bg="#efede9")

lb_canal = Label(app, text="CFB Cursos")
lb_nome = Label(app, text="Digite seu nome")
lb_idade = Label(app, text="Informe sua idade")

et_nome = Entry(app)
et_idade = Entry(app)

btn = Button(app, text="Youtube")

lb_canal.grid(column=0, row=0, columnspan=2)
lb_nome.grid(column=0, row=1, sticky='w')
lb_idade.grid(column=0, row=2, sticky='w')

et_nome.grid(column=1, row=1, padx=10)
et_idade.grid(column=1, row=2)

btn.grid(column=0, row=3, columnspan=2)

app.mainloop()
