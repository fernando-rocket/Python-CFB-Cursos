from tkinter import *

app = Tk()
app.title("Label FFrame")
app.geometry("400x400")
app.configure(bg="#efede9")

label_esportes = LabelFrame(app, text="Fernando", borderwidth=1, relief="solid")
label_esportes.place(x=10, y=10, width=300, height=100)

inside_label = Label(label_esportes, text="Srmukznc", bg="black", fg="white")
inside_label.pack(side=TOP, expand=True, fill=Y)
inside_label2 = Label(label_esportes, text="Srmukznc", bg="black", fg="white")
inside_label2.pack(side=TOP, expand=True, fill=Y)

app.mainloop()
