import pygame
import math

#Connect Four Game

#Colors
_WHITE = (255, 255, 255)
_BLACK = (0, 0, 0)
_RED = (255, 0, 0)
_BLUE = (0, 0, 255)
_YELLOW = (255, 255, 0)


#Variables
board_size = (7 * 100 + 10, 7 * 100 + 5)
board_line_width = 5
board_space_size = 100
board_pieces_array = [[0 for i in range(7)] for j in range(6)]
circle_radius = board_space_size / 2 - 15


#Board init
pygame.init()
gameDisplay = pygame.display.set_mode(board_size)
gameDisplay.fill(_WHITE)
pygame.display.set_caption("Connect Four")
pygame.display.update()


#Functions
#Draws the horizontal board and border lines
def draw_horizontal_lines_and_borders(board_size):
	size = board_size[0] - 105
	for i in range(8):
		if i == 0:
			pygame.draw.rect(gameDisplay, _BLUE, [0, 100, board_line_width, size])
		else:
			pygame.draw.rect(gameDisplay, _BLUE, [i * board_space_size + 5, 100, board_line_width, size])


#Draws the vertical lines with borders
def draw_vertical_lines_and_borders(board_size):
	for i in range(8):
		pygame.draw.rect(gameDisplay, _BLUE, [0, (i + 1) * board_space_size, board_size[1], board_line_width])


#Returns the current position of the mouse when called
def get_mouse_x_position(board_size):
	position = pygame.mouse.get_pos()
	position = int(math.floor((position[0] - 5) / board_space_size))
	return position


#Draws the entire board, combines all board drawing functions
def draw_entire_board(board_size):

	draw_horizontal_lines_and_borders(board_size)
	draw_vertical_lines_and_borders(board_size)


#Find true place to put the circle in
def find_true_position(position):
	pass


# Draws a cirecle in the position given @todo finish the function
def draw_circle(color):
	position_to_put = [get_mouse_x_position(board_size), 0]
	i = len(board_pieces_array) - 1
	while i >= 0:
		if board_pieces_array[position_to_put[0]][i] == 0:
			position_to_put[1] = i
		i -= 1
	pygame.draw.circle(gameDisplay, color, position_to_put, circle_radius)
	print position_to_put




#Main logic of the game
def run(board_size):
	#Function Variables
	game_exit = False
	current_player = 0

	while not game_exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit = True

		draw_entire_board(board_size)
		draw_circle(_YELLOW)
		pygame.display.update()

run(board_size)