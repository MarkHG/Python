import Tkinter

v = Tkinter.Tk()
varFrom = Tkinter.IntVar()

opc =["Marcelo","Marco,Israel"]
Tkinter.Label(v, text = "Elija un nombre: ").pack()
for i in in range(len(opc)):
    Tkinter.Radiobutton(v, text = opc[i], value = i, variable = varForm).pack()
v.mainloop()
