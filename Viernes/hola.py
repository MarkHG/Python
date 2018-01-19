import Tkinter #Version 2.7
def darNombre():
    et["text"] = "Hola, " + varText.get()

v = Tkinter.Tk()
v.title("Interfaz")
et = Tkinter.Label(v, text = "Hola Mundo")
et.pack(side = Tkinter.RIGHT)
b = Tkinter.Button(v,text = "Ver nombre", command = darNombre)
b.pack(side = Tkinter.RIGHT)
varText = Tkinter.StringVar()
varText.set("Ejemplo")
ent = Tkinter.Entry(v, textvariable = varText)
ent.pack(side = Tkinter.RIGHT)
v.mainloop()
v.mainloop()
