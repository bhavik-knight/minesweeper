# button class to draw the button
from constants import *
from texts import Fonts


class Button(object):
    # constructor
    def __init__(self, color, x, y, width=button_width, height=button_height, text=None):
        self.__color = colors[color]
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__text = text

    # getters and setters
    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = colors[color]

    def set_text(self, text):
        self.__text = text

    def get_button_rectangle(self):
        return pygame.Rect((self.__x, self.__y), (self.__width, self.__height))

    # draw the button on the game window
    def draw_button(self, window):
        """
        :param window: an object, the game window
        :return: None, just draw the button
        """
        text = Fonts(self.__text, color="black", bg_color="white")
        text_box = text.get_text_box()

        x, y = self.get_button_rectangle().center
        pos_x = x - text_box.get_width() // 2
        pos_y = y - text_box.get_height() // 2

        pygame.draw.rect(window, self.get_color(), self.get_button_rectangle())
        text.display_text_box(window, pos_x, pos_y)
