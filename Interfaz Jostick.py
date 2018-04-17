#===========================================================
# Creador por: William Aguirre Zapata
# Interfaz para el joystick de Arquitectura de PC 1
#===========================================================

import tkinter
from tkinter import messagebox

#--------------MENU COMPLETO---------
    
#Creacion del GUI
gui = tkinter.Tk()

#Titulo del GUI
gui.title("Interfaz Gráfico Joystick")

#Dimensiones
gui.geometry("960x614")

#Variables
x=None
y=None
z=None
w=None

a=None
b=None
c=None
d=None

#----------------TECLAS ---------------
h = [] 
def keyup(e):
    global h
    #print(e.keycode)
    if(e.keycode in h):
        h.pop(h.index(e.keycode))
        
def keydown(e):
    global h
    if not e.keycode in h:
        h.append(e.keycode)

def keyJuego():
    global h,x,y,z,w,a,b,c,d

    #DIRECCIONES-------------
    if(87 in h):
        canvas.delete(y)
        y = canvas.create_image(960/2,614/2,image=arriba)
    else:
        canvas.delete(y)

    if(83 in h):
        canvas.delete(x)
        x = canvas.create_image(960/2,614/2,image=abajo)
    else:
        canvas.delete(x)
        
    if(65 in h):
        canvas.delete(z)
        z = canvas.create_image(960/2,614/2,image=derecha)
    else:
        canvas.delete(z)
        
    if(68 in h):
        canvas.delete(w)
        w = canvas.create_image(960/2,614/2,image=izquierda)
    else:
        canvas.delete(w)

    #BOTONES----------------------
    if(73 in h):
        canvas.delete(a)
        a = canvas.create_image(960/2,614/2,image=barriba)
    else:
        canvas.delete(a)

    if(75 in h):
        canvas.delete(b)
        b = canvas.create_image(960/2,614/2,image=babajo)
    else:
        canvas.delete(b)
        
    if(76 in h):
        canvas.delete(c)
        c = canvas.create_image(960/2,614/2,image=bderecha)
    else:
        canvas.delete(c)
        
    if(74 in h):
        canvas.delete(d)
        d = canvas.create_image(960/2,614/2,image=bizquierda)
    else:
        canvas.delete(d)
        
    canvas.after(10,keyJuego)

#--------------WIDGETS------------------
canvas = tkinter.Canvas(gui,width=960,height=614)

# Pone el foco en el canvas
canvas.focus_set()

# Empaqueta (muestra) los widgets
canvas.pack()
keyJuego()
canvas.bind("<KeyPress>", keydown)#Liga el evento key al canvas
canvas.bind("<KeyRelease>", keyup)

#------------MONTAR IMAGENES--------
fondo1 = tkinter.PhotoImage(file="img/control.png")
arriba = tkinter.PhotoImage(file="img/arriba.png")
abajo = tkinter.PhotoImage(file="img/abajo.png")
derecha = tkinter.PhotoImage(file="img/derecha.png")
izquierda = tkinter.PhotoImage(file="img/izquierda.png")
barriba = tkinter.PhotoImage(file="img/barriba.png")
babajo = tkinter.PhotoImage(file="img/babajo.png")
bderecha = tkinter.PhotoImage(file="img/bderecho.png")
bizquierda = tkinter.PhotoImage(file="img/bizquierdo.png")

#-------------------CARGAR IMAGENES-----------------------------------------
canvas.create_image(960/2,614/2,image=fondo1)

gui.mainloop()
