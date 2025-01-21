from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def inserir():
    if var_id.get() == "" or var_nome.get() == "" or var_fone.get() == "":
        messagebox.showerror(title="Blank Space", message="Não deixe caixas de entrada em branco")
    else:
        tw.insert("", "end", values=(var_id.get(), var_nome.get(), var_fone.get()))
        var_id.delete(0, END)
        var_nome.delete(0, END)
        var_fone.delete(0, END)


def deletar():
    try:
        itemselecionado = tw.selection()[0]
        tw.delete(itemselecionado)
    except:
        messagebox.showinfo(title="ERRO", message="Selecione os dados a serem excluídos")


def obter():
    try:
        itemselecionado = tw.selection()[0]
        valores = tw.item(itemselecionado, "values")
        for item_tw in valores:
            print(item_tw, end=" ")
        print()
    except:
        messagebox.showinfo(title="ERRO", message="Selecione o elemento a ser obtido")


app = Tk()
app.title("Fernando TreeView")
app.configure(bg="#efede9")
app.geometry("400x300")

label1 = Label(app, text="ID", anchor=W)
var_id = Entry(app)
label2 = Label(app, text="NOME", anchor=W)
var_nome = Entry(app)
label3 = Label(app, text="TELEFONE", anchor=W)
var_fone = Entry(app)

tw = ttk.Treeview(app, columns=("id", "nome", "fone"), show="headings")
tw.column("id", minwidth=0, width=50)
tw.column("nome", minwidth=0, width=250)
tw.column("fone", minwidth=0, width=100)
tw.heading("id", text="ID")
tw.heading("nome", text="NOME")
tw.heading("fone", text="TELEFONE")

btn_insert = Button(app, text="Inserir", command=inserir)
btn_delete = Button(app, text="Deletar", command=deletar)
btn_obter = Button(app, text="Obter", command=obter)

label1.grid(column=0, row=0, sticky="w")
label2.grid(column=1, row=0, sticky="w")
label3.grid(column=2, row=0, sticky="w")

var_id.grid(column=0, row=1, sticky="w")
var_nome.grid(column=1, row=1, sticky="w")
var_fone.grid(column=2, row=1, sticky="w")

tw.grid(column=0, row=2, columnspan=3)

btn_insert.grid(column=0, row=3)
btn_delete.grid(column=1, row=3)
btn_obter.grid(column=2, row=3)

app.mainloop()
