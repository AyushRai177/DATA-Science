from turtle import *

speed('fastest')

side=10
size=50
pencolor("blue")

# crate a hexagon
for i in range(side):
    forward(size)
    left(360/6)
    write(i)
hideturtle() #hide turtle
mainloop() #keepwindow open