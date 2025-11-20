CELL_EMPTY_FLOOR = "."
CELL_VOID = " "
CELL_WALL = "#"
CELL_PLAYER = "@"

x = CELL_VOID
W = CELL_WALL
_ = CELL_EMPTY_FLOOR
maze_cells = [
    [_,x,_,_,_,_,W,W,_,_,],
    [_,_,W,W,_,_,_,_,W,_,],
    [_,_,_,_,_,W,_,_,_,_,],
    [_,_,_,W,_,_,_,_,W,_,],
    [_,x,x,_,_,_,x,_,x,x,]
]
del _
del W
del x
maze_height = len(maze_cells)
maze_width = len(maze_cells[0])

player_y = 2
player_x = 3
player_dy = 0
player_dx = 0

is_game_play = True
while is_game_play:
# Отрисовка 
    print("\n" *100)


# Отрисовка лабиринта 
for y, cells_line in enumerate(maze_cells):
    for x, cell in enumerate(cells_line):
        if x == player_x and y == player_y:
            print(cell, end=" ")
        else:
            print(cell, end=" ")
    print()


pass
is_game_play = False