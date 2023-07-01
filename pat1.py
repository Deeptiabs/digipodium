from turtle import *
speed('fastest')

for i in range(6):
    fd(100)
    lt(360/5)
    for i in range(6):
        fd(50)
        lt(360/5)

mainloop()