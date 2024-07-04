#import modules for game
import curses
import random

# initialize the curses library to create our screen
screen = curses.initscr()

# hide the mouse cursor
curses.curs_set(0)

# get max screen height and width
screen_hight, screen_width = screen.getmaxyx()

# create a new window
window = curses.newwin(screen_hight,screen_width,0,0)

# allow window to receive input from the keyboard
window.keypad(True)

# set the delay to update the screen
window.timeout(120)

# set the x,y coordinates of the initial position of snake's head
snk_x = screen_width // 4
snk_y = screen_hight // 2

# define the initial position fo snak's body
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# create the food in the middle of window
food = [screen_hight // 2, screen_width // 2]

# add the food by using PI character from curses module
window.addch(food[0], food[1], curses.ACS_PI)

# set inithial movoement direction to right
key = curses.KEY_RIGHT

# create game loop that loops forever until player loses or quits the game
while True:
    next_key = window.getch()
    key= key if next_key == -1 else next_key

    if snake[0][0] in [0, screen_hight] or \
    snake[0][1] in [0, screen_width] or \
    snake[0] in snake[1:]:
        curses.endwin()
        quit()

# set the new position of the snake head based on the direction
    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0] =new_head[0]+1
    if key == curses.KEY_UP:
        new_head[0] =new_head[0]-1
    if key == curses.KEY_RIGHT:
        new_head[1] =new_head[1]+1
    if key == curses.KEY_LEFT:
        new_head[1] =new_head[1]-1
    
    # insert the new head to the first position of snake list
    snake.insert(0, new_head)
    
    # check if snake ate the food
    if snake[0] == food:
            food = None
    
    # while food is removed generate new food in a random plase on the screen
    while food is None:
            new_food = [
                random.randint(1, screen_hight-1),
                random.randint(1, screen_width-1)
            ]
            food = new_food if new_food not in snake else None
            if food is not None:
                window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tall = snake.pop()
        window.addch(tall[0], tall[1], ' ')
        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)