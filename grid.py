import random
from constants import tile_size
from tile import Tiles


class Grid(object):
    # constructor
    def __init__(self, x, y, grid_size=9, mines=10):
        self.__x = x
        self.__y = y
        self.__N = grid_size
        self.__NUM_MINES = mines
        self.__mines_count = mines
        self.__grid_dict = dict()
        self.__mines_dict = dict()

        # generate the grid when the new instance is made
        self.generate_grid(self.__N, self.__NUM_MINES)

    # getters and setters
    def get_grid_dict(self):
        return self.__grid_dict.copy()

    def get_grid_size(self):
        return self.__N

    def get_mine_count(self):
        return self.__mines_count

    def set_mine_count(self, mines_count):
        self.__mines_count = mines_count

    def get_mines_dict(self):
        return self.__mines_dict.copy()

    def get_neighbor_tiles(self, row, col):
        # current cell is (x, y) there are total 8 neighbors
        # top:(x, y - 1), top-left:(x - 1, y - 1) , top-right:(x + 1, y - 1)
        # left:(x - 1, y), right:(x + 1, y)
        # bottom:(x, y + 1), bottom-left: (x - 1, y + 1), bottom-right: (x + 1, y + 1)
        # all those neighbors can be achieved by adding (-1, 0 or 1) to (x, y)
        # 2 positions (x, y), 3 possible choices (-1, 0, 1) => 2^3 = 8 neighbors

        # to store neighbors (index) -> tile
        neighbors = dict()

        # bounds of grid for indexing
        lo, hi = 0, self.get_grid_size()

        # iterate through all neighbors
        for i in range(-1, 2):
            for j in range(-1, 2):
                # check for this neighbor
                check_row, check_col = row + i, col + j

                if lo <= check_row < hi and lo <= check_col < hi:
                    neighbor_tile = self.get_grid_dict()[(row + i, col + j)]
                    neighbors[(check_row, check_col)] = neighbor_tile

        # return a copy to prevent accidental modifications
        return neighbors.copy()

    # generate the grid
    def generate_grid(self, n, m):
        """
        :param n: an int, grid size
        :param m: an int, number of mines
        :return: None, just generate a grid of nxn size with m mines
        """

        # total size of grid must be greater than number of mines
        assert n * n > m, "#m <= nxn; where, n = grid size, #m = number of mines"

        # generate different type of tiles
        self.generate_tiles(n)
        # self.generate_mines_for_test()
        self.generate_mines()
        self.generate_numbered_tiles()

    # generate the tiles
    def generate_tiles(self, n):
        """
        :param n: an int, grid size
        :return: None, populate the grid with tiles: index(row, col) -> Tile
        """

        pos_y = self.__y

        # iterate through each row
        for row in range(n):
            pos_x = self.__x

            # iterate through each column in the row
            for col in range(n):
                tile = Tiles(pos_x, pos_y)
                self.__grid_dict[(row, col)] = tile
                pos_x += tile_size
            pos_y += tile_size

    # generate the mines
    def generate_mines(self):
        # mine counter
        count = 0

        # generate num_mines mine at random places in grid
        while count != self.__NUM_MINES:

            # select a random location for mine in the grid
            location = random.choice(list(self.get_grid_dict()))

            # check for location is already a mine, if so do nothing
            if location in self.get_mines_dict():
                continue

            # set a mine on this location in the grid
            mine = self.get_grid_dict()[location]
            count += 1
            mine.set_mine(True)
            self.__mines_dict[location] = mine

    # generate numbered tiles
    def generate_numbered_tiles(self):
        # helper function
        def mine_counter(check_tile):
            """
            :param check_tile: an object, a tile to be checked
            :return: an int, 1 if tile is mine, 0 otherwise
            """
            return 1 if check_tile.is_mine() else 0

        # iterate over grid
        for row, col in self.get_grid_dict():
            # for each tile count neighbor mines
            counter = 0

            # if this grid location is a mine, do nothing
            if self.get_grid_dict()[(row, col)].is_mine():
                continue

            # iterate over neighbors to count number of surrounding mines
            for tile in self.get_neighbor_tiles(row, col).values():
                counter += mine_counter(tile)

            # set a number to this tile, number is same as surrounding mines
            tile = self.get_grid_dict()[(row, col)]
            tile.set_neighbor_mine_count(counter)

    # convert a grid location to tile index
    def convert_grid_location_to_tile_index(self, x, y):
        """
        :param x: a float, x position on the game window
        :param y: a float, y position on the game window
        :return: a tuple, the index of this tile if it's in bound,
                    otherwise error indication (-1, -1)
        """
        # iterate over grid
        for tile_index, tile in self.get_grid_dict().items():
            tile_x, tile_y = tile.get_location()
            # if location somewhere inside a tile area, use that tile index
            if tile_x <= x <= tile_x + tile_size and \
                    tile_y <= y <= tile_y + tile_size:
                return tile_index

        # return out of bound index for mouse click outside grid
        return -1, -1

    # draw all tiles of grid
    def draw_grid(self):
        # iterate over tiles in the grid
        for tile in self.get_grid_dict().values():
            tile.draw_tile()

    # update the tile within the grid according to different clicks of mouse
    def update(self, x, y, click):
        """
        :param x: a float, x position on the game window
        :param y: a float, y position on the game window
        :param click: a string, left or right or multi clicks of mouse
        :return: None, if it's a right click, tile is flagged
                if it's a left click, reveal the tile at this position
                revealed tile could be either blank, mine or a numbered tile
                check if game is won
        """
        # bounds for indexing
        lo, hi = 0, self.get_grid_size()

        # update iff mouse click is within grid area
        try:
            tile_index = self.convert_grid_location_to_tile_index(x, y)
            assert (lo, lo) <= tile_index < (hi, hi)

        except AssertionError:
            # print("mouse is clicked outside boundaries of grid")
            pass

        else:
            # mouse click is within the grid now
            tile = self.get_grid_dict()[tile_index]
            flagged = tile.is_flagged()

            if click == "right":
                # proceed only if tile is not opened
                if not tile.is_opened():
                    if flagged:
                        self.set_mine_count(self.get_mine_count() + 1)
                    else:
                        self.set_mine_count(self.get_mine_count() - 1)
                    # toggle the flag status
                    tile.set_flag(not flagged)
                    tile.draw_tile()

            elif click == "left":
                # proceed only if tile is not opened
                if not tile.is_opened() and not tile.is_flagged():
                    if tile.is_mine():
                        return self.check_lost()
                    self.show_tile(tile_index[0], tile_index[1])
                    return self.check_won()

            elif click == "multi":
                # get all neighbors
                neighbor_tiles = self.get_neighbor_tiles(
                    tile_index[0], tile_index[1])

                # neighbor mines and flagged tiles count
                count_mines = tile.get_neighbor_mine_count()
                count_flags = sum(1 if tile.is_flagged() else 0
                                  for tile in neighbor_tiles.values())

                # if tile is opened and has at least one mine in neighbors
                if tile.is_opened() and count_mines > 0:
                    # neighboring flagged tiles and mines count are the same
                    if count_mines == count_flags:
                        for neighbor_tile in neighbor_tiles.values():
                            # if (predicted) flagged tile is not mine, game over
                            if neighbor_tile.is_flagged() and \
                                    not neighbor_tile.is_mine():
                                neighbor_tile.open_wrong_mine()
                                return self.check_lost()

                            # open neighbors which are neither open nor flagged
                            self.show_neighbors(tile_index[0], tile_index[1])
                        return self.check_won()

    # show the tile
    def show_tile(self, row, col):
        """
        :param row: an int, tile's row
        :param col: an int, tile's column
        :return: None, just draw the tile
        """
        # print("\n -- checking for -- ", row, col)
        tile = self.get_grid_dict()[(row, col)]
        tile.open_tile()
        tile.draw_tile()

        # if tile is empty, open neighbors recursively
        if tile.get_neighbor_mine_count() == 0:
            self.show_neighbors(row, col)

    # show neighbouring tiles
    def show_neighbors(self, row, col):
        """
         :param row: an int, tile's row
         :param col: an int, tile's column
         :return: None, just show neighboring tiles
                    tiles can be either mines, blanks or a numbered tile
         """

        # open the tile only iff
        # 1. it's not open already and
        # 2. it's not a mine and
        # 3. it's not flagged and
        for tile_index, tile in self.get_neighbor_tiles(row, col).items():
            if not (tile.is_mine() or tile.is_opened() or tile.is_flagged()):
                self.show_tile(tile_index[0], tile_index[1])

    # check if the game is won
    def check_won(self):
        """
        :return: a string, won if game is won, draw the final grid
        """
        # game is won when all tiles that are not mines, are opened
        count = sum(1 if tile.is_opened() and not tile.is_mine() else 0
                    for tile in self.get_grid_dict().values())

        # if count matches the actual non-mine opened tiles, game is won
        if count == self.__N ** 2 - self.__NUM_MINES:
            # turn mines into flags
            for tile in self.get_grid_dict().values():
                tile.open_tile()
                if tile.is_mine():
                    tile.set_flag(True)

            self.set_mine_count(0)
            self.draw_grid()
            return "won"

    # check if the game is lost
    def check_lost(self):
        """
        :return: a string, lost if the game is lost, draw the final grid
        """
        # draw all mines
        for tile in self.get_grid_dict().values():
            tile.open_tile()

        self.draw_grid()
        return "lost"

    # extra helper function for testing purpose only for 10 mines
    def generate_mines_for_test(self):
        lo, hi = 0, self.get_grid_size() - 1

        mines = {
            (lo, lo), (lo, hi), (hi, lo), (hi, hi), (hi // 2, hi // 2),
            (2, 0), (0, 2), (7, 3), (5, 2), (3, 7)
        }

        for x, y in mines:
            tile = self.get_grid_dict()[(x, y)]
            tile.set_mine(True)
            self.__mines_dict[(x, y)] = tile
