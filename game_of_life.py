def get_neighbours(m,p):
    row = p[0]
    col = p[1]
    # as the point is at center 8 neighbour will be there
    n = [m[row-1][col-1],m[row-1][col],m[row-1][col+1],m[row][col-1],m[row][col+1],m[row+1][col-1],m[row+1][col],m[row+1][col+1]]
    t = 0
    for i in n:
        if i:
            t=t+1
    return t

