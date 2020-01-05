import game_of_life

def test_one_neighbour_for_point_on_center():
    grid = [[True,False,False],[False,True,False],[False,False,False]]
    a = game_of_life.get_neighbours(m=grid,p = [1,1])
    e = 1
    assert a == e

def test_more_than_one_neighbours_for_point_on_center():
    grid = [[True,True,True],[True,True,True],[True,False,True]]
    a = game_of_life.get_neighbours(m=grid,p = [1,1])
    e = 7
    assert a == e

def test_neighbour_for_point_on_edge():
    grid = [[True,True,False],[True,True,False],[False,False,False]]
    a = game_of_life.get_neighbours(m=grid,p = [2,0])
    e = 2
    assert a == e
    
def test_neighbour_for_point_on_side():
    grid = [[True,False,True],[False,False,False],[False,False,True]]
    a = game_of_life.get_neighbours(m=grid,p = [0,1])
    e = 2
    assert a == e

    

def test_next_generation_no_live_cells():
    grid = [[False,False,False],[False,False,False],[False,False,False]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,False,False],[False,False,False],[False,False,False]]
    assert a == e

def test_next_generation_one_live_cell():
    grid = [[False,False,False],[False,True,False],[False,False,False]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,False,False],[False,False,False],[False,False,False]]
    assert a == e

def test_next_generation_two_neighbour_live_cells():
    grid = [[False,False,False],[False,True,False],[False,True,False]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,False,False],[False,False,False],[False,False,False]]
    assert a == e

def test_next_generation_two_not_neighbour_live_cells():
    grid = [[True,False,False],[False,False,False],[False,False,True]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,False,False],[False,False,False],[False,False,False]]
    assert a == e


def test_next_generation_three_live_cells_not_neighbours():
    grid = [[True,False,True],[False,False,False],[False,False,True]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,False,False],[False,True,False],[False,False,False]]
    assert a == e

def test_next_generation_three_live_cells_neighbours_all_at_corners():
    grid = [[True,True,False],[True,False,False],[False,False,False]]
    a = game_of_life.next_generation(m = grid)
    e = [[True,True,False],[True,True,False],[False,False,False]]
    assert a == e

def test_next_generation_three_live_cells_neighbours_all_at_different_sides():
    grid = [[False,False,False],[True,False,True],[False,True,False]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,False,False],[False,True,False],[False,True,False]]
    assert a == e

def test_next_generation_three_live_cells_neighbours_all_at_same_sides():
    grid = [[True,True,True],[False,False,False],[False,False,False]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,True,False],[False,True,False],[False,False,False]]
    assert a == e

def test_next_generation_three_live_cells_neighbours_all_at_center():
    grid = [[False,False,False],[True,True,True],[False,False,False]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,True,False],[False,True,False],[False,True,False]]
    assert a == e

def test_next_generation_three_live_cells_neighbours_diagonally():
    grid = [[True,False,False],[False,True,False],[False,False,True]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,False,False],[False,True,False],[False,False,False]]
    assert a == e

    
def test_next_generation_four_live_cells_not_neighbours():
    grid = [[True,False,True],[False,False,False],[True,False,True]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,False,False],[False,False,False],[False,False,False]]
    assert a == e

def test_next_generation_four_live_cells_neighbours_each_on_side():
    grid = [[False,True,False],[True,False,True],[False,True,False]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,True,False],[True,False,True],[False,True,False]]
    assert a == e

def test_next_generation_four_live_cells_three_diagonally_and_one_on_side():
    grid = [[True,True,False],[False,True,False],[False,False,True]]
    a = game_of_life.next_generation(m = grid)
    e = [[True,True,False],[True,True,True],[False,False,False]]
    assert a == e

def test_next_generation_four_live_cells_three_diagonally_and_one_on_corner():
    grid = [[True,False,False],[False,True,False],[True,False,True]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,False,False],[True,True,False],[False,True,False]]
    assert a == e

def test_next_generation_four_live_cells_three_through_center_and_one_at_corner():
    grid = [[True,True,False],[False,True,False],[False,True,False]]
    a = game_of_life.next_generation(m = grid)
    e = [[True,True,False],[False,True,True],[False,False,False]]
    assert a == e

def test_next_generation_four_live_cells_three_through_center_and_one_at_side():
    grid = [[False,True,False],[True,True,False],[False,True,False]]
    a = game_of_life.next_generation(m = grid)
    e = [[True,True,False],[True,True,True],[True,True,False]]
    assert a == e

def test_next_generation_four_live_cells_three_through_side_and_one_at_center():
    grid = [[True,False,False],[True,True,False],[True,False,False]]
    a = game_of_life.next_generation(m = grid)
    e = [[True,True,False],[True,True,False],[True,True,False]]
    assert a == e

def test_next_generation_four_live_cells_three_through_side_and_one_at_corner():
    grid = [[True,False,False],[True,False,False],[True,False,True]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,False,False],[True,False,False],[False,True,False]]
    assert a == e

def test_next_generation_four_live_cells_three_through_side_and_one_on_side_near():
    grid = [[True,True,False],[True,False,False],[True,False,False]]
    a = game_of_life.next_generation(m = grid)
    e = [[True,True,False],[True,False,False],[False,False,False]]
    assert a == e

def test_next_generation_four_live_cells_three_through_side_and_one_on_side_far():
    grid = [[True,False,False],[True,False,True],[True,False,False]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,True,False],[True,False,False],[False,True,False]]
    assert a == e

def test_next_generation_five_live_cells_diagonally_cross():
    grid = [[True,False,True],[False,True,False],[True,False,True]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,True,False],[True,False,True],[False,True,False]]
    assert a == e

def test_next_generation_five_live_cells_straight_cross():
    grid = [[False,True,False],[True,True,True],[False,True,False]]
    a = game_of_life.next_generation(m = grid)
    e = [[True,True,True],[True,False,True],[True,True,True]]
    assert a == e

def test_next_generation_five_live_cells():
    grid = [[True,False,False],[True,True,True],[False,False,True]]
    a = game_of_life.next_generation(m = grid)
    e = [[True,False,False],[True,False,True],[False,False,True]]
    assert a == e

def test_next_generation_six_live_cells():
    grid = [[True,True,True],[False,False,False],[True,True,True]]
    a = game_of_life.next_generation(m = grid)
    e = [[False,True,False],[False,False,False],[False,True,False]]
    assert a == e

