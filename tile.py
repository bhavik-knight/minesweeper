from constants import *

game_window = pygame.display.set_mode((window_width, window_height))


class Tiles(object):
    # constructor
    def __init__(self, row, col):
        self.__location = row, col
        self.__open = False
        self.__mine = False
        self.__flag = False
        self.__wrong_mine = False
        self.__neighbor_mine_count = 0

    def is_opened(self):
        """return true if tile is open, false otherwise"""
        return self.__open

    def open_tile(self):
        """set this tile's open property to true"""
        self.__open = True

    def is_mine(self):
        """return true if this tile is mine, false otherwise"""
        return self.__mine

    def set_mine(self, value: bool):
        """set this mine to a boolean value"""
        self.__mine = value

    def is_flagged(self):
        """return true if tile is flagged, false otherwise"""
        return self.__flag

    def set_flag(self, value: bool):
        """set flag to a boolean value"""
        self.__flag = value

    def get_location(self):
        """return a tuple, this tile's location in grid"""
        return self.__location

    def get_neighbor_mine_count(self):
        """return an int, number of mines surrounding this tile"""
        return self.__neighbor_mine_count

    def set_neighbor_mine_count(self, number: int):
        """set this tile to an int that is number of surrounding mines"""
        self.__neighbor_mine_count = number

    def is_wrong_mine(self):
        """return true if tile is not mine, false otherwise"""
        return self.__wrong_mine

    def open_wrong_mine(self):
        """set this tile's wrong mine property to true"""
        self.__wrong_mine = True

    def draw_tile(self, window=game_window):
        # for numbered tiles, the count of neighboring mines
        count = self.get_neighbor_mine_count()

        # draw this tile on game window depending on which kind of tile it is
        if self.is_wrong_mine():
            window.blit(image_dict["wrong_flag"], self.get_location())
        elif self.is_flagged():
            window.blit(image_dict["flag"], self.get_location())
        elif not self.is_opened():
            window.blit(image_dict["tile"], self.get_location())
        else:
            if self.is_mine():
                window.blit(image_dict["mine"], self.get_location())
            elif count > 0:
                window.blit(image_dict[str(count)], self.get_location())
            else:
                window.blit(image_dict["empty"], self.get_location())
