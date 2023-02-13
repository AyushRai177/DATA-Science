from turtle import *

pencolor("blue")
fillcolor("red")
speed("fastest")
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    left(25)
    end_fill()

hideturtle()
mainloop()