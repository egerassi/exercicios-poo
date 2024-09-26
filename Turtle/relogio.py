import turtle
import math

con = turtle.Turtle()

con.width(3)
con.circle(100)

con.up()
con.left(90)
con.forward(100)
con.down()

for i in range(12):
    con.up()
    con.forward(90)
    con.down()
    con.dot()
    con.up()
    con.left(180)
    con.forward(90)
    con.left(150)
    
con.down()

def ponteiro(angulo, grossura, cor, comprimento):
    con.left(angulo)
    con.width(grossura)
    con.color(cor)
    con.forward(comprimento)
    con.up()
    con.right(180)
    con.forward(comprimento)
    con.left(180-angulo)
    con.down()
    
ponteiro(50, 4, 'Black', 50)

ponteiro(275, 3, 'Black', 72)

ponteiro(8, 2, 'Red', 85)

con.hideturtle()
turtle.done()



