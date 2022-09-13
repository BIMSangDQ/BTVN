import turtle

t=turtle.Turtle()
t.shape('turtle')

def Goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def Draw_Arc(r,rad,rotate_turtle,color):
    t.setheading(0)
    t.left(rotate_turtle)
    t.circle(r,rad)

t.speed(10)

#Bao
Goto(0,75)
t.fillcolor('yellow')
t.begin_fill()
Draw_Arc(80,30,180,'black')
Draw_Arc(25,60,-160,'black')
Draw_Arc(145,13,-104,'black')
Draw_Arc(30,55,-127,'black')
Draw_Arc(16,48,-69,'black')
Draw_Arc(98,69,-34,'black')
Draw_Arc(16,48,21,'black')
Draw_Arc(30,55,72,'black')
Draw_Arc(145,13,91,'black')
Draw_Arc(25,60,99,'black')
Draw_Arc(80,30,150,'black')
t.end_fill()

#Ma trai
Goto(-33.8,-9)
t.fillcolor('orange')
t.begin_fill()
Draw_Arc(15,360,90,'black')
t.end_fill()

#Ma phai
Goto(63.8,-9)
t.fillcolor('orange')
t.begin_fill()
Draw_Arc(15,360,90,'black')
t.end_fill()

#luoi
Goto(-15,0)
t.fillcolor('red')
t.begin_fill()
Draw_Arc(62,18,-90,'black')
Draw_Arc(12,143,-72,'black')
Draw_Arc(62,18,70,'black')
t.end_fill()

#Mieng
Goto(-22,0)
t.width(2)
t.fillcolor('yellow')
t.begin_fill()
Draw_Arc(15,94,-47,'black')
Draw_Arc(15,94,-47,'black')
t.end_fill()

#Mat trai
Goto(-24,20)
t.width(1)
t.fillcolor('black')
t.begin_fill()
Draw_Arc(11,360,90,'black')
t.end_fill()

Goto(-27,25)
t.width(1)
t.fillcolor('white')
t.begin_fill()
Draw_Arc(3.6,360,90,'white')
t.end_fill()

#Mat phai
Goto(46,20)
t.width(1)
t.fillcolor('black')
t.begin_fill()
Draw_Arc(11,360,90,'black')
t.end_fill()

Goto(34,25)
t.width(1)
t.fillcolor('white')
t.begin_fill()
Draw_Arc(3.6,360,90,'black')
t.end_fill()

#Tai trai
Goto(-39,65)
t.fillcolor('yellow')
t.begin_fill()
Draw_Arc(44,68,113,'black')
Draw_Arc(38,81,-99,'black')
t.end_fill()

Goto(-65,89)
t.fillcolor('black')
t.begin_fill()
Draw_Arc(44,21,160,'black')
Draw_Arc(38,54,-99,'black')
t.end_fill()

#Tai phai
Goto(54,50)
t.fillcolor('yellow')
t.begin_fill()
Draw_Arc(38,81,18,'black')
Draw_Arc(44,68,179,'black')
t.end_fill()

Goto(70,59)
t.fillcolor('black')
t.begin_fill()
Draw_Arc(38,54,45,'black')
Draw_Arc(44,21,179,'black')
t.end_fill()

#mui
Goto(0,0)
t.fillcolor('black')
t.begin_fill()
t.goto(4,4)
t.goto(-4,4)
t.goto(0,0)
t.end_fill()

t.hideturtle()

turtle.done()