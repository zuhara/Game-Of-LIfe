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
    
    next_gen = [[0 for i in range(rows)] for j in range(cols)]

    for i in range(rows):
        for j in range(cols):
            if m[i][j]:
                live_neighbours = get_neighbours(m,[i,j])
                if live_neighbours < 2 :           # Rule 2 
                    next_gen[i][j] = False    
                else:
                    next_gen[i][j] = m[i][j]
            else:
                live_neighbour = get_neighbours(m,[i,j])
                if live_neighbour == 3:           # Rule 4
                    next_gen[i][j] = True
                else:
                    next_gen[i][j] = m[i][j]
    return next_gen
