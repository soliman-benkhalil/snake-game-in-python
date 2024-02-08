import random  # for the snake food to be randomally
import curses  # for snake shape and movement ,.....

screen = curses.initscr()  # return window object
curses.curs_set(0)

screen_height, screen_width = screen.getmaxyx()  # unpacking

window = curses.newwin(
    screen_height, screen_width, 0,
    0)  # we make window and determine the start of it from the point (0,0)

window.keypad(1)  # 1 means true and receive input from the keyboard

window.timeout(
    125
)  # how the screen reads the input and plot the input every specific time (receive the reload of the input)

snake_x = screen_width // 4  # here we determined the initial position of the snake
# it means that the snake will appear at the middle of the screen and in the firs quarter place comparing to the width
snake_y = screen_height // 2

snake = [  # represent tha body of the snake ... head , body ,and tail
    [snake_y, snake_x], [snake_y, snake_x - 1], [snake_y, snake_x - 2]
]
food = [screen_height // 2,
        screen_width // 2]  # represent the initial food position of the snake

window.addch(food[0], food[1],
             curses.ACS_DIAMOND)  # add the character of the food to the screen
key = curses.KEY_RIGHT  # the initial direction of the snake

score = 0
window.addstr(0, 2, f"Score: {score}")  # display the score on the screen
while True:
    next_key = window.getch()  # get the next input from the user
    # if the user doesn't input anything the snake will continue in the same direction
    key = key if next_key == -1 else next_key
    if snake[0][0] in [0, screen_height] or snake[0][1] in [
            0, screen_width] or snake[0] in snake[1:]:
        curses.endwin()  # restore the terminal to its normal operating mode
        window.addstr(screen_height // 2, (screen_width - 26) //
                      2, "U r Norm Lol .. Game Over")
        window.refresh()
        quit()  # exit the program

    new_head = [
        snake[0][0], snake[0][1]
    ]  # here we will determine the direction of the snake and we give intial value to the new head then if the snake will move we will add the new head to the snake list
    # we will check now the directions of the snake and we will move it in the direction of the user
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    snake.insert(
        0, new_head
    )  # insert the new head to the head of the snake in ather way we make the snake get taller
    # we will check if the snake ate the food or not
    if snake[0] == food:
        food = None
        while food is None:
            new_food = [  # we made new food in a random place on the screen
                random.randint(
                    1, screen_height - 2
                ),  # -1 here because we do not want the food to be in the border of the screen
                random.randint(1, screen_width - 2)
            ]
            # to make sure whether the food is in the snake or not and if it is in the snake it will be None and will be regenerated
            food = new_food if new_food not in snake else None
            window.addch(
                food[0], food[1], curses.ACS_DIAMOND
            )  # add the food to the screen after the snake eat the exisiting food
            score += 3  # increase the score by 3 for each food eaten
            # display the score on the screen
            window.addstr(0, 2, f"Score: {score}")
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')
    window.addch(snake[0][0], snake[0][1],
                 curses.ACS_CKBOARD)  # ACS_CKBOARD is the shape of the snake
