import turtle
import time

pen = turtle.Turtle()
turtle.Screen().bgcolor('#545454')

def BottomDrawing():
    pen.color('#545454')
    pen.sety(-100)
    pen.color('#FFFF00')
    pen.circle(100)
    pen.color('#545454')
    pen.sety(-70)
    pen.color('#FFFF00')
    pen.circle(70)

def UpDrawing():
    pen.color('#545454')
    pen.setpos(-70,170)
    pen.color('#00FEFE')
    pen.fillcolor('#00FEFE')
    pen.begin_fill()
    pen.left(45)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.end_fill()

def Message():
    pen.color('#545454')
    pen.setpos(-40,-150)
    pen.color('#8cbfaf')
    pen.write('Te amo', font=('Arial', 18, 'normal'))

def Shape():
    BottomDrawing()
    UpDrawing()
    Message()    
    pen.ht()
    turtle.done()

Shape()    
