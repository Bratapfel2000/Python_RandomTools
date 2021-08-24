"""
adding list of string-coordinates to 0-matrix of any size, whereas matrix
(1,1) coordinate is on bottom left and (x,x) on top right
"""

# create matrix
def grids(a,b):
    a_ = []
    for i in range(a):
        a_.append([])
        for j in range(b):
            a_[i].append([0])
    return a_

# print matrix
def print_grids(matrix):
    for i in matrix:
        print(i)

# print matrix reverse
def print_grids_reverse(matrix):
    x = len(matrix)
    for i in range(x):
        print(matrix[x-i-1])

# convert string coordinates and return integers in list
def coord_to_int(coordinate):
    new_list = []
    for str_number in coordinate:
        new_list.append(str_number.split(" "))
    for i in new_list:
        i[0] = int(i[0])
        i[1] = int(i[1])
    return new_list

# add coordinates to matrix
def add_to_coordinates(matrix,coordinate):
    a = len(matrix)
    b = len(matrix[0])
    for coordinates in coordinate:
        x = coordinates[0]
        y = coordinates[1]
        for i in range(x):
            for j in range(y):
                matrix[i][j][0] += 1

if __name__ == "__main__":

    # create 4x4 matrix
    y = grids(4,4)

    # coordinates
    ref = ["1 4", "2 3", "4 1"]

    # convert to int
    ref_int = coord_to_int(ref)

    # add them to matrix
    add_to_coordinates(y,ref_int)    

    # print matrix
    print_grids_reverse(y)

