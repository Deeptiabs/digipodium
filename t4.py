from turtle import *

#definition declaration
def square(size,color='red'):
    fillcolor(color)
    for i in range(4):
        fd(size)
        rt(90)
    end_fill()

def hexagon(size):
    for i in range(6):
        fd(size)
        rt(60)

square(100,'blue')
square(50,'green')
hexagon(100)
hexagon(50)
square(25,'yellow') 

mainloop()

