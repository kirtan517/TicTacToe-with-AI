import pygame 
import math

from pygame.event import clear
pygame.init()

WIDTH=600
HEIGHT=600
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
turn=True

display_surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic Tac Toe with AI')
font = pygame.font.Font(None, 52)



win=pygame.display.set_mode((WIDTH,HEIGHT))
CORDS = [[(WIDTH/3, 0), (WIDTH/3, HEIGHT)], [(WIDTH/3*2, 0), (WIDTH/3*2, HEIGHT)],
         [(0, HEIGHT/3), (WIDTH, HEIGHT/3)], [(0, HEIGHT/3*2), (WIDTH, HEIGHT/3*2)]]
class circle():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw_circle(self):
        pygame.draw.circle(win,WHITE,(self.x,self.y),50,6)
class cross():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.Length=50/math.sqrt(2)
    def draw_cross(self):
        pygame.draw.line(win,WHITE,(self.x-self.Length,self.y-self.Length),(self.x+self.Length,self.y+self.Length),6)   
        pygame.draw.line(win, WHITE, (self.x+self.Length, self.y-self.Length), (self.x-self.Length, self.y +
                                                                                self.Length), 6)
def draw(win):
    for start, end in CORDS:
        pygame.draw.line(win,WHITE,start,end,6)
    pygame.display.update()
def position(xpos,ypos):
    L=list(range(0,800,200))
    for i in range(1,len(L)):
        if xpos<L[i] and xpos >= L[i-1]:
            x=(L[i]+L[i-1])/2
        if ypos<L[i] and ypos >= L[i-1]:
            y = (L[i]+L[i-1])/2
    return (x,y)
visited={}
results = {"x":{100 : 0, 300 : 0, 500 : 0}, "y":{100 : 0, 300 : 0, 500 : 0}}
def result(xpos,ypos):
    results["x"][xpos] += visited[(xpos,ypos)]
    results["y"][ypos] += visited[(xpos,ypos)]
    if (300, 300) in visited.keys() and (100, 100) in visited.keys() and (500, 500) in visited.keys():
        if visited[(300,300)] == visited[(100,100)] == visited[(500,500)]:
            return visited[(300,300)] 
    if (300, 300) in visited.keys() and (100, 500) in visited.keys() and (500, 100) in visited.keys():
        if visited[(300,300)] == visited[(100,500)] == visited[(500,100)]:
            return visited[(300,300)] 
    for i in results.keys():
        for value in results[i]:
            if(results[i][value]==3):
                winner = 1
            
                return winner
            elif(results[i][value]==-3):
                winner = -1
                return winner
            else:
                winner = 0
    return winner
def reset():
    global visited
    global results
    global turn
    visited={}
    results = {"x":{100 : 0, 300 : 0, 500 : 0}, "y":{100 : 0, 300 : 0, 500 : 0}}
    turn = False
    draw(win.pygame.pygame.display().mask.main())


def main():
    run=True
    global turn
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
              run=False  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    xpos, ypos = pygame.mouse.get_pos()
                    xpos,ypos = position(xpos,ypos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if (xpos, ypos) not in visited:
                    visited[(xpos, ypos)]=0
                    if event.button == 1:
                        if turn:
                            circle_obj = circle(xpos,ypos)
                            circle_obj.draw_circle()
                            visited[(xpos, ypos)] = 1
                            turn=False
                        else:
                            cross_obj=cross(xpos,ypos)
                            cross_obj.draw_cross()
                            visited[(xpos, ypos)] = -1
                            turn=True
                        winner_dec = result(xpos, ypos)
                        if(winner_dec==1):
                            text = font.render('Circle Wins', True, GREEN, GREY)
                            textRect = text.get_rect().center = (200, 10)
                            display_surface.blit(text, textRect)
                            print("Circle Wins.")
                            reset()
                        elif(winner_dec == -1):
                            text = font.render('Cross Wins', True, GREEN, GREY)
                            textRect = text.get_rect().center = (200, 10)
                            display_surface.blit(text, textRect)
                            print("Cross Wins.")
                            reset()
                        if len(visited) == 9:
                            reset()
        draw(win)
main()
