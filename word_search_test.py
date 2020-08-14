from word_search_solver import wordSearchSolver
from word_search_generator import wordSearchGenerator

# solver = wordSearchSolver()

# solver.load_word_grid_from_file('word_grid.txt')
# with open('word_list.txt') as word_list_file:
#     word_list = word_list_file.read().strip().split()

# print(solver.grid)

# print(solver.find_words(word_list))

word_gen = wordSearchGenerator(['cat','cab','rat','rabbit'])
# word_gen.display_char_grid()
# print(word_gen.insert_word('cat',0,[1,1]))
# print(word_gen.insert_word('car',0,[1,0]))
# print(word_gen.insert_word('rat',20,[0,1]))
if word_gen.generate_word_search():
    word_gen.display_char_grid()
else:
    print('Unlucky - Try Again')