#usr/bin/env Python

import random
import numpy as np
import pandas as pd
import tmxlib

#Valid move matrices
#Current cell is on the left side, cell being moved into is on the top
#I.e. movement goes left --> top
#These look silly now, but they'll be important once we start modifying the transition probabilities for
#each tile.

#"t" stands for "T-junction", "b" stands for "bend", "d" stands for "dead-end", and "s" stands for "straight"

#Move Up matrix

#     t1 t2 t3 d1 b1 b3 s1
#     ____________________
# t2 |1  1  1  1  1  1  1
# t3 |1  1  1  1  1  1  1
# t4 |1  1  1  1  1  1  1
# d4 |1  1  1  0  1  1  1
# b2 |1  1  1  1  1  1  1
# b4 |1  1  1  1  1  1  1
# s1 |1  1  1  1  1  1  1


move_up_rows = ['t2', 't3', 't4', 'd4', 'b2', 'b4', 's1']

move_up_columns = ['t1', 't2', 't3', 'd1', 'b1', 'b3', 's1']

move_up_matrix = np.array([[1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 0, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1]])

move_up_df = pd.DataFrame(move_up_matrix, index= move_up_rows, columns= move_up_columns)

#Move Down matrix

#     t2 t3 t4 d4 b2 b4 s1
#     ____________________
# t1 |1  1  1  1  1  1  1
# t2 |1  1  1  1  1  1  1
# t3 |1  1  1  1  1  1  1
# d1 |1  1  1  0  1  1  1
# b1 |1  1  1  1  1  1  1
# b3 |1  1  1  1  1  1  1
# s1 |1  1  1  1  1  1  1

move_down_rows = ['t1', 't2', 't3', 'd1', 'b1', 'b3', 's1']

move_down_columns = ['t2', 't3', 't4', 'd4', 'b2', 'b4', 's1']

move_down_matrix = np.array([[1, 1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 0, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1]])

move_down_df = pd.DataFrame(move_down_matrix, index= move_down_rows, columns= move_down_columns)

#Move Right matrix

#     t1 t2 t4 d2 b1 b2 s2
#     ____________________
# t1 |1  1  1  1  1  1  1
# t3 |1  1  1  1  1  1  1
# t4 |1  1  1  1  1  1  1
# d3 |1  1  1  0  1  1  1
# b3 |1  1  1  1  1  1  1
# b4 |1  1  1  1  1  1  1
# s2 |1  1  1  1  1  1  1

move_right_rows = ['t1', 't3', 't4', 'd3', 'b3', 'b4', 's2']

move_right_columns = ['t1', 't2', 't4', 'd2', 'b1', 'b2', 's2']

move_right_matrix = np.array([[1, 1, 1, 1, 1, 1, 1],
                              [1, 1, 1, 1, 1, 1, 1],
                              [1, 1, 1, 1, 1, 1, 1],
                              [1, 1, 1, 0, 1, 1, 1],
                              [1, 1, 1, 1, 1, 1, 1],
                              [1, 1, 1, 1, 1, 1, 1],
                              [1, 1, 1, 1, 1, 1, 1]])

move_right_df = pd.DataFrame(move_right_matrix, index= move_right_rows, columns= move_right_columns)

#Move Left matrix

#     t1 t2 t4 d3 b3 b4 s2
#     ____________________
# t1 |1  1  1  1  1  1  1
# t2 |1  1  1  1  1  1  1
# t4 |1  1  1  1  1  1  1
# d2 |1  1  1  0  1  1  1
# b1 |1  1  1  1  1  1  1
# b2 |1  1  1  1  1  1  1
# s2 |1  1  1  1  1  1  1

move_left_rows = ['t1', 't2', 't4', 'd2', 'b1', 'b2', 's2']

move_left_columns = ['t1', 't2', 't4', 'd3', 'b3', 'b4', 's2']

move_left_matrix = np.array([[1, 1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 0, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1]])
                             
move_left_df = pd.DataFrame(move_left_matrix, index= move_left_rows, columns= move_left_columns)

# Row number index relating the tile names to their rows in the movement matrices

#        t1 t2 t3 t4 d1 d2 d3 d4 b1 b2 b3 b4 s1 s2
#        _________________________________________
# Up    |-  0  1  2  -  -  -  3  -  4  -  5  6  -
# Down  |0  1  2  -  3  -  -  -  4  -  5  -  6  -
# Right |0  -  1  2  -  -  3  -  -  -  4  5  -  6
# Left  |0  1  -  2  -  3  -  -  4  5  -  -  -  6

# move_matrix_index = np.array([[-1,  0,  1,  2, -1, -1, -1,  3, -1,  4, -1,  5,  6, -1],
#                               [ 0,  1,  2, -1,  3, -1, -1, -1,  4, -1,  5, -1,  6, -1],
#                               [ 0, -1,  1,  2, -1, -1,  3, -1, -1, -1,  4,  5, -1,  6],
#                               [ 0,  1, -1,  2, -1,  3, -1, -1,  4,  5, -1, -1, -1,  6])
#
# tile_name_to_index_column = {
#                             "t1" : 0,
#                             "t2" : 1,
#                             "t3" : 2,
#                             "t4" : 3,
#                             "d1" : 4,
#                             "d2" : 5,
#                             "d3" : 6,
#                             "d4" : 7,
#                             "b1" : 8,
#                             "b2" : 9,
#                             "b3" : 10,
#                             "b4" : 11,
#                             "s1" : 12,
#                             "s2" : 13
#                         }

#This part is copied from my earlier script which reads the Dragon Warrior map and converts it to .tmx.
#Bad practice, I know, but I'll make that script more usable later.

#Open up the tileset
tilefile = open("mazetiles.png")

mtileimage = tmxlib.image.open(tilefile.name)
mtiles = tmxlib.tileset.ImageTileset("mazetiles", (64, 64), mtileimage)

#Here is the order in which tmxlib will read the tiles.
#Note that this is different from the order in which Tiled will read the tiles (see conversion table below.)

#0  = s1
#1  = t3
#2  = d1
#3  = b1
#4  = t2
#5  = d4
#6  = b4
#7  = t4
#8  = t1
#9  = d3
#10 = b3
#11 = fuschia
#12 = s2
#13 = d2
#14 = b2
#15 = fuschia

# tile_names_to_tileset_tiles = {
#     "s1" : mtiles[0],
#     "t3" : mtiles[1],
#     "d1" : mtiles[2],
#     "b1" : mtiles[3],
#     "t2" : mtiles[4],
#     "d4" : mtiles[5],
#     "b4" : mtiles[6],
#     "t4" : mtiles[7],
#     "t1" : mtiles[8],
#     "d3" : mtiles[9],
#     "b3" : mtiles[10],
#     "s2" : mtiles[12],
#     "d2" : mtiles[13],
#     "b2" : mtiles[14],
# }

#This dictionary relates the tileset list index to the tile names.
#There is almost certainly a better way to do this (index() )?

tile_names_to_tileset_numbers ={
    "s1" : 0,
    "t3" : 1,
    "d1" : 2,
    "b1" : 3,
    "t2" : 4,
    "d4" : 5,
    "b4" : 6,
    "t4" : 7,
    "t1" : 8,
    "d3" : 9,
    "b3" : 10,
    "s2" : 12,
    "d2" : 13,
    "b2" : 14,
}

# #tmxlib loads the tileset image vertically (in column-major order), whereas Tiled reads it horizontally (in
# #row-major order).
# #So we have to convert between the two when writing the array of matched tiles.

tileset_nrows = mtiles.row_count
tileset_ncols = mtiles.column_count

conversion_table = {}
for index in range(0, len(mtiles)):
    x, y = divmod(index, tileset_nrows)
    cvt_number = y * tileset_ncols + x
    conversion_table[cvt_number] = mtiles[index]

#This part is taken from Wikipedia's page on maze generation: 
#https://en.wikipedia.org/wiki/Maze_generation_algorithm
# Code by Erik Sweet and Bill Basener
#I've modified it to create a .tmx file using a set of tiles, rather than a plot in matplotlib

num_rows = int(input("Rows: ")) # number of rows
num_cols = int(input("Columns: ")) # number of columns

M = np.full((num_rows,num_cols), "em", dtype="S2") #specifies that the array will hold strings of length 2 
# The array M is going to hold the array information for each cell.
# The first four coordinates tell if walls exist on those sides 
# and the fifth indicates if the cell has been visited in the search.
# M(LEFT, UP, RIGHT, DOWN, CHECK_IF_VISITED)

# Set starting row and column
r = 0
c = 0
#Randomly pick a corridor orientation for the starting tile.
starting_tile = random.choice(['s1', 's2'])
M[r,c] = starting_tile
history = [(r,c)] # The history is the [sic]
                  # ...list of cells that have already been visited along the current path?

# Trace a path though the cells of the maze and open walls along the path.
# We do this with a while loop, repeating the loop until there is no history,
# which would mean we backtracked to the initial start.
while history:
    # check if the adjacent cells are valid for moving to
    check = []
    if r > 0 and M[r-1,c] == "em":
        check.append('U')
    if r < num_rows-1 and M[r+1,c] == "em":
        check.append('D')
    if c < num_cols-1 and M[r,c+1] == "em":
        check.append('R')
    if c > 0 and M[r,c-1] == "em":
        check.append('L')
    
    if len(check): # If there is a valid cell to move to.
        last_tile = M[history[-1]] 
        history.append([r,c])
        move_direction = random.choice(check)
        if move_direction == 'U':
            tile_choices = move_up_df.loc[last_tile]
            tile_choices = tile_choices[tile_choices != 0]  #filter out banned transitions
            tile_choice_list = list(tile_choices.index.values)
            choice = random.choice(tile_choice_list)
            print choice
            r = r-1
            M[r,c] = choice            
        if move_direction == 'D':
            tile_choices = move_down_df.loc[last_tile]
            tile_choices = tile_choices[tile_choices != 0]  #filter out banned transitions
            tile_choice_list = list(tile_choices.index.values)
            choice = random.choice(tile_choice_list)
            print choice
            r = r+1
            M[r,c] = choice
        if move_direction == 'R':
            tile_choices = move_right_df.loc[last_tile]
            tile_choices = tile_choices[tile_choices != 0]  #filter out banned transitions
            tile_choice_list = list(tile_choices.index.values)
            choice = random.choice(tile_choice_list)
            c = c+1
            M[r,c] = choice
        if move_direction == 'L':
            tile_choices = move_left_df.loc[last_tile]
            tile_choices = tile_choices[tile_choices != 0]  #filter out banned transitions
            tile_choice_list = list(tile_choices.index.values)
            choice = random.choice(tile_choice_list)
            c = c-1
            M[r,c] = choice
    else: # If there are no valid cells to move to.
    # retrace one step back in history if no move is possible
        r,c = history.pop()


# # Open the walls at the start and finish
# M[0,0,0] = 1
# M[num_rows-1,num_cols-1,2] = 1










