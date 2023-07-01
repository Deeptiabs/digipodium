from turtle import *

speed('fast')

for i in range (6):
    pencolor('violet')
    fd(50)
    for i in range(6):
        pencolor('red')
        fd(50)
        for i in range(6):
            pencolor('green')
            fd(25)
            lt(360/4)
    lt(360/4)
lt(360/4)

mainloop()



