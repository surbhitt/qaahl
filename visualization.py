# visualization module

import pygame
import math

from main import GraphNode

pygame.init()

HEIGHT = 720
WIDTH = 1280
COL_WHITE = "#ffffff"
COL_BLACK = "#000000" 
COL_LT_GRAY = "#7c6f64" 
COL_DR_GRAY1 = "#3c3836" 
COL_DR_GRAY2 = "#181818"
COL_BRIGHT_RED     = '#fb4934'     
COL_BRIGHT_GREEN   = '#b8bb26'     
COL_BRIGHT_YELLOW  = '#fabd2f'     
COL_BRIGHT_BLUE    = '#83a598'     
COL_BRIGHT_PURPLE  = '#d3869b'     
COL_BRIGHT_AQUA    = '#8ec07c'     
COL_BRIGHT_ORANGE  = '#fe8019'  

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(COL_DR_GRAY2)
clock = pygame.time.Clock()
CENTX, CENTY =  screen.get_width()//2, screen.get_height()//2

def draw_text(data, posx, posy, col=COL_WHITE, size=19, surf=None):
    font = pygame.font.Font("./quicksand.ttf", size)
    text = font.render(data, True, col)
     
    # create a rectangular object for the
    # text surface object
    if surf == None:
        surf = text.get_rect()
    
    # set the center of the rectangular object.
    surf.center = (posx, posy)
    screen.blit(text, surf)

def draw_header():
    draw_text("Graph:base", 100, 50, col=COL_LT_GRAY)

def draw_head(pos):
    rad = 50
    pygame.draw.circle(screen, COL_BRIGHT_BLUE, pos, rad)    
    draw_text("link_to_the_path", pos.x, pos.y, col=COL_BLACK)

def draw_child(node, pos):
    rad = 30
    pygame.draw.circle(screen, COL_BRIGHT_AQUA, pos, rad)    
    draw_text(node.url, pos.x, pos.y, col=COL_BLACK)

def draw_graph(graph: GraphNode):
    pos_head = pygame.Vector2(CENTX-250, CENTY)
    dist = 250
    angle_inc = 360/len(graph.paths)
    for i in range(len(graph.paths)):
       end =  pygame.Vector2(pos_head.x + dist*math.cos(math.radians(angle_inc*i)), pos_head.y - dist*math.sin(math.radians(angle_inc*i)))
       pygame.draw.line(screen, COL_LT_GRAY, pos_head, end)
       draw_child(graph.paths[i], end)
    draw_head(pos_head)
    # rect = pygame.Rect(screen.get_width()//2, screen.get_height()//2, 50, 80)
    # pygame.draw.rect(screen, cols_sec, rect, 1)

def draw_legend():
    pass

def draw_footer():
    height = 30
    footer_surface = pygame.Surface((screen.get_width(), height))
    footer_surface.fill(COL_DR_GRAY1)
    screen.blit(footer_surface, (0, screen.get_height() - height))
    draw_text("Keys: (q)uit", 80, screen.get_height()-15, col=COL_WHITE, size=20)

def draw(graph: GraphNode):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q :
                    running = False
     
        # RENDER YOUR GAME HERE
        draw_header()
        draw_graph(graph)
        

        draw_legend()
        draw_footer()
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(15)  # limits FPS to 15


def main():
    graph = GraphNode("head")
    graph.paths = [GraphNode(str(x)) for x in range(10)]
    draw(graph) 
    pygame.quit()

if __name__=="__main__":
    main()
