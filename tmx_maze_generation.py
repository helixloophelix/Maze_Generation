#usr/bin/env Python

import random
import numpy as np
import tmxlib

#Valid move matrices
#Current cell is on the left side, cell being moved into is on the top
#I.e. movement goes left --> top
#These look silly now, but they'll be important once we start modifying the transition probabilities for
#each tile.

#"t" stands for "T-junction", "b" stands for "bend", "d" stands for "dead-end", and "s" stands for "straight"

#Move Up matrix

#     t2 t3 t4 d4 b2 b4 s1
#     ____________________
# t2 |1  1  1  1  1  1  1
# t3 |1  1  1  1  1  1  1
# d1 |1  1  1  0  1  1  1
# b1 |1  1  1  1  1  1  1
# b3 |1  1  1  1  1  1  1
# s1 |1  1  1  1  1  1  1

#Move Down matrix

#     t1 t2 t3 d1 b1 b3 s1
#     ____________________
# t2 |1  1  1  1  1  1  1
# t3 |1  1  1  1  1  1  1
# t4 |1  1  1  1  1  1  1
# d4 |1  1  1  0  1  1  1
# b2 |1  1  1  1  1  1  1
# b4 |1  1  1  1  1  1  1
# s1 |1  1  1  1  1  1  1

#Move Right matrix

#     t1 t3 t4 d3 b3 b4 s2
#     ____________________
# t1 |1  1  1  1  1  1  1
# t2 |1  1  1  1  1  1  1
# t4 |1  1  1  1  1  1  1
# d2 |1  1  1  0  1  1  1
# b1 |1  1  1  1  1  1  1
# b2 |1  1  1  1  1  1  1
# s2 |1  1  1  1  1  1  1

#Move Left matrix

#     t1 t2 t4 d2 b1 b2 s2
#     ____________________
# t1 |1  1  1  1  1  1  1
# t3 |1  1  1  1  1  1  1
# t4 |1  1  1  1  1  1  1
# d3 |1  1  1  0  1  1  1
# b3 |1  1  1  1  1  1  1
# b4 |1  1  1  1  1  1  1
# s2 |1  1  1  1  1  1  1

#Here is the order in which tmxlib will read the tiles.
#Note that this is different from the order in which Tiled will read the tiles (see conversion table below.)

#1  = s1
#2  = t3
#3  = d1
#4  = b1
#5  = t2
#6  = d4
#7  = b4
#8  = t4
#9  = t1
#10 = d3
#11 = b3
#12 = fuschia
#13 = s2
#14 = d2
#15 = b2
#16 = fuschia

#This part is copied from my earlier script which reads the Dragon Warrior map and converts it to .tmx.
#Bad practice, I know, but I'll make that script more usable later.

#Open up the tileset
tilefile = open("mazetiles.png")

mtileimage = tmxlib.image.open(tilefile.name)
mtiles = tmxlib.tileset.ImageTileset("mazetiles", (64, 64), mtileimage)

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

for tile in mtiles:
    

#This part is taken from Wikipedia's page on maze generation: 
#https://en.wikipedia.org/wiki/Maze_generation_algorithm
# Code by Erik Sweet and Bill Basener
#I've modified it to create a .tmx file using a set of tiles, rather than a plot in matplotlib

num_rows = int(input("Rows: ")) # number of rows
num_cols = int(input("Columns: ")) # number of columns

M = np.zeros((num_rows,num_cols,5), dtype=np.uint8)
# The array M is going to hold the array information for each cell.
# The first four coordinates tell if walls exist on those sides 
# and the fifth indicates if the cell has been visited in the search.
# M(LEFT, UP, RIGHT, DOWN, CHECK_IF_VISITED)
image = np.zeros((num_rows*10,num_cols*10), dtype=np.uint8)
# The array image is going to be the output image to display

# Set starting row and column
r = 0
c = 0
history = [(r,c)] # The history is the [sic]
                  # ...list of cells that have already been visited along the current path?






# Trace a path though the cells of the maze and open walls along the path.
# We do this with a while loop, repeating the loop until there is no history, 
# which would mean we backtracked to the initial start.
while history: 
    M[r,c,4] = 1 # designate this location as visited
    # check if the adjacent cells are valid for moving to
    check = []
    if c > 0 and M[r,c-1,4] == 0:
        check.append('L')  
    if r > 0 and M[r-1,c,4] == 0:
        check.append('U')
    if c < num_cols-1 and M[r,c+1,4] == 0:
        check.append('R')
    if r < num_rows-1 and M[r+1,c,4] == 0:
        check.append('D')    
    
    if len(check): # If there is a valid cell to move to.
        # Mark the walls between cells as open if we move
        history.append([r,c])
        move_direction = random.choice(check)
        if move_direction == 'L':
            M[r,c,0] = 1
            c = c-1
            M[r,c,2] = 1
        if move_direction == 'U':
            M[r,c,1] = 1
            r = r-1
            M[r,c,3] = 1
        if move_direction == 'R':
            M[r,c,2] = 1
            c = c+1
            M[r,c,0] = 1
        if move_direction == 'D':
            M[r,c,3] = 1
            r = r+1
            M[r,c,1] = 1
    else: # If there are no valid cells to move to.
	# retrace one step back in history if no move is possible
        r,c = history.pop()
    
         
# Open the walls at the start and finish
M[0,0,0] = 1
M[num_rows-1,num_cols-1,2] = 1










