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

    def draw(self):
        self.display.fill((32, 32, 32))
        self.grid.draw(self.display, self.grid_pos)
        pygame.display.update()

    def new_tetromino(self):
        pass

    def loop(self):
        pass


class Grid:
    matrix = list()
    
    def __init__(self, width, height):
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

    def set_pos(self, square, x, y):
        self.remove_square(square)
        self.matrix[x][y] = square

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
    squares = list()

    def spawn(self):
        pass
            


class JTetromino(Tetromino):
    grid = Grid(3, 3)
    


if __name__ == '__main__':
	game = Tetris()
	game.loop()
	#pygame.quit()
	#quit()
