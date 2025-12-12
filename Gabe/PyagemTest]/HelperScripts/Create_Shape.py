import pygame
import math
from HelperScripts.screen import screen as Scc
def Rect(X, Y, width, height, fill=(0,0,0), border=None, borderWidth=2,
     opacity=255, rotateAngle=0, align='left-top',
     Screen = None,render = False):
    
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

    if render == True:
        Screen.blit(TempSurf, RotatedRect)
    else:
        return (TempSurf,RotatedRect)

def Oval(X, Y, width, height, fill=(0,0,0), border=None,
     borderWidth=2, opacity=255, rotateAngle=0,
     Screen = None, render = False):
    
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
    if render == True:
        Screen.blit(RotatedSurf, RotatedRect)
    else:
        return(TempSurf, RotatedRect)

def Circle(X, Y, radius, fill=(0,0,0), border=None,
       borderWidth=2, opacity=100, rotateAngle=0,
       Screen = None, render = True):
    return Oval(X,Y,radius,radius,fill,border,borderWidth,opacity,rotateAngle, Screen=Screen, render=render)

def Line(x1, y1, x2, y2, fill=(0,0,0), lineWidth=2, opacity=255, Screen = None, render = True):
    
    global screen
    if Screen is None:
        Screen = screen
    
    length = int(math.hypot(x2 - x1, y2 - y1)) or 1  # distance between
    TempSurf = pygame.Surface((length, lineWidth), pygame.SRCALPHA)  # width=line length, height=lineWidth
    # Check if fill is a gradient
    if isinstance(fill, list) and fill[0] == "gradient":
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
        
        
    else:
        # boring line
        color = pygame.Color(fill[0], fill[1], fill[2], opacity) if isinstance(fill, tuple) else fill
        pygame.draw.line(TempSurf, color, (x1, y1), (x2, y2), lineWidth)
    if render == True:
        Screen.blit(RotSurf, rect.topleft)
    else:
        return [TempSurf,rect.topleft]

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
            Screen = None,render = False):
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
    if render == True:
        Screen.blit(TempSurf, rect)
    else:
        return(TempSurf,rect)
