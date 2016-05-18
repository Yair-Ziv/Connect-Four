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
screen_size = (7 * 100 + 10, 7 * 100 + 5)
board_line_width = 5
board_space_size = 100
board_pieces_array = [[0 for i in range(7)] for j in range(6)]
circle_radius = board_space_size / 2 - 15
current_player = 0


#Board init
pygame.init()
gameDisplay = pygame.display.set_mode(screen_size)
gameDisplay.fill(_WHITE)
pygame.display.set_caption("Connect Four")
pygame.display.update()


#Functions
#Draws the horizontal board and border lines
def draw_horizontal_lines_and_borders(screen_size):
	size = screen_size[0] - 105
	for i in range(8):
		if i == 0:
			pygame.draw.rect(gameDisplay, _BLUE, [0, 100, board_line_width, size])
		else:
			pygame.draw.rect(gameDisplay, _BLUE, [i * board_space_size + 5, 100, board_line_width, size])


#Draws the vertical lines with borders
def draw_vertical_lines_and_borders(screen_size):
	for i in range(8):
		pygame.draw.rect(gameDisplay, _BLUE, [0, (i + 1) * board_space_size, screen_size[1], board_line_width])


#Returns the current position of the mouse when called
def get_mouse_x_position(screen_size):
	position = pygame.mouse.get_pos()
	position = int(math.floor((position[0] - 5) / board_space_size))
	return position


#Draws the entire board, combines all board drawing functions
def draw_entire_board(screen_size):
	draw_horizontal_lines_and_borders(screen_size)
	draw_vertical_lines_and_borders(screen_size)


#Find true place to put the circle in
def find_true_position(position):
	x_position = 55 + position[0] * board_space_size
	y_position = screen_size[1] - 50 - (100 * position[1])
	return [x_position, y_position]


#A function that checks if the game has been won, checks every column, row, diagonal and every way someone could have won the game
def check_won():
	#Checks if the current_player variable is more than the ammount alowed, meaning it's a tie
	if current_player >= 6 * 7:
		return True
	#Check rows
	for i in range(len(board_pieces_array)):
		for j in range(4):
			if board_pieces_array[i][j] == board_pieces_array[i][j + 1] and board_pieces_array[i][j + 1] == board_pieces_array[i][j + 2] and board_pieces_array[i][j + 2] == board_pieces_array[i][j + 3] and not board_pieces_array[i][j] == 0:
				return True

	#Check columns 
	for rows in range(len(board_pieces_array[0])):
		for columns in range(3):
			if board_pieces_array[columns][rows] == board_pieces_array[columns + 1][rows] and board_pieces_array[columns + 1][rows] == board_pieces_array[columns + 2][rows] and board_pieces_array[columns + 2][rows] == board_pieces_array[columns + 3][rows] and not board_pieces_array[columns][rows] == 0:
				return True

	#Check diagonals to the right up
	for rows in range(len(board_pieces_array[0]) - 3):
		for columns in range(3):
			if board_pieces_array[columns][rows] == board_pieces_array[columns + 1][rows + 1] and board_pieces_array[columns + 1][rows + 1] == board_pieces_array[columns + 2][rows + 2] and board_pieces_array[columns + 2][rows + 2] == board_pieces_array[columns + 3][rows + 3] and not board_pieces_array[columns][rows] == 0:
				return True



# Draws a cirecle in the position given @todo finish the function
def draw_circle(color):
	global current_player	
	position_to_put = [get_mouse_x_position(screen_size)] #Position for the piece to go, has only the x_pos for now
	#Itterates through the loop finding the lowest place that's empty and appends it to position_to_put
	#If the culomn is full return and don't do a thing
	if not board_pieces_array[len(board_pieces_array) - 1][position_to_put[0]] == 0:
		return 

	current_player += 1
	for i in range(len(board_pieces_array)):
		if board_pieces_array[i][position_to_put[0]] == 0:
			position_to_put.append(i)
			break

	#The position of the circle before the change and the draw
	init_position = position_to_put

	position_to_put = find_true_position(position_to_put)
	pygame.draw.circle(gameDisplay, color, position_to_put, 40)

	# Updates the board_pieces_array for what piece was sent where
	if color == _YELLOW:
		board_pieces_array[init_position[1]][init_position[0]] = 1
	elif color == _RED:
		board_pieces_array[init_position[1]][init_position[0]] = 2
	print check_won()



#Main logic of the game
def run(screen_size):
	#Function Variables
	game_exit = False

	while not game_exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if current_player % 2 == 0:
					draw_circle(_YELLOW)
				else:
					draw_circle(_RED)

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					game_exit = True

		draw_entire_board(screen_size)
		# draw_circle(_YELLOW)
		pygame.display.update()

run(screen_size)