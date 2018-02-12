# Complete the function below.
def copyMaze(maze):
    return [row[:] for row in maze]
    
def countCheese(maze):
    ret = 0
    for row in maze:
        for column in row:
            ret += 1 if column == 2 else 0
    return ret

def possibleMoves(maze, x, y, n):
    if x>0 and maze[x-1][y] != 1:
        new_maze = copyMaze(maze)
        new_n = n-1 if new_maze[x-1][y]==2 else n
        new_maze[x-1][y]=0
        yield [new_maze, x-1, y, new_n]
    if x<len(maze)-1 and maze[x+1][y] != 1:
        new_maze = copyMaze(maze)
        new_n = n-1 if new_maze[x+1][y]==2 else n
        new_maze[x+1][y] = 0
        yield [new_maze, x+1, y, new_n]
    if y>0 and maze[x][y-1] != 1:
        new_maze = copyMaze(maze)
        new_n = n-1 if new_maze[x][y-1]==2 else n
        new_maze[x][y-1]=0
        yield [new_maze, x, y-1, new_n]
    if y<len(maze[0])-1 and maze[x][y+1] != 1:
        new_maze = copyMaze(maze)
        new_n = n-1 if new_maze[x][y+1]==2 else n
        new_maze[x][y+1]=0
        yield [new_maze, x, y+1, new_n]

def minMoves(maze, x, y):
    tab_open = [[copyMaze(maze), 0, 0, countCheese(maze), 0]] # [Maze, x_tom, y_tom, cheese_left, step_taken]
    tab_close = []
    while len(tab_open)>0:
        front=tab_open[0]
        if front[3]==0 and front[1]==x and front[2]==y:
            return front[-1]
        tab_close.append(front[:-1])
        step = front[-1]+1
        for state in possibleMoves(*front[:4]):
            if state not in tab_close:
                tab_open.append(state+[step])
        tab_open.pop(0)
    return -1