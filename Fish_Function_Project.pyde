from random import*
def setup():
    size(700,700)
    background(14,103,158)
    #randint
    f = 1
    while f <= 50:
        fish(randint(10,700),randint(10,700),255,randint(0,200),randint(170,240),-10 )
        f += 1
        
    
def fish (x,y,red_color,green_color,blue_color,x_speed): 
    #prints family crest at x,y
    fish_width = randint(50,100)
    fish_height = randint(40,50)
    x1 = x +fish_width/2
    x2 = x +(fish_width/2) +10
    y2 = y - 20
    y3 = y + 20
    x_speed = 10
    fill (red_color, green_color, blue_color)
    ellipse (x,y,fish_width,randint(40,50))
    triangle (x1,y,x2,y2,x2,y3)
    #make the fish move
    if x <= 700:
        x = x - x_speed
        x1 = x1 - x_speed
        x2 = x2 - x_speed
    

    # def setup():
    #     x = randint(10,700)
    #     y = randint(10,700)
    #     x1 = x +fish_width/2
    #     x2 = x +(fish_width/2) +10
    #     y2 = y - 20
    #     y3 = y + 20
    #     red_color = 255
    #     green_color = randint(0,150)
    #     blue_color = randint(170,240)
    #     fish_width = randint(50,100)
    #     fish_height = randint(40,50)
    #     x_speed = randint(0,15)
        
