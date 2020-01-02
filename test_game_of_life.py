import game_of_life

def test_neighbours_of_point_on_center():
    a = game_of_life.get_neighbours(m=[[True,False,False],[False,True,False],[False,False,False]],p = [1,1])
    e = 1
    assert a == e
