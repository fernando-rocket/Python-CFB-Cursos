from tkinter import *

app = Tk()
app.title("Fernando Label")
app.geometry("500x500")
app.configure(bg="#efede9")

main_frame = Frame(app, borderwidth=1, relief="solid", background="white")
main_frame.place(x=0, y=0, width=300, height=300)

main_label = Label(main_frame, text="Fernando Gois", bg="#efede9", fg="blue", font=("Arial", 12))
main_label.pack(side=LEFT, fill=X, expand=True)

app.mainloop()
