import pygame

# game window
window_width = 800
window_height = 640

# set font
font_size = 24
font_type = "fonts/Monaco.ttf"

# extra constants
text_padding = font_size // 3
tile_size = 32
button_width = 160
button_height = 32

# colors dict
colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255,),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "crimson": (220, 20, 60),
    "black_bg": (1, 1, 1)
}

# tiles dictionary, populate with different types of tiles
image_dict = dict()

# non-numbered tiles
image_dict["tile"] = pygame.image.load("images/tile.png")
image_dict["empty"] = pygame.image.load("images/empty.png")
image_dict["flag"] = pygame.image.load("images/flag.png")
image_dict["mine"] = pygame.image.load("images/mine.png")
image_dict["wrong_flag"] = pygame.image.load("images/wrong_flag.png")

# numbered tiles
for i in range(1, 9):
    image_dict[str(i)] = pygame.image.load(f"images/{i}.png")
