import game_of_life

def test_one_neighbour_for_point_on_center():
    a = game_of_life.get_neighbours(m=[[True,False,False],[False,True,False],[False,False,False]],p = [1,1])
    e = 1
    assert a == e

def test_more_than_one_neighbours_for_point_on_center():
    a = game_of_life.get_neighbours(m=[[True,True,True],[False,True,True],[False,False,False]],p = [1,1])
    e = 4
    assert a == e
