from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

caminho = "C:/Users/Fernando/Documents"

fefe = "C:/Users/Fernando/Documents/code/fefe.jpg"


def mp(mm):
    return mm / 0.352777


def criarpdf():
    if os.path.exists(caminho+"\\cfbcursos.pdf"):
        print("PDF Existente")
    else:
        cnv = canvas.Canvas(caminho+"\\cfbcursos.pdf", pagesize=A4)
        cnv.drawImage(fefe, x=mp(80), y=mp(80))
        cnv.drawImage(fefe, x=mp(120), y=mp(80), width=100, height=100)
        cnv.drawImage(fefe, x=mp(160), y=mp(80), width=200, height=200)
        cnv.drawString(mp(160), mp(50), "CfbCursos")
        cnv.circle(x_cen=mp(50), y_cen=mp(120), r=mp(10))
        cnv.save()
        print("PDF Criado")


def deletarpdf():
    try:
        os.remove(caminho+"\\cfbcursos.pdf")
        print("PDF Deletado")
    except:
        print("PDF Inexistente")


app = Tk()
app.title("Fernando PDF")
app.geometry("600x450")

btn = Button(app, text="Criar PDF", command=criarpdf)
btn.pack(side=LEFT, padx=10)

btn2 = Button(app, text="Deletar PDF", command=deletarpdf)
btn2.pack(side=RIGHT, padx=10)

app.mainloop()
