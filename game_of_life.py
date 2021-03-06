import time
def get_neighbours(m,p):
    r = p[0]
    c = p[1]
    n = [[r-1,c],[r+1,c],[r,c+1],[r,c-1],[r-1,c-1],[r-1,c+1],[r+1,c-1],[r+1,c+1]]
    
    #Find the position of neighbours
    neighbours = []
    for i in n:
        if (0 <= i[0] < len(m)) and (0 <= i[1] < len(m[0])):
            neighbours.append([i[0],i[1]])
            
    #Find number of live neighbours
    live_neighbour = 0
    for point in neighbours:
        if m[point[0]][point[1]]:
            live_neighbour = live_neighbour + 1           
    return live_neighbour


def next_generation(m):
    rows = len(m)
    cols = len(m[0])
    
    next_gen = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):
            live_neighbours = get_neighbours(m,[i,j])
            if m[i][j]:
                if live_neighbours < 2 :           # Rule 2 
                    next_gen[i][j] = False
                elif live_neighbours == 2 :        # Rule 1
                    next_gen[i][j] = True
                elif live_neighbours > 3 :         # Rule 3
                    next_gen[i][j] = False
                else:
                    next_gen[i][j] = m[i][j]
            else:
                if live_neighbours == 3:           # Rule 4
                    next_gen[i][j] = True
                else:
                    next_gen[i][j] = m[i][j]
    return next_gen


def display(m):
    string = ""
    for  i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]:
                string = string + " 0 "
            else:
                string = string + " * "
        string = string + "\n"
    return string

grid = [[False,True,False],[False,True,False],[False,True,False]]
n = 1
while n < 10:
    n = n + 1
    time.sleep(0.5)
    m = next_generation(grid)
    grid = m
    d = display(grid)
    print(d)
