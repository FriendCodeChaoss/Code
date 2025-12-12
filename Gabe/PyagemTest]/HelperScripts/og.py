from cmu_graphics import *

###starting scene 
#background
sky = Rect(0, 0, 400, 250, fill=gradient(rgb(255, 69, 0), rgb(255, 165, 0), rgb(255, 160, 122), rgb(255, 105, 180), rgb(150, 0, 150), start='bottom'))
sun = Group(
    Circle(200, 220, 40, fill=gradient(rgb(255, 255, 255), rgb(255, 255, 255), rgb(255, 255, 100))),
)
background = Group(
    Rect(0, 250, 400, 150, fill=gradient(rgb(255, 40, 0), rgb(255, 165, 0), start='top')),
    Polygon(0, 300, 400, 330, 400, 550, 0, 550, fill=gradient(rgb(120, 20, 0), rgb(255, 70, 0), start='bottom')),
    #left clouds
    Oval(100, 235, 200, 20, fill=gradient(rgb(255, 90, 0), rgb(255, 10, 0), rgb(220, 0, 0), start='left')),
    Oval(70, 70, 200, 100, fill=gradient(rgb(150, 0, 150), rgb(150, 0, 150), rgb(255, 135, 180), rgb(255, 160, 122), start='top')),
    Oval(250, 200, 70, 30, fill=gradient(rgb(255, 10, 0), rgb(255, 100, 0), start='left')),
    Oval(270, 100, 100, 60, fill=gradient(rgb(250, 165, 140), rgb(255, 127, 80), start='top')),
    Oval(370, 125, 200, 70, fill=gradient(rgb(255, 160, 122), rgb(255, 127, 80), rgb(255, 165, 0), start='top')),
    Oval(300, 50, 400, 100, fill=gradient(rgb(150, 0, 150), rgb(150, 0, 150), rgb(255, 135, 180), rgb(255, 160, 122), start='top')),
)

tree = Group(
    Polygon(-20, 350, 20, 350, 150, 150, 170, 100, 135, 150, fill=gradient(rgb(227, 60, 0), rgb(180, 50, 0), rgb(50, 0, 0), start='bottom')),
    Polygon(170, 100, 150, 150, 170, 230, 180, 150, fill=gradient(rgb(100, 100, 70), rgb(180, 50, 0), start='top')),
    Polygon(170, 100, 190, 140, 230, 180, 220, 130, fill=gradient(rgb(100, 100, 70), rgb(180, 50, 0), start='top')),
    Polygon(170, 100, 140, 150, 70, 210, 105, 140, fill=gradient(rgb(100, 100, 70), rgb(180, 50, 0), start='top')),
    Polygon(170, 100, 105, 130, 60, 130, 105, 100, fill=gradient(rgb(100, 100, 70), rgb(120, 80, 40), rgb(180, 50, 0), start='right-top')),
)

###chef
#rotations
f = Oval(170, 270, 50, 30, fill=rgb(50, 30, 0))
f.rotate(-20, 170, 270)
a = Oval(150, 220, 30, 50, fill=rgb(50, 30, 0))
a.rotate(-45, 150, 220)
b = Oval(250, 220, 30, 50, fill=rgb(50, 30, 0))
b.rotate(45, 250, 220)
h = Oval(230, 270, 50 , 30, fill=rgb(50, 30, 0))
h.rotate(20, 230, 270)
e = Oval(170, 270, 40, 20, fill=rgb(255, 255, 230))
e.rotate(-20, 170, 270)
g = Oval(230, 270, 40 , 20, fill=rgb(255, 255, 230))
g.rotate(20, 230, 270)
c = Oval(150, 220, 20, 40, fill=rgb(255, 255, 230))
c.rotate(-45, 150, 220)
d = Oval(250, 220, 20, 40, fill=rgb(255, 255, 230))
d.rotate(45, 250, 220)
k = Rect(152, 208, 15, 30, fill=rgb(50, 30, 0))
k.rotate(-45, 154, 208)
l = Rect(233, 198, 15, 30, fill=rgb(50, 30, 0))
l.rotate(45, 233, 205)
i = Rect(158, 208, 5, 30, fill=rgb(139, 0, 0))
i.rotate(-45, 158, 208)
j = Rect(239, 205, 5, 30, fill=rgb(139, 0, 0))
j.rotate(45, 239, 205)

chef = Group(
    #spatula borders
    Line(140, 180, 140, 220, lineWidth=12, fill=rgb(50, 30, 0)),
    Line(130, 180, 150, 180, lineWidth=12, fill=rgb(50, 30, 0)),
    Line(130, 160, 150, 160, lineWidth=12, fill=rgb(50, 30, 0)),
    Line(132.5, 186, 132.5, 154, lineWidth=12, fill=rgb(50, 30, 0)),
    Line(147.5, 186, 147.5, 154, lineWidth=12, fill=rgb(50, 30, 0)),
    Line(140, 180, 140, 160, lineWidth=12, fill=rgb(50, 30, 0)),
    
    #spatula
    Line(140, 180, 140, 220, lineWidth=5, fill=rgb(180, 180, 180)),
    Line(130, 180, 150, 180, lineWidth=5, fill=rgb(180, 180, 180)),
    Line(130, 160, 150, 160, lineWidth=5, fill=rgb(180, 180, 180)),
    Line(132.5, 180, 132.5, 160, lineWidth=5, fill=rgb(180, 180, 180)),
    Line(147.5, 180, 147.5, 160, lineWidth=5, fill=rgb(180, 180, 180)),
    Line(140, 180, 140, 160, lineWidth=5, fill=rgb(180, 180, 180)),
    
    #borders
    Oval(215, 140, 40, 100, fill=rgb(50, 30, 0)),
    Oval(185, 140, 40, 100, fill=rgb(50, 30, 0)),
    Oval(200, 190, 100, 70, fill=rgb(50, 30, 0)),
    Circle(200, 180, 45, fill=rgb(50, 30, 0)),
    Oval(200, 240, 120, 100, fill=rgb(50, 30, 0)),
    f,
    a,
    b,
    h,
    
    #body
    Circle(200, 180, 40, fill=rgb(255, 255, 230)),
    Oval(215, 140, 30, 90, fill=rgb(255, 255, 230)),
    Oval(185, 140, 30, 90, fill=rgb(255, 255, 230)),
    Oval(200, 190, 90, 60, fill=rgb(255, 255, 230)),
    Oval(200, 240, 110, 90, fill=rgb(255, 255, 230)),
    
    #feets
    e,
    g,
    c,
    d,
    
    #face
    Circle(184, 173, 6, fill=rgb(50, 30, 0)),
    Circle(216, 173, 6, fill=rgb(50, 30, 0)),
    Oval(170, 185, 16, 12, fill=rgb(255, 192, 203)),
    Oval(230, 185, 16, 12, fill=rgb(255, 192, 203)),
    Line(194, 185, 194, 182, lineWidth=1),
    Line(206, 185, 206, 182, lineWidth=1),
    Line(194, 185, 206, 185, lineWidth=1),
    
    #apron
    k,
    l,
    Polygon(170, 220, 230, 220, 240, 275, 160, 275, fill=rgb(50, 30, 0)),
    Polygon(175, 225, 225, 225, 233, 270, 167, 270, fill=rgb(139, 0, 0)),
    i,
    j,
    
    
    #chef hat
    Rect(180, 110, 40, 40, fill=rgb(50, 30, 0)),
    Oval(200, 110, 40, 30, fill=rgb(50, 30, 0)),
    Oval(200, 150, 40, 30, fill=rgb(50, 30, 0)),
    Rect(185, 110, 30, 40, fill=rgb(139, 0, 0)),
    Oval(200, 110, 30, 20, fill=rgb(139, 0, 0)),
    Oval(200, 150, 30, 20, fill=rgb(120, 20, 0)),
    Line(190, 110, 190, 130, fill=rgb(120, 20, 0)),
    Line(200, 115, 200, 135, fill=rgb(120, 20, 0)),
    Line(210, 110, 210, 135, fill=rgb(120, 20, 0)),
)

###shop
shop = Group(
    #inside
    Rect(100, 100, 180, 100, fill=rgb(50, 30, 0)),
    Rect(105, 150, 170, 120, fill=gradient(rgb(100, 50, 0), rgb(250, 120, 0), start='left-bottom')),
        #utilities
    Rect(105, 105, 60, 40, fill=gradient(rgb(170, 170, 170), rgb(100, 100, 100), start='top')),
    Rect(110, 115, 50, 25, fill=gradient(rgb(119, 136, 153), rgb(119, 160, 180), start='left-bottom')),
    Line(135, 115, 140, 140, fill=rgb(119, 170, 190)),
    Line(145, 115, 150, 140, fill=rgb(119, 170, 190)),
    Rect(205, 105, 80, 40, fill=gradient(rgb(160, 160, 160), rgb(240, 240, 240), start='left-bottom')),
    Line(215, 115, 215, 105, fill=rgb(130, 130, 130)),
    
    chef,
    
    #front borders
    Polygon(25, 275, 25, 215, 45, 195, 355, 195, 350, 100, 380, 45, 380, 230, 335, 275, fill=rgb(50, 30, 0)),
    Rect(25, 95, 80, 130, fill=rgb(50, 30, 0)),
    Rect(275, 95, 80, 130, fill=rgb(50, 30, 0)),
    
    #shop
    Rect(30, 220, 300, 50, fill=gradient(rgb(100, 50, 0), rgb(200, 80, 0), start='bottom')),
    Polygon(30, 220, 330, 220, 350, 200, 50, 200, fill=gradient(rgb(210, 80, 0), rgb(250, 120, 0), start='bottom')),
    Polygon(330, 270, 330, 100, 375, 50, 375, 225, fill=gradient(rgb(100, 50, 0), rgb(200, 80, 0), rgb(220, 100, 0), rgb(255, 160, 0), start='bottom')),
    Rect(30, 100, 50, 120, fill=gradient(rgb(200, 80, 0), rgb(250, 120, 0), start='bottom')),
    Polygon(80, 100, 80, 220, 100, 200, 100, 100, fill=gradient(rgb(200, 80, 0), rgb(255, 160, 0), start='bottom')),
    Rect(280, 100, 50, 120, fill=gradient(rgb(200, 80, 0), rgb(250, 120, 0), start='bottom')),
    
    #top
    Polygon(10, 105, 35, 45, 380, 45, 355, 105, fill=rgb(50, 30, 0)),
    Polygon(20, 100, 65, 100, 85, 50, 40, 50, fill=rgb(140, 0, 0)),
    Polygon(65, 100, 105, 100, 125, 50, 85, 50, fill=rgb(255, 255, 230)),
    Polygon(105, 100, 145, 100, 165, 50, 125, 50, fill=rgb(140, 0, 0)),
    Polygon(145, 100, 185, 100, 205, 50, 165, 50, fill=rgb(255, 255, 230)),
    Polygon(185, 100, 225, 100, 245, 50, 205, 50, fill=rgb(140, 0, 0)),
    Polygon(225, 100, 265, 100, 285, 50, 245, 50, fill=rgb(255, 255, 230)),
    Polygon(265, 100, 305, 100, 325, 50, 285, 50, fill=rgb(140, 0, 0)),
    Polygon(305, 100, 350, 100, 370, 50, 325, 50, fill=rgb(255, 255, 230)),
    
    #plates
    Oval(130, 205, 50, 30, fill=rgb(50, 30, 0)),
    Oval(130, 205, 40, 20, fill=rgb(255, 255, 230)),
    Oval(130, 204, 25, 10, fill=None, border=rgb(220, 220, 220)),
    Oval(190, 205, 50, 30, fill=rgb(50, 30, 0)),
    Oval(190, 205, 40, 20, fill=rgb(255, 255, 230)),
    Oval(190, 204, 25, 10, fill=None, border=rgb(220, 220, 220)),
    Oval(250, 205, 50, 30, fill=rgb(50, 30, 0)),
    Oval(250, 205, 40, 20, fill=rgb(255, 255, 230)),
    Oval(250, 204, 25, 10, fill=None, border=rgb(220, 220, 220)),
    
    #pathway
    Oval(45, 305, 50, 30, fill=rgb(50, 30, 0)),
    Oval(120, 320, 50, 30, fill=rgb(50, 30, 0)),
    Oval(195, 305, 50, 30, fill=rgb(50, 30, 0)),
    Oval(270, 320, 50, 30, fill=rgb(50, 30, 0)),
    Oval(345, 305, 50, 30, fill=rgb(50, 30, 0)),
)

###starting screen cont.
title = Group(
    Label('Crescent', 230, 280, fill=gradient('silver', 'white', start='bottom'), font=' PERSONAL USE', size=50),
    Label('Spoon', 270, 330, fill=gradient('silver', 'white', start='bottom'), font=' PERSONAL USE', size=50),
)

###starting the game
box = Rect(250, 100, 150, 85, fill='white')
arrow = Label('>', 265, 120, fill='white', bold=True)
new = Label('n e w g a m e', 320, 120, font='montserrat', fill='white', bold=True)
controls = Label('c o n t r o l s', 311, 135, font='montserrat', fill='white')
credits = Label('c r e d i t s', 305, 150, font='montserrat', fill='white')
exit = Label('e x i t g a m e', 320, 165, font='montserrat', fill='white')

tree.dx = 2
sun.dx=.5
title.dx=.3
tree.moving = False
background.dx=1
title.opacity=100
shop.centerX-=400
shop.centerY+=300
shop.dx=3
box.opacity=30

def onStep():
    if tree.moving==True:
        tree.centerX+=tree.dx
        sun.centerX+=sun.dx
        title.centerX+=title.dx
        title.centerY+=title.dx
        shop.centerX+=shop.dx
        shop.centerY-=shop.dx/1.5
        background.centerY-=background.dx*1.3
        sun.centerY-=background.dx*1.3
        tree.centerY-=background.dx
        tree.dx*=.99
        sun.dx*=.985
        shop.dx*=.996
        title.dx*=.992
        background.dx*=.99

        if box.opacity>1:
            box.opacity-=1
        if arrow.opacity>1:
            arrow.opacity-=4
        if new.opacity>1:
            new.opacity-=3
        if controls.opacity>1:
            controls.opacity-=3
        if credits.opacity>1:
            credits.opacity-=3
        #if exit.opacity>1:
            #exit.opacity-=3
        
        if title.dx < .05:
            if title.opacity>0:
                title.opacity-=1

        if shop.right >= 330:
            shop.dx*=.97
            if app.lleft:
                if chef.left>=30:
                    chef.centerX-=3
            if app.uup:
                if chef.top>=85:
                    chef.centerY-=2
            if app.ddown:
                if chef.bottom<=300:
                    chef.centerY+=2
            if app.rright:
                if chef.right<=370:
                    chef.centerX+=3

        if shop.right >= 374.5:
            shop.dx=0
            tree.dx=0
            background.dx=0
creditPage = Group(
    Rect(0, 0, 400, 300, fill=gradient(rgb(255, 255, 230), rgb(201, 201, 161), start='top')),
    Rect(0, 250, 400, 150, fill=gradient(rgb(255, 255, 230), rgb(255, 255, 230), rgb(200, 200, 160), start='bottom')),
    Rect(0, 0, 400, 400, fill=None, borderWidth=12, border=rgb(50, 30, 0)),
    Label('[ESC] Back', 55, 30, font='montserrat'),
    #hat
    Rect(50, 250, 80, 80, fill=rgb(50, 30, 0)),
    Oval(90, 250, 80, 60, fill=rgb(50, 30, 0)),
    Oval(90, 330, 80, 60, fill=rgb(50, 30, 0)),
    Rect(60, 250, 60, 80, fill=rgb(139, 0, 0)),
    Oval(90, 250, 60, 40, fill=rgb(139, 0, 0)),
    Oval(90, 330, 60, 40, fill=rgb(120, 20, 0)),
    Line(70, 250, 70, 290, fill=rgb(120, 20, 0), lineWidth=4),
    Line(90, 260, 90, 300, fill=rgb(120, 20, 0), lineWidth=4),
    Line(110, 250, 110, 300, fill=rgb(120, 20, 0), lineWidth=4),
    #credits
    Label('Thank you', 200, 110, font='montserrat', fill=rgb(50, 30, 0), bold=True, size=40),
    Label('for playing!', 200, 150, font='montserrat', fill=rgb(50, 30, 0), bold=True, size=40),
    Label('A game', 250, 250, font='montserrat', fill=rgb(50, 30, 0), bold=True, size=40),
    Label('by Parker', 250, 290, font='montserrat', fill=rgb(50, 30, 0), bold=True, size=40),
)
controlPage = Group(
    Rect(0, 0, 400, 300, fill=gradient(rgb(255, 255, 230), rgb(201, 201, 161), start='top')),
    Rect(0, 250, 400, 150, fill=gradient(rgb(255, 255, 230), rgb(255, 255, 230), rgb(200, 200, 160), start='bottom')),
    Rect(0, 0, 400, 400, fill=None, borderWidth=12, border=rgb(50, 30, 0)),
    Label('[ESC] Back', 55, 30, font='montserrat'),
    Label('Gameplay', 200, 50, font='montserrat', size=20, fill=rgb(50, 30, 0), bold=True),
    Line(50, 70, 350, 70, lineWidth=4, fill=rgb(50, 30, 0)),
    Label('Controls', 200, 250, font='montserrat', size=20, fill=rgb(50, 30, 0), bold=True),
    Line(50, 270, 350, 270, lineWidth=4, fill=rgb(50, 30, 0)),
    #controls
    Label('Move the chef: W=up A=left S=down D=right', 200, 290, font='montserrat', fill=rgb(50, 30, 0)),
)
creditPage.visible=False
controlPage.visible=False
#def spawnCustomer(x, order):

###onKeyPress
app.lleft=False
app.uup=False
app.rright=False
app.ddown=False

def onKeyPress(key):
    if key == 'a':
        app.lleft=True
    elif key == 'w':
        app.uup=True
    elif key == 's':
        app.ddown=True
    elif key == 'd':
        app.rright=True
    if key == 'enter':
        if new.bold==True:
            tree.moving
            tree.moving=True
        elif controls.bold==True:
            controlPage.visible=True
        elif credits.bold==True:
            creditPage.visible=True
        elif exit.bold==True:
            app.stop()
    if key == 'down':
        if arrow.centerY<165:
            arrow.centerY+=15
        if new.bold==True:
            new.bold=False
            controls.bold=True
        elif controls.bold==True:
            controls.bold=False
            credits.bold=True
        elif credits.bold==True:
            credits.bold=False
            exit.bold=True
    if key == 'up':
        if arrow.centerY>120:
            arrow.centerY-=15
        if exit.bold==True:
            exit.bold=False
            credits.bold=True
        elif credits.bold==True:
            credits.bold=False
            controls.bold=True
        elif controls.bold==True:
            controls.bold=False
            new.bold=True
    if key == 'escape':
        creditPage.visible=False
        controlPage.visible=False

def onKeyRelease(key):
    if key == 'a':
        app.lleft=False
    elif key == 'w':
        app.uup=False
    elif key == 's':
        app.ddown=False
    elif key == 'd':
        app.rright=False

chef.width-=90
chef.height-=120
chef.centerY-=30


cmu_graphics.run()