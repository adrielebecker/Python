import turtle

pen = turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def Desenho():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

def nome():
    pen.up()
    pen.setpos(-60, 80)
    pen.down()
    pen.color('black')
    pen.write('Adriele Becker', font=("arial", 10, "normal"))

Desenho()
nome()
pen.ht()
turtle.done()