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
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = False
    return m
