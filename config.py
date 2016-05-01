import pygame

FPS = 10 # frames per second to update the screen
WINDOWWIDTH = 700 # width of the program's window, in pixels
WINDOWHEIGHT = 600 # height in pixels
SPACESIZE = 50 # width & height of each space on the board, in pixels
BOARDWIDTH = 8 # how many columns of spaces on the game board
BOARDHEIGHT = 8 # how many rows of spaces on the game board
WHITE_TILE = 'WHITE_TILE' # an arbitrary but unique value
BLACK_TILE = 'BLACK_TILE' # an arbitrary but unique value
EMPTY_SPACE = 'EMPTY_SPACE' # an arbitrary but unique value
HINT_TILE = 'HINT_TILE' # an arbitrary but unique value
ANIMATIONSPEED = 25 # integer from 1 to 100, higher is faster animation
INFINITY = 99999999

# Amount of space on the left & right side (XMARGIN) or above and below
# (YMARGIN) the game board, in pixels.
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * SPACESIZE)) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * SPACESIZE)) / 2)

#              R    G    B
WHITE      = (255, 255, 255)
BLACK      = (  0,   0,   0)
GREEN      = (  0, 155,   0)
BRIGHTBLUE = (  0,  50, 255)
BROWN      = (153,  0,   0)
DARKBLUE   = (95, 158, 160)
BBROWN    = (120,80,39)
BBBROWN    = (101,67,33)
BBBBROWN =(51,0,0)

TRANSPARENT=pygame.Color(255,255,255,0)
TEXTBGCOLOR1 = BRIGHTBLUE
TEXTBGCOLOR2 = GREEN
GRIDLINECOLOR = BBBROWN
TEXTCOLOR = WHITE
TEXTCOLOR1 = BROWN
HINTCOLOR = BBROWN
TEXTCOLOR2 = BBBROWN
