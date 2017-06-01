from tkinter import*
import math
import time
import random
import threading

#VARIABLES#
i = 300
j = 500
k = 1100
l = 500
t = random.randint(160, 625)
y = 20
g = random.randint(860, 1325)
h = 20
presionar = False
x = None

def vent():
    "Funcion que destruye la ventana menú y abre la del juego"
    global menu
    menu.destroy()
    pista()

def pista():
    "Crea la pista con el nombre y el puntaje de cada jugador, almacena los contadores y las imagenes para cargarlas junto con los carros"    
    global ventana, nombre, nombre1, c, fondo, carro, tecla,carrito, fondo1, fondo2
    global score, puntos, x, i, j, k, l, fondo3, fondo4, z, t, y, g, h, e, e1
    global enemigo, crash, cont, contG, dif
    ventana = Tk()
    c = Canvas(ventana, width = 1500, height = 600)
    fondo = PhotoImage(file="Pista.png")
    fondo1 = c.create_image(400,200, image = fondo)
    fondo2 = c.create_image(400,-470, image = fondo)
    fondo3 = c.create_image(1100,200, image = fondo)
    fondo4 = c.create_image(1100,-470, image = fondo)
    score = 0
    cont = 50
    dif = 20
    contG = 0
    name = Label(ventana, text=nombre.get(), font="Arial", fg="red")
    name.place(x=350, y=5)
    name1 = Label(ventana, text=nombre1.get(), font="Arial", fg="red")
    name1.place(x=1050, y=5)
    carro = PhotoImage(file = "carrito1.png")
    enemigo = PhotoImage(file = "enemigo.png")
    crash = PhotoImage(file = "crash.png")
    x = c.create_image(i, j, image = carro)
    z = c.create_image(k, l, image = carro)
    e = c.create_image(t, y, image = enemigo)
    e1 = c.create_image(g, h, image = enemigo)
    print (carro.width(), carro.height())
    print (enemigo.width(), enemigo.height())
    moverpista()
    save = Button(ventana, text="Salvar", font="Arial", command=guardar).place(x=700, y=20)
    ventana.bind('<d>', derecha)
    ventana.bind('<a>', izquierda)
    ventana.bind('<l>', derecha1)
    ventana.bind('<j>', izquierda1)
    c.pack()

def pistaCargada():
    "Crea la pista con el nombre y el puntaje de cada jugador guardados en la partida anterior"    
    global ventana, nombre, nombre1, c, fondo, carro, tecla,carrito, fondo1, fondo2
    global score, puntos, x, i, j, k, l, fondo3, fondo4, z, t, y, g, h, e, e1
    global enemigo, crash, cont, contG, dif
    menu.destroy()
    a = open("partidas.txt","r")
    nombre = a.readline()
    nombre1 = a.readline()
    score = int(a.readline().strip())
    i = int(a.readline().strip())
    j = int(a.readline().strip())
    k = int(a.readline().strip())
    l = int(a.readline().strip())
    ventana = Tk()
    c = Canvas(ventana, width = 1500, height = 600)
    fondo = PhotoImage(file="Pista.png")
    fondo1 = c.create_image(400,200, image = fondo)
    fondo2 = c.create_image(400,-470, image = fondo)
    fondo3 = c.create_image(1100,200, image = fondo)
    fondo4 = c.create_image(1100,-470, image = fondo)
    score = 0
    cont = 50
    dif = 20
    contG = 0
    name = Label(ventana, text=nombre, font="Arial", fg="red")
    name.place(x=350, y=5)
    name1 = Label(ventana, text=nombre1, font="Arial", fg="red")
    name1.place(x=1050, y=5)
    carro = PhotoImage(file = "carrito1.png")
    enemigo = PhotoImage(file = "enemigo.png")
    crash = PhotoImage(file = "crash.png")
    x = c.create_image(i, j, image = carro)
    z = c.create_image(k, l, image = carro)
    e = c.create_image(t, y, image = enemigo)
    e1 = c.create_image(g, h, image = enemigo)
    print (carro.width(), carro.height())
    print (enemigo.width(), enemigo.height())
    moverpista()
    save = Button(ventana, text="Salvar", font="Arial", command=guardar).place(x=700, y=20)
    ventana.bind('<d>', derecha)
    ventana.bind('<a>', izquierda)
    ventana.bind('<l>', derecha1)
    ventana.bind('<j>', izquierda1)
    a.close()
    c.pack()

def derecha(event):
    "Mueve el carro hacia la derecha"
    global presiono,i,j,carro, carrito, c,x
    if (i<625):
        c.delete(x)
        i = i + 10
        x = c.create_image(i,j,image=carro)
    elif(i >= 625):
        c.delete(x)
        i = i - 10
        x = c.create_image(i,j,image=carro)

def derecha1(event):
    "Mueve el carro hacia la derecha"
    global k,l,carro, carrito, c,z
    if (k<1325):
        c.delete(z)
        k = k + 10
        z = c.create_image(k,l,image=carro)
    elif(k >= 1325):
        c.delete(z)
        k = k - 10
        z = c.create_image(k,l,image=carro)

def izquierda1(event):
    "Mueve el carro hacia la derecha"
    global k,l,carro, carrito, c,z
    if (k>860):
        c.delete(z)
        k = k - 10
        z = c.create_image(k,l,image=carro)
    elif(k <= 860):
        c.delete(z)
        k = k + 10
        z = c.create_image(k,l,image=carro)
        
def izquierda(event):
    "Mueve el carro hacia la izquierda"
    global presiono,i,j,carro, carrito, x
    if (i>160):
        c.delete(x)
        i = i - 5
        x = c.create_image(i,j,image=carro)
    elif(i <= 160):
        c.delete(x)
        i = i + 5
        x = c.create_image(i,j,image=carro)

def moverpista():
    "Mueve la pista para generar el efecto de movimiento, junto con los carros enemigos"
    global i, x, j, c, k, l, fondo, fondo1, fondo2, fondo3, fondo4, score, puntos, z
    global enemigo, e, e1, t, y, g, h, cont, contG, dif
    c.move(fondo1,0,dif)
    c.move(fondo2,0,dif)
    c.move(fondo3,0,dif)
    c.move(fondo4,0,dif)
    c.move(e, 0, dif)
    c.move(e1, 0, dif)
    choque()
    if(c.coords(fondo1)[1]>=1100 or c.coords(fondo2)[1]>=1100):
        c.delete(fondo1)
        fondo1=c.create_image(400,-460,image=fondo)
        c.delete(fondo2)
        fondo2=c.create_image(400,200,image=fondo)
        c.delete(fondo3)
        fondo3 = c.create_image(1100,200, image = fondo)
        c.delete(fondo4)
        fondo4 = c.create_image(1100,-460, image = fondo)
        c.delete(x)
        c.delete(z)
        t = random.randint(160, 625)
        g = random.randint(860, 1325)
        x = c.create_image(i,j,image=carro)
        z = c.create_image(k,l,image=carro)
        e = c.create_image(t, y, image = enemigo)
        e1 = c.create_image(g, h, image = enemigo)
    if (cont == 0):
        over = Button(ventana, text="¡¡LOS CARROS SE QUEDARON SIN GASOLINA!!", font="Arial", command=fin).place(x=500, y=350)
        c.after(100, 100)
    if (contG >= 1000  ):
        cont = cont + 45
        contG = 0
    dif = dif + 0.05
    score = score + 2
    cont = cont - 0.08
    contG = contG + 2
    puntos = Label(ventana, text="Puntos: " + str(score), font="Arial", fg="red")
    gasolina = Label(ventana, text="gasolina: " + str(int(cont)), font="Arial", fg="red")
    gasolina.place(x=700, y=85)
    puntos.place(x=700, y=60)
    c.delete(gasolina)
    c.after(100, moverpista)


def choque():
    "Funcion que detecta el choque y para el juego inmediatamente"
    global c, x, e, z, e1, i, j, k, l, ventana, crash
    a0 = (c.coords(x)[0], c.coords(x)[1]) 
    b0 = (c.coords(e)[0], c.coords(e)[1]) 
    a1 = (c.coords(z)[0], c.coords(z)[1])
    b1 = (c.coords(e1)[0], c.coords(e1)[1])
    if(math.fabs(a0[0] - b0[0]) <= 39 and math.fabs(a0[1] - b0[1]) <= 74):
        print ("entre")
        over = Button(ventana, text="Player2 Win", font="Arial", command=fin).place(x=250, y=250)
        c.delete(x)
        c.delete(e)
        boom = c.create_image(i, j, image = crash)
        c.after(100, 100)
    if(math.fabs(a1[0] - b1[0]) <= 39 and math.fabs(a1[1] - b1[1]) <= 74):
        print ("entre")
        over = Button(ventana, text="Player1 Win", font="Arial", command=fin).place(x=1000, y=250)
        c.delete(z)
        c.delete(e1)
        boom = c.create_image(k, l, image = crash)
        c.after(100, 100)

def fin():
    "Funcion para salir del juego en caso de que alguno de los dos jugadores gane o se les acabe la gasolina"
    global ventana
    ventana.destroy()
    
def guardar():
    "Guarda los datos en un archivo de texto"
    global nombre, score, i, j,x 
    a = open("partidas.txt", "w")
    a.write(str(nombre.get()) +"\n")
    a.write(str(nombre1.get()) +"\n")
    a.write(str(score)+"\n")
    a.write(str(i)+"\n")
    a.write(str(j)+"\n")
    a.write(str(k)+"\n")
    a.write(str(l)+"\n")
    a.close()

def ins():
    "Muestra las instrucciones en pantalla"
    global botones
    inst = Tk()
    inst.title("Instrucciones")
    inst.resizable(0, 0)
    inst.geometry("550x300")
    q = Canvas(menu, width=550, height = 300)
    q.pack(fill="none")
    botones = PhotoImage(file = "ins.png")
    q.create_image(250, 150, image = botones)
    back = Button(q, text= "Back", font ="Arial", command = menu).place(x=200, y=10)
    

#MENU
"Menu de inicializacion"
def menu():
    global menu, nombre, nombre1
    menu = Tk()
    menu.title("Cars")
    menu.resizable(0, 0)
    menu.geometry("550x300")
    m = Canvas(menu, width=550, height = 300)
    m.pack(fill="none")
    fondo = PhotoImage(file = "mcarro.png")
    m.create_image(250,150, image = fondo)
    nombre = StringVar()
    nombre.set("Jugador1:")
    nombre1 = StringVar()
    nombre1.set("Jugador2:")
    jugador = Entry(menu, textvariable = nombre, font ="Arial").place(x=200, y=10)
    jugador1 = Entry(menu, textvariable = nombre1, font ="Arial").place(x=200, y=40)
    empezar = Button(menu, text="Jugar", font="Arial", command=vent).place(x=200, y=80)
    instru = Button(menu, text="instrucciones", font="Arial", command=ins).place(x=200, y=130)
    cargar = Button(menu, text="Cargar la ultima partida", font="Arial", command=pistaCargada).place(x=200, y=180)
    salir = Button(menu, text="Salir", font="Arial", command=exit).place(x=200, y=230)
    menu.mainloop()
menu()
