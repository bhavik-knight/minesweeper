import sys
from constants import *
from buttons import Button
from grid import Grid
from texts import Fonts


# game window
game_window = pygame.display.set_mode((window_width, window_height))

# game variables
grid_dimension = 0
num_mines = 0


# base state of the game
def base_state():
    # set a caption for intro
    pygame.display.set_caption("Introduction")

    # game window

    # CS50 text
    cs50 = Fonts("<< CS50 Final Project >>", "crimson")
    cs50.set_text_size(48)
    pos_x = (window_width - cs50.get_text_box().get_width() - text_padding) // 2
    pos_y = 0
    cs50.display_text_box(game_window, pos_x, pos_y)

    # the welcome text
    welcome = Fonts("<< Welcome to Minesweeper >>", "cyan")
    welcome.set_text_size(32)
    pos_x = (window_width - welcome.get_text_box().get_width() - text_padding) // 2
    pos_y = window_height // 4
    welcome.display_text_box(game_window, pos_x, pos_y)

    # coder name
    coder = Fonts("<< coded by:~ Bhavik Knight >>", "yellow")
    pos_x = (window_width - coder.get_text_box().get_width() - text_padding) // 2
    pos_y = window_height // 3
    coder.display_text_box(game_window, pos_x, pos_y)

    # display choices to select a mode
    mode_choice = Fonts("<< Please choose your mode >>", "green")
    pos_x = (window_width - mode_choice.get_text_box().get_width()) // 2
    pos_y = window_height // 2
    mode_choice.display_text_box(game_window, pos_x, pos_y)

    # option a
    choice_a = Fonts("A.  9 x  9 grid with 10 mines", "white")
    pos_x = (window_width - choice_a.get_text_box().get_width()) // 2
    pos_y += choice_a.get_text_box().get_height()
    choice_a .display_text_box(game_window, pos_x, pos_y)

    # option b
    choice_b = Fonts("B. 16 x 16 grid with 40 mines", "white")
    pos_x = (window_width - choice_b.get_text_box().get_width()) // 2
    pos_y += choice_b.get_text_box().get_height()
    choice_b .display_text_box(game_window, pos_x, pos_y)

    # buttons will be towards bottom of window
    pos_y = 3 * window_height // 4
    pos_x = window_width // 4
    button_a = Button("white", pos_x, pos_y, 160, 32, "A")
    button_a.draw_button(game_window)

    pos_x = window_width // 2
    button_b = Button("white", pos_x, pos_y, 160, 32, "B")
    button_b.draw_button(game_window)

    # for escape key to exit the game at any point
    esc = Fonts("<< Press Esc key to quit the game >>", "magenta")
    pos_x = (window_width - esc.get_text_box().get_width() - text_padding) // 2
    pos_y = window_height - esc.get_text_box().get_height() - 16
    esc.display_text_box(game_window, pos_x, pos_y)

    # after drawing things, update window
    pygame.display.update()

    # clock tick
    pygame.time.Clock().tick(1) // 1000

    # game running flag
    running = True

    while running:
        # iterate through captured events
        for event in pygame.event.get():

            # game quit is captured
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # quit the game, if escape key is pressed
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            # capture mouse clicks
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # left click
                if event.button == 1:
                    x, y = event.dict["pos"]

                    # global variables
                    global grid_dimension, num_mines

                    # check which button is pressed A or B
                    if button_a.get_button_rectangle().collidepoint(x, y):
                        grid_dimension, num_mines = 9, 10
                        running = False

                    elif button_b.get_button_rectangle().collidepoint(x, y):
                        grid_dimension, num_mines = 16, 40
                        running = False

    # delay for some time
    pygame.time.wait(1000)

    # clear the window
    game_window.fill(colors["black"])

    # call to the game loop
    game_loop()


# main game loop
def game_loop():
    # set a caption for the game
    pygame.display.set_caption("Minesweeper")

    # game variables
    timer = 0
    switched_on = False

    # grid location
    grid_x = (window_width - (grid_dimension * tile_size)) // 2
    grid_y = (window_width - (grid_dimension * tile_size)) // 3

    # instantiate and draw the grid
    grid = Grid(grid_x, grid_y, grid_dimension, num_mines)
    grid.draw_grid()

    # result fonts
    result_fonts = Fonts(text="", color="black")
    center_x, center_y = 0, 0

    # game running flag
    running = True
    while running:
        # timer and mines
        timer_text = f"time: {timer:<6}"
        mines_text = f"mines: {grid.get_mine_count():2}"

        # update the display
        pygame.display.update()

        # switch on timer
        if switched_on:
            clock = pygame.time.Clock()
            timer += clock.tick(1) // 1000

        # won/lost
        result = ""

        # look for different events while game is running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # check for roller click
                if event.button == 2:
                    click = "multi"
                else:
                    # check for left and/or right click
                    click = "left" if event.button == 1 else "right"

                # turn on timer after first mouse click
                switched_on = True

                # click position
                x, y = event.dict["pos"]

                result = grid.update(x, y, click)
                mines_text = f"mines: {grid.get_mine_count():2}"

        # show timer and mines
        timer_font = Fonts(timer_text, "yellow")
        timer_font.display_text_box(game_window, text_padding, text_padding)

        mines_font = Fonts(mines_text, "cyan")
        mines_font.display_text_box(game_window, -text_padding, text_padding)

        # window center
        center_y = text_padding

        # display result
        if result == "lost":
            # display game over text on the window
            result_fonts.set_color("red")
            result_fonts.set_text("You Lost")
            center_x = (window_width - result_fonts.get_text_box().get_width() - text_padding) // 2
            result_fonts.display_text_box(game_window, center_x, center_y)
            switched_on = False
            running = False

        elif result == "won":
            # display winner text on the window
            result_fonts.set_color("green")
            result_fonts.set_text("You WON!")
            center_x = (window_width - result_fonts.get_text_box().get_width() - text_padding) // 2
            result_fonts.display_text_box(game_window, center_x, center_y)
            switched_on = False
            running = False

    # update the display
    pygame.display.update()

    # wait 3 seconds
    pygame.time.wait(3 * 1000)

    # result fonts, make them disappear
    result_fonts.set_color("black")
    result_fonts.display_text_box(game_window, center_x, center_y)

    # quit the display
    game_over_state()


# game over state
def game_over_state():
    # set display caption
    pygame.display.set_caption("Play Again?")

    # button position
    center_x = (window_width - button_width) // 2
    center_y = text_padding

    # restart.display_text_box(game_window, center_x, center_y)
    restart_button = Button(color="white", x=center_x, y=center_y, text="restart")
    restart_button.draw_button(game_window)
    pygame.display.update()

    # clock tick
    pygame.time.Clock().tick(1) // 1000

    # display update
    pygame.display.update()

    while True:
        # catch different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                # left click
                if event.button == 1:
                    x, y = event.dict["pos"]

                    # check for restart
                    if restart_button.get_button_rectangle().collidepoint(x, y):
                        # clear the game window
                        game_window.fill(colors["black"])

                        # goto bast state
                        base_state()
