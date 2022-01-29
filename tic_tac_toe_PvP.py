import turtle


def initialize_screen():
	global screen, board, last_player
	screen = turtle.Screen()
	screen.setup(800, 800)
	screen.setworldcoordinates(-5, -5, 5, 5)
	screen.bgcolor("light blue")
	screen.title("Tic-Tac-Toe - e-yantra")
	turtle.hideturtle()
	turtle.speed(10)
	turtle.delay(1)  # Making the drawing visible looks better

	board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	last_player = "O"

	return screen


def draw_board():
	turtle.pencolor("navy blue")
	turtle.penup()
	turtle.goto(-1.67, -5)
	turtle.pendown()
	turtle.goto(-1.67, 5)

	turtle.penup()
	turtle.goto(1.67, -5)
	turtle.pendown()
	turtle.goto(1.67, 5)

	turtle.penup()
	turtle.goto(-5, -1.67)
	turtle.pendown()
	turtle.goto(5, -1.67)

	turtle.penup()
	turtle.goto(-5, 1.67)
	turtle.pendown()
	turtle.goto(5, 1.67)


def draw_circle(x, y):
	turtle.penup()
	turtle.goto(x, y-1.5)  # Subtracting radius so that x,y is the center of the circle
	turtle.pendown()
	turtle.pencolor("white")
	turtle.circle(1.5, steps=30)


def draw_x(x, y):
	turtle.pencolor("black")
	turtle.penup()
	turtle.goto(x+1.4, y-1.4)
	turtle.pendown()
	turtle.goto(x-1.4, y+1.4)

	turtle.penup()
	turtle.goto(x-1.4, y-1.4)
	turtle.pendown()
	turtle.goto(x+1.4, y+1.4)


def draw(i, j, p):
	left_y = -5 + 3.33*(2-i)
	right_y = -1.67 + 3.33*(2-i)
	y = (left_y+right_y) / 2

	left_x = -5 + 3.33*j
	right_x = -1.67 + 3.33*j
	x = (left_x+right_x)/2

	if p == "X":
		draw_x(x, y)
	else:
		draw_circle(x, y)


def gameover(board):
	combos = []

	for row in board:
		combos.append(row)  # Add horizontal combinations

	for i in range(3):
		column = []
		for j in range(3):
			column.append(board[j][i])
		combos.append(column)  # Add vertical combinations

	combos.append([board[i][i] for i in range(3)])  # Diagonal up to down
	combos.append([board[i][2-i] for i in range(3)])  # Diagonal down to up

	zeroes = 0
	for combo in combos:
		if len(set(combo)) == 1 and combo[0] != 0:
			return 1 if combo[0] == "X" else 2  # Player has won
		for i in combo:
			if i == 0:
				zeroes += 1

	if zeroes == 0:  # Tie
		return 3

	return 0  # Game not over


def play(x, y):
	if x < -1.67:
		vertical = 0
	elif x > 1.67:
		vertical = 2
	else:
		vertical = 1

	if y < -1.67:
		horizontal = 2
	elif y > 1.67:
		horizontal = 0
	else:
		horizontal = 1

	global last_player, board
	if board[horizontal][vertical] == 0:
		player = "X" if last_player == "O" else "O"
		last_player = player
		board[horizontal][vertical] = player

		draw(horizontal, vertical, player)

		status = gameover(board)

		if status != 0:
			if status == 1:
				text = f"{name_1} has won."
			elif status == 2:
				text = f"{name_2} has won."
			elif status == 3:
				text = "The game ended in a tie."
			answer = screen.textinput("Game Over!", text + " Would you like to play again? (click cancel to quit)")

			screen.clear()
			if answer is None:
				screen.bye()
			else:
				reinitialize_screen()


def reinitialize_screen():
	initialize_screen()
	draw_board()
	screen.onclick(play)


def input_names_of_player():
	global name_1, name_2
	name_1 = turtle.textinput("Setup Game", "Input Name of Player 1")
	name_2 = turtle.textinput("Setup Game", "Input Name of Player 2")


if __name__ == "__main__":
	initialize_screen()
	draw_board()  # Draw the board for the first time.
	input_names_of_player()
	screen.onclick(play)
	turtle.mainloop()
