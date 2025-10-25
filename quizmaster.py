import pgzrun

WIDTH = 1000
HEIGHT = 600

marqueebox = Rect(0,0,1000,90)

def draw():
    screen.fill("red")
    screen.draw.filled_rect(marqueebox,"pink")
pgzrun.go()