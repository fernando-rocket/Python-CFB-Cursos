from tkinter import *
from tkinter import messagebox


def app_fernando():
    def showmsg():
        if var_typeOfmsg.get() == "1":
            messagebox.showinfo(title="CFB Cursos", message="info")
        elif var_typeOfmsg.get() == "2":
            messagebox.showwarning(title="CFB Cursos", message="error")
        elif var_typeOfmsg.get() == "3":
            messagebox.showerror(title="CFB Cursos", message="warning")
            app.quit()
        else:
            print("Erro. tiposmsg não se enquadra em nenhuma das opções*[1,2,3]*")

    app = Tk()
    app.title("MSG Fernando")
    app.configure(bg="#efede9")
    app.geometry("500x500")

    # MessageBox com info, error e warning ------------------------------------------
    var_typeOfmsg = StringVar()
    var_typeOfmsg.set("1")
    Radiobutton(app, text="Info", value="1", variable=var_typeOfmsg).pack()
    Radiobutton(app, text="Error", value="2", variable=var_typeOfmsg).pack()
    Radiobutton(app, text="Warning", value="3", variable=var_typeOfmsg).pack()
    btn = Button(app, text="Show Message", command=showmsg)
    btn.pack()

    app.mainloop()


def showapp():
    res = messagebox.askyesno(title="Resetar", message="Confirma reset do textbox?")
    if res == True:
        app_fernando()
    else:
        print("OK")


showapp()
