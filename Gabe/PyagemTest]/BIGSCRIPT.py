import pygame
import random
import math

Scc = ""
def gradient(*args, start = 'top'):
    pts = []
    for a in args:
        if isinstance(a, (tuple, list)):
            pts.append(a)
    return CreateGradientStrict(pts,align=start)

def rgb(r,g,b):
    return (r,g,b)

def CreateGradientStrict(colors, detailLevel=50, align="top"):
    colorss = colors
    steps = len(colors) * detailLevel 

    #size
    if align in ["top-left", "top-right", "bottom-left", "bottom-right", "center"]:
        width = height = steps  # square for diagonal or center
    elif align in ["left", "right"]:
        width, height = steps, 1  # horizontal gradient
    else:
        width, height = 1, steps  # vertical gradient

    # create surface
    surf = pygame.Surface((width, height), pygame.SRCALPHA)

    # gradient TIME
    if align == "center":
        # center expands outward
        for y in range(height):
            for x in range(width):
                dx = abs(x - width // 2) / (width // 2)
                dy = abs(y - height // 2) / (height // 2)
                t = max(dx, dy)
                segment = t * (len(colors) - 1)
                idx = int(segment)
                blend = segment - idx
                if idx >= len(colors) - 1:
                    c1, c2 = colors[-2], colors[-1]
                else:
                    c1, c2 = colors[idx], colors[idx + 1]
                r = int(c1[0] + (c2[0] - c1[0]) * blend)
                g = int(c1[1] + (c2[1] - c1[1]) * blend)
                b = int(c1[2] + (c2[2] - c1[2]) * blend)
                surf.set_at((x, y), (r, g, b))

    elif align in ["top-left", "top-right", "bottom-left", "bottom-right"]:
        # diagonal gradient
        for y in range(height):
            for x in range(width):
                # diagonal progress
                if align == "top-left":
                    t = (x + y) / (width + height - 2)
                elif align == "top-right":
                    t = ((width - 1 - x) + y) / (width + height - 2)
                elif align == "bottom-left":
                    t = (x + (height - 1 - y)) / (width + height - 2)
                elif align == "bottom-right":
                    t = ((width - 1 - x) + (height - 1 - y)) / (width + height - 2)

                segment = t * (len(colors) - 1)
                idx = int(segment)
                blend = segment - idx
                if idx >= len(colors) - 1:
                    c1, c2 = colors[-2], colors[-1]
                else:
                    c1, c2 = colors[idx], colors[idx + 1]
                r = int(c1[0] + (c2[0] - c1[0]) * blend)
                g = int(c1[1] + (c2[1] - c1[1]) * blend)
                b = int(c1[2] + (c2[2] - c1[2]) * blend)
                surf.set_at((x, y), (r, g, b))

    elif align in ["left", "right"]:
        # horizontal gradient
        for x in range(width):
            t = x / (width - 1)
            if align == "right":
                t = 1 - t  # flip for right
            segment = t * (len(colors) - 1)
            idx = int(segment)
            blend = segment - idx
            if idx >= len(colors) - 1:
                c1, c2 = colors[-2], colors[-1]
            else:
                c1, c2 = colors[idx], colors[idx + 1]
            r = int(c1[0] + (c2[0] - c1[0]) * blend)
            g = int(c1[1] + (c2[1] - c1[1]) * blend)
            b = int(c1[2] + (c2[2] - c1[2]) * blend)
            surf.set_at((x, 0), (r, g, b))

    elif align in ["top", "bottom"]:
        # vertical gradient
        for y in range(height):
            t = y / (height - 1)
            if align == "bottom":
                t = 1 - t  # flip for bottom
            segment = t * (len(colors) - 1)
            idx = int(segment)
            blend = segment - idx
            if idx >= len(colors) - 1:
                c1, c2 = colors[-2], colors[-1]
            else:
                c1, c2 = colors[idx], colors[idx + 1]
            r = int(c1[0] + (c2[0] - c1[0]) * blend)
            g = int(c1[1] + (c2[1] - c1[1]) * blend)
            b = int(c1[2] + (c2[2] - c1[2]) * blend)
            surf.set_at((0, y), (r, g, b))

    return ["gradient", surf, colorss, align]


def RandomGradient(MaxColors,Detail=50,WhatWay="top"):
    count = 0
    Max = random.randint(2,MaxColors)
    Colors = []
    while count < Max:
        count += 1
        Colors.append([random.randint(1,255),random.randint(1,255),random.randint(1,255)])
    return CreateGradientStrict(Colors, Detail, WhatWay)

def Rect(X, Y, width, height, fill=(0,0,0), border=None, borderWidth=2,
     opacity=255, rotateAngle=0, align='left-top',
     Screen = None,render = True):
    
    global screen
    if Screen is None:
        Screen = screen
    #Create rectangle/frame
    if border == None:
        TempSurf = pygame.Surface((width, height), pygame.SRCALPHA)
        #set graident texture size
        if fill[0] == "gradient":
            TempSurf.blit(pygame.transform.scale(fill[1], (width, height)), (0, 0))
        else:
            TempSurf.fill(pygame.Color(fill[0],fill[1],fill[2],255))
    else:
        #make the frame + border size
        TempSurf = pygame.Surface((width+(borderWidth*2), height+(borderWidth*2)), pygame.SRCALPHA)
        
        # Draw the border first
        if isinstance(border, list) and border[0] == "gradient":
            TempSurf.blit(pygame.transform.scale(border[1], (width+(borderWidth*2), height+(borderWidth*2))), (0,0))
        else:
            pygame.draw.rect(TempSurf, border, pygame.Rect(0, 0, width+(borderWidth*2), height+(borderWidth*2)))

        # Draw the inner fill
        if fill[0] == "gradient":
            TempSurf.blit(pygame.transform.scale(fill[1], (width, height)), (borderWidth, borderWidth))
        else:
            Box = pygame.Surface((width, height), pygame.SRCALPHA)
            Box.fill((fill[0],fill[1],fill[2]))
            TempSurf.blit(Box,(borderWidth, borderWidth))
    
    #set transparency
    TempSurf.set_alpha(opacity)
    #then rotate image
    RotatedSurf = pygame.transform.rotate(TempSurf, rotateAngle)
    #set final pos and rotashe/confirm it
    RotatedRect = RotatedSurf.get_rect(topleft=(X-(width/2), Y-(height/2)))
    #add to canvis

    #GEts save string
    DecodeColor = ""
    if fill[0] == "gradient":
        DecodeColor = "G,"
        for Value in fill[2]:
            DecodeColor = DecodeColor+f"{Value[0]}+{Value[1]}+{Value[2]}+"
        DecodeColor = DecodeColor+f",50,{fill[3]}"
    else:
        DecodeColor = f"C,{fill[0]},{fill[1]},{fill[2]}"
    DecodeBorderColor = ""
    if border == None:
        DecodeBorderColor = "None,0,0,0"
    elif border[0] == "gradient":
        DecodeBorderColor = "G,"
        for Value in border[2]:
            DecodeBorderColor = DecodeBorderColor+f"{Value[0]}+{Value[1]}+{Value[2]}+"
        DecodeBorderColor = DecodeBorderColor+f",50,{border[3]}"
    else:
        DecodeBorderColor = f"C,{fill[0]},{fill[1]},{fill[2]}"
    global Scc
    Scc = Scc+f"R,{X},{Y},{width},{height},{DecodeColor},{DecodeBorderColor},{borderWidth},{opacity},{rotateAngle},{align}|"
    print(Scc)
    if render == True:
        Screen.blit(RotatedSurf, RotatedRect)
    else:
        return [RotatedSurf,RotatedRect]

def Oval(X, Y, width, height, fill=(0,0,0), border=None,
     borderWidth=2, opacity=255, rotateAngle=0,
     Screen = None, render = True):
    
    global screen
    if Screen is None:
        Screen = screen

    TempSurf = pygame.Surface((width + borderWidth*2, height + borderWidth*2), pygame.SRCALPHA)

    if border:
        if border[0] == "gradient":
            TempSurf.blit(pygame.transform.scale(border[1], (width + borderWidth*2, height + borderWidth*2)), (0,0))
        else:
            pygame.draw.ellipse(TempSurf, border, pygame.Rect(0,0,width + borderWidth*2, height + borderWidth*2))
    
    if fill[0] == "gradient":
        scaled_fill = pygame.transform.scale(fill[1], (width, height))
        mask = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.ellipse(mask, (255,255,255), pygame.Rect(0,0,width,height))
        scaled_fill.blit(mask, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
        TempSurf.blit(scaled_fill, (borderWidth, borderWidth))
    else:
        pygame.draw.ellipse(TempSurf, fill, pygame.Rect(borderWidth, borderWidth, width, height))
    #transparency
    TempSurf.set_alpha(opacity)
    #rotate
    RotatedSurf = pygame.transform.rotate(TempSurf, rotateAngle)
    #pos
    RotatedRect = RotatedSurf.get_rect(topleft=(X-(width/2), Y-(height/2)))
    #display
    #GEts save string
    DecodeColor = ""
    if fill[0] == "gradient":
        DecodeColor = "G,"
        for Value in fill[2]:
            DecodeColor = DecodeColor+f"{Value[0]}+{Value[1]}+{Value[2]}+"
        DecodeColor = DecodeColor+f",50,{fill[3]}"
    else:
        DecodeColor = f"C,{fill[0]},{fill[1]},{fill[2]}"
    DecodeBorderColor = ""
    if border == None:
        DecodeBorderColor = "None,0,0,0"
    elif border[0] == "gradient":
        DecodeBorderColor = "G,"
        for Value in border[2]:
            DecodeBorderColor = DecodeBorderColor+f"{Value[0]}+{Value[1]}+{Value[2]}+"
        DecodeBorderColor = DecodeBorderColor+f",50,{border[3]}"
    else:
        DecodeBorderColor = f"C,{fill[0]},{fill[1]},{fill[2]}"
    global Scc
    Scc = Scc+f"O,{X},{Y},{width},{height},{DecodeColor},{DecodeBorderColor},{borderWidth},{opacity},{rotateAngle}|"
    print(Scc)
    if render == True:
        Screen.blit(RotatedSurf, RotatedRect)
    else:
        return [RotatedSurf,RotatedRect]

def Circle(X, Y, radius, fill=(0,0,0), border=None,
       borderWidth=2, opacity=100, rotateAngle=0,
       Screen = None, render = True):
    return Oval(X,Y,radius,radius,fill,border,borderWidth,opacity,rotateAngle, Screen=Screen, render=render)

def Line(x1, y1, x2, y2, fill=(0,0,0), lineWidth=2, opacity=255, Screen = None, render = True):
    
    global screen
    if Screen is None:
        Screen = screen
    # Check if fill is a gradient
    if isinstance(fill, list) and fill[0] == "gradient":
        # Calculate line length and make TempSurf wide enough
        length = int(math.hypot(x2 - x1, y2 - y1)) or 1  # distance between points
        TempSurf = pygame.Surface((length, lineWidth), pygame.SRCALPHA)  # width=line length, height=lineWidth

        # gradient scaled to the surface
        TempSurf.blit(pygame.transform.scale(fill[1], (length, lineWidth)), (0, 0))

        # Rotate surface
        angle = -math.degrees(math.atan2(y2 - y1, x2 - x1))
        RotSurf = pygame.transform.rotate(TempSurf, angle)

        # position and rotated surface
        rect = RotSurf.get_rect(center=((x1 + x2)/2, (y1 + y2)/2))

        # Set transparency
        RotSurf.set_alpha(opacity)

        # Add to screen
        if render == True:
            Screen.blit(RotSurf, rect.topleft)
        else:
            return [RotSurf,rect.topleft]
        
    else:
        # boring line
        color = pygame.Color(fill[0], fill[1], fill[2], opacity) if isinstance(fill, tuple) else fill
        """if render == True:
            Screen.blit(RotatedSurf, RotatedRect)
        else:
            return [RotatedSurf,RotatedRect]"""
        pygame.draw.line(Screen, color, (x1, y1), (x2, y2), lineWidth)

def Label(text,
          x,
          y,
          size=24,
          fill=(255, 255, 255),
          flipX=False,
          flipY=False,
          mode="linear",
          center_expand=False,
          font=None,
          Screen = None,):
    
    global screen
    if Screen is None:
        Screen = screen

    if font is None:
        font = pygame.font.SysFont(None, size)

    pos = (x, y)

    text_surface = font.render(text, True, (255, 255, 255))
    text_w, text_h = text_surface.get_size()

    mask_surface = pygame.Surface((text_w, text_h), pygame.SRCALPHA)
    mask_surface.blit(text_surface, (0, 0))

    is_gradient = isinstance(fill, dict) and fill.get("gradient")

    if not is_gradient:
        colored = font.render(text, True, fill)
        Screen.blit(colored, pos)
        return

    grad_info = fill

    final_surf = pygame.Surface((text_w, text_h), pygame.SRCALPHA)
    final_surf.blit(fill, (0, 0))
    final_surf.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    Screen.blit(final_surf, pos)

def Polygon(*args,
            fill=(0,0,0),
            border=None,
            borderWidth=2,
            opacity=255,
            rotateAngle=0,
            Screen = None,render = True):
    points = args
    # Collect numeric points
    pts = [a for a in args if isinstance(a, (int, float))]
    if len(pts) % 2 != 0 or len(pts) < 6:
        return  # need at least 3 points (6 numbers)

    pointList = [(pts[i], pts[i+1]) for i in range(0, len(pts), 2)]

    # Bounding box
    xs = [p[0] for p in pointList]
    ys = [p[1] for p in pointList]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    w = max(maxx - minx, 1)
    h = max(maxy - miny, 1)

    # Temporary surface
    TempSurf = pygame.Surface((w + borderWidth*2, h + borderWidth*2), pygame.SRCALPHA)
    shifted = [(x - minx + borderWidth, y - miny + borderWidth) for (x, y) in pointList]

    # --- FILL ---
    if isinstance(fill, list) and fill[0] == "gradient":
        # gradient fill
        grad_surf = pygame.transform.scale(fill[1], (w, h))
        mask = pygame.Surface((w, h), pygame.SRCALPHA)
        pygame.draw.polygon(mask, (255,255,255), [(x-borderWidth, y-borderWidth) for (x,y) in shifted])
        grad_surf.blit(mask, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
        TempSurf.blit(grad_surf, (borderWidth, borderWidth))
    else:
        # solid fill
        pygame.draw.polygon(TempSurf, fill, shifted)

    # --- BORDER ---
    if border is not None:
        if isinstance(border, list) and border[0] == "gradient":
            bw, bh = w + borderWidth*2, h + borderWidth*2
            grad_surf = pygame.transform.scale(border[1], (bw, bh))
            mask = pygame.Surface((bw, bh), pygame.SRCALPHA)
            pygame.draw.polygon(mask, (255,255,255), shifted)
            grad_surf.blit(mask, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
            TempSurf.blit(grad_surf, (0,0))
        else:
            pygame.draw.polygon(TempSurf, border, shifted, borderWidth)

    # --- FINALIZE ---
    TempSurf.set_alpha(opacity)
    if rotateAngle != 0:
        TempSurf = pygame.transform.rotate(TempSurf, rotateAngle)

    rect = TempSurf.get_rect(topleft=(minx - borderWidth, miny - borderWidth))

    #GEts save string
    Points = ""
    for point in points:
        print(point)
        Points = Points+str(point)+"+"
    DecodeColor = ""
    if fill[0] == "gradient":
        DecodeColor = "G,"
        for Value in fill[2]:
            DecodeColor = DecodeColor+f"{Value[0]}+{Value[1]}+{Value[2]}+"
        DecodeColor = DecodeColor+f",50,{fill[3]}"
    else:
        DecodeColor = f"C,{fill[0]},{fill[1]},{fill[2]}"
    DecodeBorderColor = ""
    if border == None:
        DecodeBorderColor = "None,0,0,0"
    elif border[0] == "gradient":
        DecodeBorderColor = "G,"
        for Value in border[2]:
            DecodeBorderColor = DecodeBorderColor+f"{Value[0]}+{Value[1]}+{Value[2]}+"
        DecodeBorderColor = DecodeBorderColor+f",50,{border[3]}"
    else:
        DecodeBorderColor = f"C,{fill[0]},{fill[1]},{fill[2]}"
    global Scc
    Scc = Scc+f"P,{Points},{DecodeColor},{DecodeBorderColor},{borderWidth},{opacity},{rotateAngle}|"
    print(Scc)
    if render == True:
        Screen.blit(TempSurf, rect)
    else:
        return [TempSurf, rect]


def Group(*draw_calls, width=1000, height=1000,Screen):
    temp_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Backup the global screen
    original_screen = Screen
    # Redirect all drawing to temp_surface
    Screen = temp_surface

    # Call each function
    for call in draw_calls:
        pass  # the functions already executed, they drew to `screen` (now temp_surface)

    # Restore the original screen
    Screen = original_screen

    # Return the grouped surface
    return temp_surface

def render(surface,x,y,screen):
    screen.blit(surface,(x,y))

def LoadScene(string,scene):
    for Main in str.split(string, "|"):
        SmallerSPlit = str.split(Main,",")
        if SmallerSPlit[0] in ("R", "O"):
            PosSize = [int(SmallerSPlit[1]),int(SmallerSPlit[2]),int(SmallerSPlit[3]),int(SmallerSPlit[4])]
            #check if color or other
            if SmallerSPlit[5] == "C":
                texture = (int(SmallerSPlit[6]),int(SmallerSPlit[7]),int(SmallerSPlit[8]))
            elif SmallerSPlit[5] == "G":
                gradientSplit = str.split(SmallerSPlit[6],"+")
                grad_array = []
                for i in range(math.floor((len(gradientSplit))/3)):
                    TN = (i*3) #Temp number
                    grad_array.append((int(gradientSplit[TN]),int(gradientSplit[TN+1]),int(gradientSplit[TN+2])))
                texture = CreateGradientStrict(grad_array,int(SmallerSPlit[7]),SmallerSPlit[8])
            #moveing onto the border
            if SmallerSPlit[9] == "C":
                Border = (int(SmallerSPlit[10]),int(SmallerSPlit[11]),int(SmallerSPlit[12]))
            elif SmallerSPlit[9] == "G":
                gradientSplit = str.split(SmallerSPlit[10],"+")
                grad_array = []
                for i in range(math.floor((len(gradientSplit))/3)):
                    TN = (i*3) #Temp number
                    grad_array.append((int(gradientSplit[TN]),int(gradientSplit[TN+1]),int(gradientSplit[TN+2])))
                Border = CreateGradientStrict(grad_array,int(SmallerSPlit[11]),SmallerSPlit[12])
            else:
                Border = None
            BorderWidth = int(SmallerSPlit[13])
            Opacity = int(SmallerSPlit[14])
            RotateAngle = int(SmallerSPlit[15])
            if SmallerSPlit[0] == "R":
                Align = SmallerSPlit[16]
            if SmallerSPlit[0] == "R":
                Rect(PosSize[0],PosSize[1], #pos
                 PosSize[2],PosSize[3], #size
                 texture,Border,BorderWidth,
                 Opacity,RotateAngle,Align,
                 Screen=scene)
            else:
                Oval(PosSize[0],PosSize[1], #pos
                 PosSize[2],PosSize[3], #size
                 texture,Border,BorderWidth,
                 Opacity,RotateAngle,
                 Screen=scene)
        elif SmallerSPlit[0] == "P":
            Points = []
            for Point in str.split(SmallerSPlit[1],"+"):
                if Point != '':
                    Points.append(int(Point))
            if SmallerSPlit[2] == "C":
                texture = (int(SmallerSPlit[3]),int(SmallerSPlit[4]),int(SmallerSPlit[5]))
            elif SmallerSPlit[2] == "G":
                gradientSplit = str.split(SmallerSPlit[3],"+")
                grad_array = []
                for i in range(math.floor((len(gradientSplit))/3)):
                    TN = (i*3) #Temp number
                    grad_array.append((int(gradientSplit[TN]),int(gradientSplit[TN+1]),int(gradientSplit[TN+2])))
                texture = CreateGradientStrict(grad_array,int(SmallerSPlit[4]),SmallerSPlit[5])
            #moveing onto the border
            if SmallerSPlit[6] == "C":
                Border = (int(SmallerSPlit[7]),int(SmallerSPlit[8]),int(SmallerSPlit[9]))
            elif SmallerSPlit[6] == "G":
                gradientSplit = str.split(SmallerSPlit[7],"+")
                grad_array = []
                for i in range(math.floor((len(gradientSplit))/3)):
                    TN = (i*3) #Temp number
                    grad_array.append((int(gradientSplit[TN]),int(gradientSplit[TN+1]),int(gradientSplit[TN+2])))
                Border = CreateGradientStrict(grad_array,int(SmallerSPlit[8]),SmallerSPlit[9])
            else:
                Border = None
            BorderWidth = int(SmallerSPlit[10])
            Opacity = int(SmallerSPlit[11])
            RotateAngle = int(SmallerSPlit[12])
            Polygon(*Points,texture,Border,BorderWidth,Opacity,RotateAngle)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 400))

def app():
    return
def Start(screen):
    sky = Rect(200, 130, 400, 260, fill=gradient(rgb(255, 69, 0), rgb(255, 165, 0), rgb(255, 160, 122), rgb(255, 105, 180), rgb(150, 0, 150), start='bottom'),Screen=screen)
    sun = Group(
        Circle(200, 220, 80, fill=gradient(rgb(255, 255, 255), rgb(255, 255, 255), rgb(255, 255, 100),start="center"),Screen=screen, opacity=255),
        Screen=screen
    )
    background = Group(
        Rect(200, 330, 400, 150, fill=gradient(rgb(255, 40, 0), rgb(255, 165, 0), start='top'),Screen=screen),
        Polygon(0, 300, 400, 330, 400, 550, 0, 550, fill=gradient(rgb(120, 20, 0), rgb(255, 70, 0), start='bottom'),Screen=screen),
        #left clouds
        Oval(100, 235, 200, 20, fill=gradient(rgb(255, 90, 0), rgb(255, 10, 0), rgb(220, 0, 0), start='left'),Screen=screen),
        Oval(70, 70, 200, 100, fill=gradient(rgb(150, 0, 150), rgb(150, 0, 150), rgb(255, 135, 180), rgb(255, 160, 122), start='top'),Screen=screen),
        Oval(250, 200, 70, 30, fill=gradient(rgb(255, 10, 0), rgb(255, 100, 0), start='left'),Screen=screen),
        Oval(270, 100, 100, 60, fill=gradient(rgb(250, 165, 140), rgb(255, 127, 80), start='top'),Screen=screen),
        Oval(370, 125, 200, 70, fill=gradient(rgb(255, 160, 122), rgb(255, 127, 80), rgb(255, 165, 0), start='top'),Screen=screen),
        Oval(300, 50, 400, 100, fill=gradient(rgb(150, 0, 150), rgb(150, 0, 150), rgb(255, 135, 180), rgb(255, 160, 122), start='top'),Screen=screen),
        Screen=screen
    )

    tree = Group(
        Polygon(-20, 350, 20, 350, 150, 150, 170, 100, 135, 150, fill=gradient(rgb(227, 60, 0), rgb(180, 50, 0), rgb(50, 0, 0), start='bottom'),Screen=screen),
        Polygon(170, 100, 150, 150, 170, 230, 180, 150, fill=gradient(rgb(100, 100, 70), rgb(180, 50, 0), start='top'),Screen=screen),
        Polygon(170, 100, 190, 140, 230, 180, 220, 130, fill=gradient(rgb(100, 100, 70), rgb(180, 50, 0), start='top'),Screen=screen),
        Polygon(170, 100, 140, 150, 70, 210, 105, 140, fill=gradient(rgb(100, 100, 70), rgb(180, 50, 0), start='top'),Screen=screen),
        Polygon(170, 100, 105, 130, 60, 130, 105, 100, fill=gradient(rgb(100, 100, 70), rgb(120, 80, 40), rgb(180, 50, 0), start='right-top'),Screen=screen),
        Screen=screen
    )
def main():
    clock = pygame.time.Clock()
    running = True
    screen.fill("black")
    Start(screen)
    #LoadScene("R,0,0,400,250,G,255+69+0+255+165+0+255+160+122+255+105+180+150+0+150+,50,bottom,None,0,0,0,2,255,0,left-top|O,200,220,40,40,G,255+255+255+255+255+255+255+255+100+,50,top,None,0,0,0,2,100,0|R,0,250,400,150,G,255+40+0+255+165+0+,50,top,None,0,0,0,2,255,0,left-top|P,0+300+400+330+400+550+0+550+,G,120+20+0+255+70+0+,50,bottom,None,0,0,0,2,255,0|O,100,235,200,20,G,255+90+0+255+10+0+220+0+0+,50,left,None,0,0,0,2,255,0|O,70,70,200,100,G,150+0+150+150+0+150+255+135+180+255+160+122+,50,top,None,0,0,0,2,255,0|O,250,200,70,30,G,255+10+0+255+100+0+,50,left,None,0,0,0,2,255,0|O,270,100,100,60,G,250+165+140+255+127+80+,50,top,None,0,0,0,2,255,0|O,370,125,200,70,G,255+160+122+255+127+80+255+165+0+,50,top,None,0,0,0,2,255,0|O,300,50,400,100,G,150+0+150+150+0+150+255+135+180+255+160+122+,50,top,None,0,0,0,2,255,0|P,-20+350+20+350+150+150+170+100+135+150+,G,227+60+0+180+50+0+50+0+0+,50,bottom,None,0,0,0,2,255,0|P,170+100+150+150+170+230+180+150+,G,100+100+70+180+50+0+,50,top,None,0,0,0,2,255,0|P,170+100+190+140+230+180+220+130+,G,100+100+70+180+50+0+,50,top,None,0,0,0,2,255,0|P,170+100+140+150+70+210+105+140+,G,100+100+70+180+50+0+,50,top,None,0,0,0,2,255,0|P,170+100+105+130+60+130+105+100+,G,100+100+70+120+80+40+180+50+0+,50,right-top,None,0,0,0,2,255,0|",screen)
    while running:
        #Line(random.randint(1,400),random.randint(1,400),random.randint(1,400),random.randint(1,400),RandomGradient(20,50,"right"),10, Screen=screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #end event/ close window if the X button is pressed
                running = False
        #Rect(random.randint(0,400),random.randint(0,400),10,10,RandomGradient(5))
    

        #go to next frame
        pygame.display.flip()

        clock.tick(100)  # limit FPS

    pygame.quit()

if __name__ == "__main__":    
    main()
    