import random
from copy import deepcopy


class wordSearchGenerator():
    DEFAULT_CHAR = '_'
    directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]

    def __init__(self, words, grid_size=None):
        if not grid_size:
            self.grid_size = max([len(word) for word in words])
        else:
            self.grid_size = grid_size
        
        self.words = words
        self.char_grid = []
        for _ in range(self.grid_size):
            self.char_grid.append([self.DEFAULT_CHAR] * (self.grid_size))

    def display_char_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                print(self.char_grid[i][j],end=' ')
            print()

    def generate_word_search(self, filename=None):
        for word in self.words:
            if not self.fit_word(word):
                return False
        
        for i in range(len(self.char_grid)):
            if self.char_grid[i] is self.DEFAULT_CHAR:
                self.char_grid[i] = chr(random.randint(ord('a'), ord('z')))
        return True

    def fit_word(self, word):
        origins = random.sample(list(range(self.grid_size ** 2)), self.grid_size ** 2)
        directions = random.sample(self.directions, len(self.directions))

        for origin in origins:
            for dir in directions:
                origin_coord = [origin//self.grid_size, origin%self.grid_size]
                if self.insert_word(word, origin_coord, dir):
                    return True
        else:
            return False

    def insert_word(self, word, origin, dir):
        temp_char_grid = deepcopy(self.char_grid)
        char_row = origin[0]
        char_col = origin[1]
        for char in word:
            if char_row not in range(self.grid_size) or char_col not in range(self.grid_size) or not (temp_char_grid[char_row][char_col] is char or temp_char_grid[char_row][char_col] is self.DEFAULT_CHAR):
                return False
            temp_char_grid[char_row][char_col] = char
            char_row += dir[0]
            char_col += dir[1]        

        self.char_grid = temp_char_grid
        return True
            