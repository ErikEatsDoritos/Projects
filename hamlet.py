import pygame , sys , random , time 
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN
pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
characters = pygame.image.load("hamlet\\Characters.png")
attackbutton = pygame.image.load("hamlet\\attack.png")
blockbutton = pygame.image.load("hamlet\\block.png")
parrybutton = pygame.image.load("hamlet\\parry.png")
attackbutton = pygame.transform.scale(attackbutton,(1000,1000))
blockbutton = pygame.transform.scale(blockbutton,(1000,1000))
parrybutton = pygame.transform.scale(parrybutton,(1000,1000))
characters = pygame.transform.scale(characters,(1000,1000))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 30)
RED = (255, 0, 0)
BLUE = (96, 198, 221)
YELLOW =(221, 232, 78)
GRAY = (161,149,149)
font = pygame.font.SysFont(None, 30)
click = False
progress = 0
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
# ---------------------------
def main_menu():
    click = False
    while True:
        click = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
    
        screen.fill((GRAY))
        draw_text("Hamlet Duel", pygame.font.SysFont(None, 80), (BLACK), screen, 45, 100)
        draw_text('Beat Laertes in a duel to win!', font, (BLACK), screen, 50, 200)
        mx , my = pygame.mouse.get_pos()
        
        Button_1 = pygame.draw.rect(screen, BLACK,(200,300,200,100)) 
        
        draw_text("Play", pygame.font.SysFont(None, 50) ,BLUE,screen,240,330)
        
        if Button_1.collidepoint((mx,my)):
            pygame.draw.rect(screen, RED,(200,300,200,100),3)
            if click:
                game()      

        
       
        pygame.display.flip()
        clock.tick(60)

def game():
    Hamlet_hitpoint = 3
    Laertes_hitpoint = 3 
    running = True
    click = False
    Hamlet_selection = 0
    Laertes_selection = random.randrange(1,4) 
    while running: 
        click = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill((255,212,135))
        mx , my = pygame.mouse.get_pos()
        Attack = pygame.draw.rect(screen, GRAY,(40,350,100,100)) 
        Block = pygame.draw.rect(screen, GRAY,(150,350,100,100)) 
        Parry = pygame.draw.rect(screen, GRAY,(260,350,100,100)) 
        pygame.draw.rect(screen, GRAY,(0,0,200,100))
        pygame.draw.rect(screen, GRAY,(440,0,200,100))
        pygame.draw.rect(screen, RED,(25,50,50*Hamlet_hitpoint,25))
        pygame.draw.rect(screen, RED,(465,50,50*Laertes_hitpoint,25))
        screen.blit(attackbutton,(-280,50))
        screen.blit(blockbutton,(-220,-20))
        screen.blit(parrybutton,(-80,10))
        screen.blit(characters,(-20,-150))
        draw_text('Hamlet', font, (BLACK), screen, 25, 25)
        draw_text('Laertes', font, (BLACK), screen, 465, 25)
        
        if Attack.collidepoint((mx,my)):
            pygame.draw.rect(screen, RED,(40,350,100,100),2) 
            if click:
                Hamlet_selection = 1
                if Hamlet_selection == 1 and Laertes_selection ==1:
                    Hamlet_hitpoint -= 1 
                    Laertes_hitpoint -= 1
                    Laertes_selection = random.randrange(1,4)
                elif Hamlet_selection == 1 and Laertes_selection ==2:
                    Laertes_selection = random.randrange(1,4)
                
                elif Hamlet_selection == 1 and Laertes_selection ==3:
                    Hamlet_hitpoint -= 1 
                    Laertes_selection = random.randrange(1,4)
        if Block.collidepoint((mx,my)):
            pygame.draw.rect(screen, RED,(150,350,100,100),2) 
            if click:
                Hamlet_selection = 2
                if Hamlet_selection == 2 and Laertes_selection ==1:
                        Laertes_selection = random.randrange(1,4)
                elif Hamlet_selection == 2 and Laertes_selection ==2:
                        Laertes_selection = random.randrange(1,4)
                elif Hamlet_selection == 2 and Laertes_selection ==3:
                        Laertes_selection = random.randrange(1,4)
        if Parry.collidepoint((mx,my)):
            pygame.draw.rect(screen, RED,(260,350,100,100),2) 
            if click:
                Hamlet_selection = 3
                if Hamlet_selection == 3 and Laertes_selection ==1:
                    Laertes_hitpoint -= 1
                    Laertes_selection = random.randrange(1,4)

                elif Hamlet_selection == 3 and Laertes_selection ==2:
                    Laertes_selection = random.randrange(1,4)

                elif Hamlet_selection == 3 and Laertes_selection ==3:
                    Laertes_selection = random.randrange(1,4) 
        
        if Hamlet_hitpoint == 0:
            end("Laertes Wins")
            return
        elif Laertes_hitpoint == 0:
            end("Hamlet Wins")
            return
        elif Hamlet_hitpoint == 0 and Laertes_hitpoint == 0: 
            end("Both Lose")
            return

        
    
        pygame.display.flip()
        clock.tick(60)


def end(result):
        running = True
        click = False
        while running: 
            click = False
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            screen.fill((255,212,135))
            mx , my = pygame.mouse.get_pos()
            draw_text(f'{result}', pygame.font.SysFont(None, 80), (BLACK), screen, 45, 100)
            Button_1 = pygame.draw.rect(screen, BLACK,(200,300,200,100)) 
        
            draw_text("Return", pygame.font.SysFont(None, 50) ,BLUE,screen,240,330)
        
            if Button_1.collidepoint((mx,my)):
                pygame.draw.rect(screen, RED,(200,300,200,100),3)
                if click:
                    return
           
           
            pygame.display.flip()
            clock.tick(60)
main_menu()
