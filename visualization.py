# visualization module
"""
    TODO
     - header
     - format the links
     - legend
     - click
"""
import pygame
import math

# ----------------------------------------------------------------- modules
from classes import GraphNode
from helpers import is_cursor_on_node
# ----------------------------------------------------------------- constants
# screen resolution
SCREEN_HEIGHT, SCREEN_WIDTH = 720, 1280
CENTX, CENTY =  SCREEN_WIDTH//2 , SCREEN_HEIGHT//2  
# colors
COL_WHITE = "#ffffff"
COL_BLACK = "#000000" 
COL_LT_GRAY = "#7c6f64" 
COL_DR_GRAY1 = "#3c3836" 
COL_DR_GRAY2 = "#181818"
COL_BRT_RED = '#fb4934'     
COL_BRT_GREEN = '#b8bb26'     
COL_BRT_YELLOW = '#fabd2f'     
COL_BRT_BLUE = '#83a598'     
COL_BRT_PURPLE = '#d3869b'     
COL_BRT_AQUA = '#8ec07c'     
COL_BRT_ORANGE = '#fe8019'

# initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(COL_DR_GRAY2)
clock = pygame.time.Clock() # for fps
node_hovered = GraphNode("")
trans_url_text = {}

# ----------------------------------------------------------------- functions
# render text on screen
# TODO the surf parameter and the idea does not function
#       the text is not being rendered on the surf
#       screen relative positioning at this moment
#       correct the coordinationg from center based positioning to left top based
def draw_text(data, posx, posy, txt_col=COL_WHITE, bg_col=None, size=19, surf=screen):
    font = pygame.font.Font("./quicksand.ttf", size)
    text = font.render(data, True, txt_col, bg_col)
     
    # create a rectangular object for the
    # text surface object
    text_rect = text.get_rect()
    
    # set the center of the rectangular object.
    text_rect.center = (posx, posy)
    surf.blit(text, text_rect)

def format_link_text(node, base, max_len=17):
    path = node.rel_path.replace("https://", "")
    if len(path) > 17:
        path = path[:max_len]+" ---" 
    trans_url_text[node.rel_path] = path

# draw the header for the screen
def draw_header(url):
    draw_text(f" ./ = {url} ", 150, 20, txt_col=COL_WHITE, bg_col=COL_BLACK)
    draw_text(f" depth =  ", 80, 50, txt_col=COL_WHITE, bg_col=COL_BLACK)

# draw the head node 
def draw_head(rel_path, pos):
    rad = 50
    pygame.draw.circle(screen, COL_BRT_BLUE, pos, rad)    
    draw_text(rel_path, pos.x, pos.y, txt_col=COL_WHITE, bg_col=COL_BLACK)

# draw corresponding child nodes
def draw_child(node, base, pos):
    global node_hovered
    rad = 30
    curx, cury = pygame.mouse.get_pos()
    if (is_cursor_on_node(curx, cury, pos.x, pos.y,rad)):
        node_hovered = node
        col = COL_BRT_AQUA
    else: 
        col = COL_BRT_RED
    pygame.draw.circle(screen, col, pos, rad)    
    draw_text(trans_url_text[node.rel_path], pos.x, pos.y, size=15, txt_col=COL_WHITE, bg_col=COL_BLACK)

# draw the whole graph 
# calls to draw_child and draw_head fns
def draw_graph(graph: GraphNode):
    pos_head = pygame.Vector2(CENTX-250, CENTY)
    dist = 250
    if len(graph.paths):
        angle_inc = 360/len(graph.paths)
        for i in range(len(graph.paths)):
           end =  pygame.Vector2(pos_head.x + dist*math.cos(math.radians(angle_inc*i)), pos_head.y - dist*math.sin(math.radians(angle_inc*i)))
           pygame.draw.line(screen, COL_LT_GRAY, pos_head, end)
           draw_child(graph.paths[i], graph.rel_path, end)
           draw_legend_content(i+1, graph.paths[i].rel_path)
    draw_head(graph.rel_path, pos_head)

# draw the legend/sidebar
# content list of the paths
def draw_legend_content(sr_no, rel_path):
    # very messy should be somehow linked to legend 
    # TODO
    posx, posy = SCREEN_WIDTH-(500//2), 25
    rel_path = rel_path.replace("https://", "")

    draw_text(rel_path[:45], posx, (sr_no*posy)+30)
    
def draw_legend():
    width = 500
    height = screen.get_height()
    pygame.draw.rect(screen, COL_BLACK, (SCREEN_WIDTH - width, 0, width, height))
    # legend = pygame.Surface((width, height))
    # legend.fill(COL_BLACK)
    # screen.blit(legend, (SCREEN_WIDTH - width, 0))
    draw_text("[-] Legend", SCREEN_WIDTH-width+50, 20, txt_col=COL_WHITE, bg_col=COL_BLACK)

# draw the footer
def draw_footer():
    height = 30
    footer_surface = pygame.Surface((screen.get_width(), height))
    footer_surface.fill(COL_BLACK)
    screen.blit(footer_surface, (0, screen.get_height() - height))
    draw_text(" -> (q)uit | -> click on the node to expand ", 200, screen.get_height()-17, txt_col=COL_WHITE, bg_col=COL_BLACK, size=20)

# draw the whole screen
# takes the object array containing the nodes as parameters
# calls to draw_header 
#          draw_graph
#          draw_legend
#          draw_footer
def draw(graph: GraphNode):
    node_to_explore = graph
    running = True
    for child in graph.paths:
        format_link_text(child, graph.rel_path) 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q :
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # not the cleanest logic :::improve
                node_to_explore =  node_hovered
                print("to expand ", node_to_explore)
                 
        # RENDER YOUR GAME HERE
        draw_header(node_to_explore.rel_path)
        draw_legend()
        draw_graph(node_to_explore)
        draw_footer()
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(15)  # limits FPS to 15


# ----------------------------------------------------------------- test
# for dummy testing purposes
def main():
    graph = GraphNode("head")
    graph.paths = [GraphNode(str(x)) for x in range(10)]
    draw(graph) 
    pygame.quit()

if __name__=="__main__":
    main()
