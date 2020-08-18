import turtle

#Ventana
wn = turtle.Screen()
wn.title ('Ping Pong By Johana')
wn.bgcolor ("black")
wn.setup(width = 800, height= 600)
wn.tracer(0)

#Marcador
marcadorA =0
marcadorB =0

#JugadorA
JugadorA = turtle.Turtle()
JugadorA.speed(0)
JugadorA.shape("square")
JugadorA.color("blue")
JugadorA.penup()
JugadorA.goto (0,290)
JugadorA.shapesize(stretch_wid=1,stretch_len=5)

#JugadorB
JugadorB = turtle.Turtle()
JugadorB.speed(0)
JugadorB.shape("square")
JugadorB.color("red")
JugadorB.penup()
JugadorB.goto (0,-280)
JugadorB.shapesize(stretch_wid=1,stretch_len=5)

#Pelota
Pelota = turtle.Turtle()
Pelota.speed(0)
Pelota.shape("circle")
Pelota.color("white")
Pelota.penup()
Pelota.goto (0,0)
Pelota.dx = 0.3
Pelota.dy = 0.3

#DIVISIÓN
Division = turtle.Turtle()
Division.color("white")
Division.goto (-410,0)
Division.goto (410,0)

#Pen

Pen1 = turtle.Turtle()
Pen1.speed (0)
Pen1.color("blue")
Pen1.penup()
Pen1.goto(330,275)


Pen2 = turtle.Turtle()
Pen2.speed (0)
Pen2.color("red")
Pen2.penup()
Pen2.goto(-330,-275)


#Funciones
def jugadorA_right():
    x = JugadorA.xcor()
    x += 20
    JugadorA.setx(x)

def jugadorA_left():
    x = JugadorA.xcor()
    x -= 20
    JugadorA.setx(x)

def jugadorB_right():
    x = JugadorB.xcor()
    x += 20
    JugadorB.setx(x)

def jugadorB_left():
    x = JugadorB.xcor()
    x -= 20
    JugadorB.setx(x)    

# Teclado
wn.listen()
wn.onkeypress(jugadorA_right,"D")  
wn.onkeypress(jugadorA_left,"A") 
wn.onkeypress(jugadorA_right,"d")  
wn.onkeypress(jugadorA_left,"a") 
wn.onkeypress(jugadorB_right,"Right")  
wn.onkeypress(jugadorB_left,"Left") 







while True:
    wn.update()

    Pelota.setx(Pelota.xcor() + Pelota.dx)
    Pelota.sety(Pelota.ycor() + Pelota.dy)

    #Bordes
    if Pelota.xcor () > 380:
        Pelota.dx *= -1
    if Pelota.xcor () < (-380):
        Pelota.dx *= -1    

    #Bordes derecha/Izquierda
    if Pelota.ycor() > 290:
        Pelota.goto(0,0) 
        Pelota.dy *= -1
        marcadorB += 1
        Pen2.clear()
        Pen2.write("Jugador A: {} ".format(marcadorB), align= "center", font=("Curier",16, "normal"))
        
    if Pelota.ycor() < -290:
        Pelota.goto(0,0) 
        Pelota.dy *= -1 
        marcadorA += 1 
        Pen1.clear()
        Pen1.write("Jugador B: {} ".format(marcadorA), align= "center", font=("Curier",16, "normal"))    

    if  ((Pelota.ycor() > 270 and Pelota.ycor () < 290 )
            and (Pelota.xcor() < JugadorA.xcor() + 50
            and  Pelota.xcor() > JugadorA.xcor() - 50)):
        Pelota.dy *= -1    

    if  ((Pelota.ycor() < -270 and Pelota.ycor () > -290 )
            and (Pelota.xcor() < JugadorB.xcor() + 50
            and  Pelota.xcor() > JugadorB.xcor() - 50)):
        Pelota.dy *= -1 

