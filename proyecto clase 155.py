from tkinter import*
import random

root=Tk()
root.geometry("500x500")
root.config(bg="blue")

colores=["red","blue","purple","pink","yellow","brown"]

def fondo():
    a=random.randint(0, 5)
    root.config(bg=colores[a])
   

button_1=Button(root,text="Dame click",command=fondo)
button_1.place(relx=0.5 , rely=0.5 , anchor=CENTER)





root.mainloop()

