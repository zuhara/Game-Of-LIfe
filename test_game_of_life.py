import game_of_life

def test_one_neighbour_for_point_on_center():
    grid = [[True,False,False],[False,True,False],[False,False,False]]
    a = game_of_life.get_neighbours(m=grid,p = [1,1])
    e = 1
    assert a == e

def test_more_than_one_neighbours_for_point_on_center():
    grid = [[True,True,True],[False,True,True],[False,False,False]]
    a = game_of_life.get_neighbours(m=grid,p = [1,1])
    e = 4
    assert a == e

def test_neighbour_for_point_on_edge():
    grid = [[True,True,False],[True,True,False],[False,False,False]]
    a = game_of_life.get_neighbours(m=grid,p = [2,0])
    e = 2
    assert a == e
    
def test_neighbour_for_point_on_side():
    grid = [[True,True,False],[True,True,False],[False,False,False]]
    a = game_of_life.get_neighbours(m=grid,p = [1,2])
    e = 2
    assert a == e
