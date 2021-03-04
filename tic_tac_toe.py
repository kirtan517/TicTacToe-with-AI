# importing libraries
from min_max import best_move
import pygame
import math
import time
from pygame.event import clear
pygame.init()

# Global Variables
WIDTH = 600
HEIGHT = 600
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
turn = True


WINNER_FONT = pygame.font.SysFont('comicsans', 100)
pygame.display.set_caption('Tic Tac Toe with AI')
font = pygame.font.Font(None, 20)

visited = {}
results = {"x": {100: 0, 300: 0, 500: 0}, "y": {100: 0, 300: 0, 500: 0}}
draw_objects = []
winner_dec = 0

Score_Circle = 0
Score_Cross = 0

AITURN =True
AI = True

win = pygame.display.set_mode((WIDTH, HEIGHT))
CORDS = [[(WIDTH/3, 0), (WIDTH/3, HEIGHT)], [(WIDTH/3*2, 0), (WIDTH/3*2, HEIGHT)],
         [(0, HEIGHT/3), (WIDTH, HEIGHT/3)], [(0, HEIGHT/3*2), (WIDTH, HEIGHT/3*2)]]

def draw_score(text,xpos,ypos):
    """
    print scores on window
    """
    draw_text = font.render(text, 1, WHITE)
    win.blit(draw_text, (xpos, ypos))
   

def draw_winner(text):
    """
    display winner at the end of game on window
    """
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    win.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)

class circle():
    """
    define center position of circle  
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_circle(self):
        """
        draw cirlce
        """
        pygame.draw.circle(win, WHITE, (self.x, self.y), 50, 6)


class cross():
    """
    define center position of cross  
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Length = 50/math.sqrt(2)

    def draw_cross(self):
        """
        draw cross
        """
        pygame.draw.line(win, WHITE, (self.x-self.Length, self.y -
                                      self.Length), (self.x+self.Length, self.y+self.Length), 6)
        pygame.draw.line(win, WHITE, (self.x+self.Length, self.y-self.Length), (self.x-self.Length, self.y +
                                                                                self.Length), 6)


def draw(win):
    win.fill(BLACK)
    draw_score("Score Circle :"+str(Score_Circle),0,0)
    draw_score("Score Cross :"+str(Score_Cross),200,0)
    for start, end in CORDS:
        pygame.draw.line(win, WHITE, start, end, 6)
    
    for i in draw_objects:
        i()
    pygame.display.update()


def position(xpos, ypos):
    L = list(range(0, 800, 200))
    for i in range(1, len(L)):
        if xpos < L[i] and xpos >= L[i-1]:
            x = (L[i]+L[i-1])/2
        if ypos < L[i] and ypos >= L[i-1]:
            y = (L[i]+L[i-1])/2
    return (x, y)




def result(xpos, ypos):
    print(visited)
    results["x"][xpos] += visited[(xpos, ypos)]
    results["y"][ypos] += visited[(xpos, ypos)]
    if (300, 300) in visited.keys() and (100, 100) in visited.keys() and (500, 500) in visited.keys():
        if visited[(300, 300)] == visited[(100, 100)] == visited[(500, 500)]:
            return visited[(300, 300)]
    if (300, 300) in visited.keys() and (100, 500) in visited.keys() and (500, 100) in visited.keys():
        if visited[(300, 300)] == visited[(100, 500)] == visited[(500, 100)]:
            return visited[(300, 300)]
    for i in results.keys():
        for value in results[i]:
            if(results[i][value] == 3):
                winner = 1

                return winner
            elif(results[i][value] == -3):
                winner = -1
                return winner
            else:
                winner = 0
    return winner



def reset():
    global visited, results, turn, draw_objects, winner_dec, AITURN, AI
    winner_dec =0
    if AI:
        AITURN=False
        AI = False
    else:
        AITURN = True
        AI = True

    draw_objects =[]
    visited = {}
    results = {"x": {100: 0, 300: 0, 500: 0}, "y": {100: 0, 300: 0, 500: 0}}
    draw(win)

def display_winner():
    global Score_Circle, Score_Cross
    
    if(winner_dec == 1):
            draw_winner("Circle Wins.")
            Score_Circle +=1
            return 1
    elif(winner_dec == -1):
        Score_Cross +=1
        draw_winner("Cross Wins.")
        return 1
    if len(visited) == 9:
        draw_winner("Draw")
        return 1
    return 0


def selector(xpos, ypos):
    if AITURN:
        circle_obj = circle(xpos, ypos)
        draw_objects.append(circle_obj.draw_circle)
        visited[(xpos, ypos)] = 1
                

    else:
        cross_obj = cross(xpos, ypos)
        draw_objects.append(cross_obj.draw_cross)
        visited[(xpos, ypos)] = -1
                
                            


def main():
    run = True
    global winner_dec, turn, AITURN
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              run = False

            if AITURN:
                xpos,ypos = best_move(turn,visited)
                selector( xpos, ypos)
                if not len(visited) == 9:            
                    winner_dec = result(xpos, ypos)
                if (display_winner()==1):
                    reset()
                    continue
                AITURN = False
                
            else:        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        xpos, ypos = pygame.mouse.get_pos()
                        xpos, ypos = position(xpos, ypos)

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        
                        if (xpos, ypos) not in visited:
                            selector( xpos, ypos)
                            
                            if not len(visited) == 9:
                                winner_dec = result(xpos, ypos)
                            if (display_winner()==1):
                                reset()
                                continue
                            AITURN = True
                            
        draw(win)
            

if __name__ == "__main__":
    main()
