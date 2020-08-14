from functools import reduce

class wordSearchSolver():

    check_directions = [[1,0],[-1,0],[0,-1],[0,1],[1,-1],[1,1],[-1,-1],[-1,1]] # [vertical (+1:up),horizontal (+1:right)]

    def __init__(self):
        self.grid = []
        return

    # TODO: ensure grid is N x N (square)
    def load_word_grid_from_file(self, filename):
        with open(filename) as word_search_file:
            self.grid = word_search_file.readlines()
            for i in range(len(self.grid)):
                    self.grid[i] = [char for char in self.grid[i].strip()]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
    
    def find_words(self, word_list):
        return reduce(lambda a,b: a and b, [self.__find_word(word) for word in word_list], True)
    
    def __find_word(self, word):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] is word[0]:
                    for dir in self.check_directions:
                        if self.__check_direction(dir, word, [i,j]):
                            return True
        return False

    def __check_direction(self, dir, word, char_coord):
        char_row = char_coord[0]
        char_col = char_coord[1]
        for char in word:
            if char_row not in range(0,self.rows) or char_col not in range(0,self.cols) or self.grid[char_row][char_col] is not char:
                return False
            char_row += dir[0]
            char_col += dir[1]
        return True