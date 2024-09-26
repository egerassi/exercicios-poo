import turtle

construtor = turtle.Turtle()

x= 40

construtor.left(180)

for i in range(302):
    construtor.right(91)
    construtor.forward(x)
    x += 1
    
turtle.done()