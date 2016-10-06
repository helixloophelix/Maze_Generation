#usr/bin/env Python

import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import tmxlib

# This class doesn't have to do anything special-- it's just a convenient way of storing tile attributes.

class MazeTile:
    
    def __init__(self, name, direction_indicator, number, conversion_number):
        self.name = name
        self.direction_indicator = direction_indicator
        self.conversion_number = conversion_number
        self.number = number
        
#Let's load the tiles first.

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
#11 = c0
#12 = s2
#13 = d2
#14 = b2
#15 = fuschia

# tmxlib loads the tileset image vertically (in column-major order), whereas Tiled reads it horizontally (in
# row-major order).
# So we have to convert between the two when writing the array of matched tiles.

tileset_nrows = mtiles.row_count
tileset_ncols = mtiles.column_count

conversion_table = {}
for index in range(0, len(mtiles)):
    x, y = divmod(index, tileset_nrows)
    cvt_number = y * tileset_ncols + x
    conversion_table[cvt_number] = mtiles[index]
    print "Tile number %d linked to conversion number %d" % (index, cvt_number)

# Now let's define the properties of each tile in terms of the MazeTile class.
# Here 0 and 1 are doing the work of boolean variables. It's easier on numpy that way.
# These could be lists instead of dictionaries, but it'd be much harder for me to parse if I did that.

# List ordering follows the maze array order: left, up, right, down.

# s1_directions = {
#     'l' : 0,
#     'u' : 1,
#     'r' : 0,
#     'd' : 1,
# }

s1_directions = [0, 1, 0, 1]

s1 = MazeTile('s1', s1_directions, 0, conversion_table[0])

# t3_directions = {
#     'l' : 0,
#     'u' : 1,
#     'r' : 1,
#     'd' : 1,
# }

t3_directions = [0, 1, 1, 1]

t3 = MazeTile('t3', t3_directions, 1, conversion_table[1])

# d1_directions = {
#     'l' : 0,
#     'u' : 0,
#     'r' : 0,
#     'd' : 1,
# }

d1_directions = [0, 0, 0, 1]

d1 = MazeTile('d1', d1_directions, 2, conversion_table[2])

# b1_directions = {
#     'l' : 1,
#     'u' : 0,
#     'r' : 0,
#     'd' : 1,
# }

b1_directions = [1, 0, 0, 1]

b1 = MazeTile('b1', b1_directions, 3, conversion_table[3])

# t2_directions = {
#     'l' : 1,
#     'u' : 1,
#     'r' : 0,
#     'd' : 1,
# }

t2_directions = [1, 1, 0, 1]

t2 = MazeTile('t2', t2_directions, 4, conversion_table[4])

# d4_directions = {
#     'l' : 0,
#     'u' : 1,
#     'r' : 0,
#     'd' : 0,
# }

d4_directions = [0, 1, 0, 0]

d4 = MazeTile('d4', d4_directions, 5, conversion_table[5])

# b4_directions = {
#     'l' : 0,
#     'u' : 1,
#     'r' : 1,
#     'd' : 0,
# }

b4_directions = [0, 1, 1, 0]

b4 = MazeTile('b4', b4_directions, 6, conversion_table[6])

# t4_directions = {
#     'l' : 1,
#     'u' : 1,
#     'r' : 1,
#     'd' : 0,
# }

t4_directions = [1, 1, 1, 0]

t4 = MazeTile('t4', t4_directions, 7, conversion_table[7])

# t1_directions = {
#     'l' : 1,
#     'u' : 0,
#     'r' : 1,
#     'd' : 1,
# }

t1_directions = [1, 0, 1, 1]

t1 = MazeTile('t1', t1_directions, 8, conversion_table[8])

# d3_directions = {
#     'l' : 0,
#     'u' : 0,
#     'r' : 1,
#     'd' : 0,
# }

d3_directions = [0, 0, 1, 0]

d3 = MazeTile('d3', d3_directions, 9, conversion_table[9])

# b3_directions = {
#     'l' : 0,
#     'u' : 0,
#     'r' : 1,
#     'd' : 1,
# }

b3_directions = [0, 0, 1, 1]

b3 = MazeTile('b3', b3_directions, 10, conversion_table[10])

# c0_directions = {
#     'l' : 1,
#     'u' : 1,
#     'r' : 1,
#     'd' : 1,
# }

c0_directions = [1, 1, 1, 1]

c0 = MazeTile('c0', c0_directions, 11, conversion_table[11])

# s2_directions = {
#     'l' : 1,
#     'u' : 0,
#     'r' : 1,
#     'd' : 0
# }

s2_directions = [1, 0, 1, 0]

s2 = MazeTile('s2', s2_directions, 12, conversion_table[12])

# d2_directions = {
#     'l' : 1,
#     'u' : 0,
#     'r' : 0,
#     'd' : 0,
# }

d2_directions = [1, 0, 0, 0]

d2 = MazeTile('d2', d2_directions, 13, conversion_table[13])

# b2_directions = {
#     'l' : 1,
#     'u' : 1,
#     'r' : 0,
#     'd' : 0,
# }

b2_directions = [1, 1, 0, 0]

b2 = MazeTile('b2', b2_directions, 14, conversion_table[14])

maze_tile_list = [s1, t3, d1, b1, t2, d4, b4, t4, t1, d3, b3, c0, s2, d2, b2]

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
        check.append('l')  
    if r > 0 and M[r-1,c,4] == 0:
        check.append('u')
    if c < num_cols-1 and M[r,c+1,4] == 0:
        check.append('r')
    if r < num_rows-1 and M[r+1,c,4] == 0:
        check.append('d')    
    
    if len(check): # If there is a valid cell to move to.
        # Mark the walls between cells as open if we move
        history.append([r,c])
        move_direction = random.choice(check)
        if move_direction == 'l':
            M[r,c,0] = 1
            c = c-1
            M[r,c,2] = 1 #open up the wall to the right, so that the tiles line up
        if move_direction == 'u':
            M[r,c,1] = 1
            r = r-1
            M[r,c,3] = 1
        if move_direction == 'r':
            M[r,c,2] = 1
            c = c+1
            M[r,c,0] = 1
        if move_direction == 'd':
            M[r,c,3] = 1
            r = r+1
            M[r,c,1] = 1
    else: # If there are no valid cells to move to.
	# retrace one step back in history if no move is possible
        r,c = history.pop()
    
         
# Open the walls at the start and finish
M[0,0,0] = 1
M[num_rows-1,num_cols-1,2] = 1

# # Generate the image for display
# for row in range(0,num_rows):
#     for col in range(0,num_cols):
#         cell_data = M[row,col]
#         for i in range(10*row+1,10*row+9):
#             image[i,range(10*col+1,10*col+9)] = 255
#             if cell_data[0] == 1:image[range(10*row+1,10*row+9),10*col] = 255
#             if cell_data[1] == 1:image[10*row,range(10*col+1,10*col+9)] = 255
#             if cell_data[2] == 1:image[range(10*row+1,10*row+9),10*col+9] = 255
#             if cell_data[3] == 1:image[10*row+9,range(10*col+1,10*col+9)] = 255

# # Display the image
# plt.imshow(image, cmap = cm.Greys_r, interpolation='none')
# plt.show()

# This ends the part I took off of Wikipedia

# print M

# You can't create this directly as an array because numpy is stupid
map_list = []

# Here we loop through the maze array and relate each set of open values to the appropriate tile.

# Screw nditer-- in this case I might as well just use for loops, because the syntax for restricting nditer
# to just the first two dimensions is obscure and counterintuitive.

for maze_tile in maze_tile_list:
    print maze_tile.name
    print maze_tile.number

for row in range(0, num_rows):
    for col in range(0, num_cols):
        match_found = False
        current_tile = M[row, col]
        current_tile_directions = current_tile[0:4]
        current_tile_direction_list = current_tile_directions.tolist()
        for maze_tile in maze_tile_list:
            opening_list = maze_tile.direction_indicator
            # print opening_list
            # print current_tile_direction_list
            if opening_list == current_tile_direction_list:
                print opening_list
                print current_tile_direction_list
                print maze_tile.name
                print maze_tile.number
                map_list.append(maze_tile.number)
                match_found = True
                break
        if match_found == False:
            print ("Error: no matching tile found")
            print opening_list
            print current_tile_direction_list
            print (row, col)
             
        
# Now we just create the .tmx file. This part is ripped directly from the alefgard script.

print map_list
oneD_map_array = np.fromiter(map_list, int)
print oneD_map_array
print oneD_map_array.size
map_array = np.reshape(oneD_map_array, (num_rows, num_cols))
print map_array

#I don't know why Tiled is doing this, but perhaps we need to take the transpose of the map array?
map_array = map_array.transpose()

#To create the final .tmx map, we first create a Map object
output_map = tmxlib.map.Map((num_rows, num_cols), (64, 64))

#Then we add a tile layer to it. This tile layer is empty.
output_map.add_tile_layer("Generated Tile Layer")

#Next, we request the layers from the Map object. This gives us a LayerList object.
layers = output_map.layers

#The first element in the LayerList should be our TileLayer object.
output_tile_layer = layers[0]

#Now, we iterate over the map array, stuffing its value into the TileLayer object.
map_array_iterator = np.nditer(map_array, flags=["multi_index"])
while not map_array_iterator.finished:
    current_tile = map_array[map_array_iterator.multi_index]
    converted_tile = conversion_table[current_tile]
    print map_array_iterator.multi_index
    print converted_tile
    output_tile_layer[map_array_iterator.multi_index] = converted_tile
    map_array_iterator.iternext()

output_map.save("maze.tmx")

# maze_array_iterator = np.nditer(M, flags=['multi_index', 'ranged'], itershape=(0))
# while not maze_array_iterator.finished:
#     current_tile = M[maze_array_iterator.multi_index, 0]
#     print maze_array_iterator.multi_index
#     print current_tile
#     maze_array_iterator.iternext()
# #     current_tile_directions = current_tile[0:4]
# #     current_tile_direction_list = current_tile_directions.tolist()
# #     for maze_tile in maze_tile_list:
# #         opening_list = maze_tile.direction_indicator.values()
# #         print opening_list
# #         print current_tile_direction_list
# #         if opening_list == current_tile_direction_list:
# #             tile.array[maze_array_iterator.multi_index] = maze_tile.conversion_number
# #             break
# #
# # print tile_array
