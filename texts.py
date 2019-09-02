from constants import *


class Fonts:

    # constructor
    def __init__(self, text, color, bg_color="black_bg"):
        # self.__window = win
        self.__text = text
        self.__color = colors[color]
        self.__bg_color = colors[bg_color]
        self.__text_size = font_size
        pygame.font.init()

    # getters and setters
    def get_color(self):
        return self.__color

    def get_text_size(self):
        return self.__text_size

    def set_color(self, color):
        self.__color = colors[color]

    def set_bg_color(self, color):
        self.__bg_color = colors[color]

    def set_text(self, text):
        self.__text = text

    def set_text_size(self, text_size):
        self.__text_size = text_size

    def get_text_box(self):
        # generate fonts
        text = pygame.font.Font(font_type, self.get_text_size())

        # render text
        surface = text.render(self.__text, True, self.__color, self.__bg_color)
        return surface

    def display_text_box(self, window, pos_x, pos_y):
        # set some font
        text_box = self.get_text_box()

        # text_size
        text_width, text_height = text_box.get_size()

        # position of text on the game window
        if pos_x < 0:
            text_position = pos_x + window_width - text_width, pos_y
        else:
            text_position = pos_x, pos_y

        # draw the text-box on the game window
        window.blit(text_box, text_position)
