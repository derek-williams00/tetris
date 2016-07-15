from random import randint

import pygame
from pygame.locals import *

class Tetris:
    display_size = (528, 704)
    board_size = (10, 20)
    grid_pos = (32, 32)

    def __init__(self):
        self.grid = Grid(*self.board_size)
        self.display = pygame.display.set_mode(self.display_size)
        self.clock = pygame.time.Clock()
        self.exit = False
        self.falling_tetromino = Tetromino()

    def draw(self):
        '''Draws all of the elements of the display in the window'''
        self.display.fill((32, 32, 32))
        self.grid.draw(self.display, self.grid_pos)
        pygame.display.update()

    def new_tetromino(self):
        tetrominos = [Tetromino]
        self.falling_tetromino = tetrominos[randint(0, len(tetrominos)-1)]()
        grid = self.grid
        self.falling_tetromino.spawn(self.grid)

    def handle_events(self):
        pygame.event.pump()

    def is_tetromino_fallen(self):
        if self.falling_tetromino.fallen:
            self.new_tetromino()

    def loop(self):
        while not self.exit:
            self.handle_events()
            self.falling_tetromino.fall(self.grid)
            self.is_tetromino_fallen()
            self.draw()
            self.clock.tick(1)

class Grid:
    def __init__(self, width, height):
        self.matrix = list()
        for column_index in range(0, width):
            column = list()
            for square_index in range(0, height):
                column.append(EmptySquare())
            self.matrix.append(column)

    def width(self):
        '''returns the width of the grid matrix in pixils'''
        return self.cell_width * len(self.matrix)

    def height(self):
        '''returns the height of the grid matrix in pixils'''
        return self.cell_width * len(self.matrix[0])

    def get_square(self, x, y):
        return self.matrix[x][y]

    def empty_pos(self, x, y):
        self.matrix[x][y] = EmptySquare()

    def remove_square(self, square):
        for column in self.matrix:
            for itsquare in column:
                if itsquare == square:
                    self.empty_pos(*self.get_pos(itsquare))

    def get_pos(self, square):
        for column in self.matrix:
            try:
                return tuple([self.matrix.index(column), column.index(square)])
            except ValueError:
                pass
        raise ValueError("Square is not in grid")

    def set_pos(self, square, x, y):
        self.remove_square(square)
        self.matrix[x][y] = square

    def is_square_empty(self, x, y):
        if type(self.get_square(x, y)) == EmptySquare:
            return True
        else:
            return False

    def rel_set_pos(self, square, delta_x, delta_y):
        start_pos = self.get_pos(square)
        new_x = start_pos[0] + delta_x
        new_y = start_pos[1] + delta_y
        self.set_pos(square, new_x, new_y)

    def draw(self, surface, pos):
        x = pos[0]
        y = pos[1]
        for column in self.matrix:
            for square in column:
                square.draw(surface, (x, y))
                y += square.width
            x += square.width
            y = pos[1]  


class Square:
    width = 32
    
    def __init__(self):
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

    def __str__(self):
        return 'Square'

    def draw(self, surface, pos):
        pygame.draw.rect(surface, self.color, (pos[0], pos[1], self.width, self.width), 0)


class EmptySquare(Square):
    color = (16, 16, 16)

    def __init__(self):
        pass
    
    def __str__(self):
        return 'Empty'


class Tetromino:
    def __init__(self):
        self.squares = (Square(), Square(), Square(), Square())
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.fallen = False
        for square in self.squares:
            square.color = self.color

    def spawn(self, grid):
        y = 0
        for square in self.squares:
            grid.set_pos(square, 4, y)
            y += 1
    
    def fall(self, grid):
        new_positions = dict()
        old_positions = dict()
        for square in self.squares:
            old_positions[square] = (grid.get_pos(square)[0], grid.get_pos(square)[1])
            new_positions[square] = (grid.get_pos(square)[0], grid.get_pos(square)[1]+1)
            grid.remove_square(square)
        try:
            for square, pos in new_positions.items():
                if grid.is_square_empty(*pos):
                    grid.set_pos(square, pos[0], pos[1])
                else:
                    raise IndexError  ## Bad practice but only implementation that works
        except IndexError:
            for square, pos in old_positions.items():
                grid.set_pos(square, pos[0], pos[1])
            self.fallen = True

    def rotate(self):
        pass


class JTetromino(Tetromino):
    ori0 = [False, True, False,
            False, True, False,
            True, True, False]
    
    ori1 = [True, False, False,
            True, True, True,
            False, False, False]
    
    ori2 = [False, True, True,
            False, True, False,
            False, True, False]
    
    ori3 = [False, False, False,
            True, True, True,
            False, False, True]
    
    rotaions = [ori0, ori1, ori2, ori3]

    def spawn(self, grid):  #Work on this
        pass

    def rotate(self):
        current_index = self.rotations.index(self.ori)


if __name__ == '__main__':
	game = Tetris()
	game.draw()
	game.falling_tetromino.spawn(game.grid)
	game.loop()
	#pygame.quit()
	#quit()
