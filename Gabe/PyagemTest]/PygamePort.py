import pygame
import random,math
from HelperScripts.Color import RandomGradient
from HelperScripts.Create_Shape import Line
from HelperScripts.ManageScene import Group, Move

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 400),pygame.RESIZABLE)
print(max(pygame.display.get_window_size()[0],pygame.display.get_window_size()[1]))
def app():
    return

def main():
    clock = pygame.time.Clock()
    running = True
    #Start(screen)
    Parts = Start(screen)
    print(Parts[1])

    size = (pygame.display.get_window_size()[0],pygame.display.get_window_size()[1])
    while running:
        
        #Start(screen)
        Max = max(pygame.display.get_window_size()[0],pygame.display.get_window_size()[1])
        Line(random.randint(1,Max),random.randint(1,Max),random.randint(1,Max),random.randint(1,Max),RandomGradient(20,50,"right"),10, Screen=screen)
        #Line(random.randint(1,Max),random.randint(1,Max),pygame.display.get_window_size()[0],pygame.display.get_window_size()[1],RandomGradient(20,50,"right"),10, Screen=screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #end event/ close window if the X button is pressed
                running = False
            if event.type == pygame.WINDOWRESIZED:
                size = (pygame.display.get_window_size()[0],pygame.display.get_window_size()[1])
        #Rect(random.randint(0,400),random.randint(0,400),10,10,RandomGradient(5))
        #screen.fill('black')
        screen.blit(*Group(*Parts[0],width=size[0],height=size[1]))
        #go to next frame
        pygame.display.flip()
        Parts = Move(Parts,['sky', 'sun', 'background', 'tree'],(1,1))
        clock.tick(120)  # limit FPS

    pygame.quit()

if __name__ == "__main__":
    from HelperScripts.TEst import Start
    
    main()
    