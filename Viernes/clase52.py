import tkinter
v=tkinter.Tk()
def darNombre():
    et["text"]="hola, "+varText.get()




v.title("interfaz")
et=tkinter.Label(v,text="hola mundo")
et.pack()
b=tkinter.Button(v,text="ver nombre",command=darNombre)
b.pack(side=tkinter.RIGHT)
varText=tkinter.StringVar()
varText.set("ejemplo")
ent=tkinter.Entry(v,textvariable=varText)
ent.pack()
v.mainloop()
