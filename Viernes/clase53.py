import tkinter

v=tkinter.Tk()
varForm=tkinter.IntVar()
opc=["aaron","casar","angel","saul","mario","gerson","alejandro","israel","marco","marcelo"]
tkinter.Label(v,text="elija un nombre").pack()
for i  in range(len(opc)):
    tkinter.Radiobutton(v,text=opc[i],value=i,variable=varForm).pack()
