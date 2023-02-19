import pgzrun
music.play('bg')

b=Rect((50,50),(100,50))
vx,vy=3,5 # global variable

def draw():
    screen.fill('black')
    screen.draw.filled_rect(b,'yellow')

def update():
    global vx,vy
    b.x +=vx
    b.y +=vy
    if b.right > 800 or b.left<0:
        vx=-vy
    if b.bottom >600 or b.top<0:
        vy=-vy

#outside of all function
pgzrun.go()