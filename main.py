import numpy as np

if __name__ == '__main__':
    m = 5
    n = 5
    grid = np.zeros((m,n))
    holes = set([(1,1), (1,2), (2,1), (2,2)])
    tetrominos = {
        1: [(0,0), (0,1), (0,2), (0,3)],
        -1: [(0,0), (1,0), (2,0), (3,0)],
        # 'HF': [(0,0), (0,-1), (0,-2), (0,-3)],
        # 'VF': [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
    }

    print (m*n - len(holes))
    print (np.sum(grid))


    def checkCoord(r, c, search_state, grid=grid, holes=holes):
        '''
        checks if given r,c lies within grid and if it is unoccupied
        '''
        if (r, c) in holes: return False

        if r >= 0 and r < len(grid[0]) and c >= 0 and c < len(grid):
            print ('debug', grid[r][c], search_state)
            if grid[r][c] == search_state: return True
        return False


    def place_tetronmino(tetromino, r, c, grid=grid):
        '''
        if valid, place tetroninmo on grid, starting at (i,j)
        tetronimo expected to be key in dict choices, i.e a type of valid tetroniimoes
        :return:
        '''
        coords = [[r + i, c + j] for i, j in tetrominos[tetromino]]
        coords_empty = [checkCoord(i, j, search_state=0.) for i, j in coords]
        print (coords)
        print (coords_empty)
        print (all(coords_empty))

        if all(coords_empty):
            for i, j in coords:
                grid[i][j] = tetromino
        print (grid)

    def remove_tetronmino(tetromino, r, c, grid=grid):
        '''
        if valid, remove  specified tetroninmo on grid, starting at (i,j)
        tetronimo expected to be key in dict choices, i.e a type of valid tetronimoes
        :return:
        '''
        coords = [(r + i, c + j) for i, j in tetrominos[tetromino]]
        # TODO: make sure only removing discrete tetronimos # here is where key comes in
        coords_full = [checkCoord(i, j, search_state=tetromino) for i, j in coords]

        if all(coords_full):
            for i, j in coords:
                grid[i][j] = 0


    def backtrack():
        # if len(remaining_places) == 0
        if np.sum(np.abs(grid)) == m*n - len(holes):
            print ('possible')
            return True
        if np.sum(np.abs(grid)) %2 == 1:
            print('not possible')
            return False
        # if containsUnreachable(grid):
        #     return

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0.:
                    print (r,c)
                    for t in tetrominos:
                        print(r,c)
                        print (t)
                        place_tetronmino(t, r,c)
                        print (grid)
                        print ('filled', np.sum(np.abs(grid)))
                        if backtrack() == True:
                            return True
                        remove_tetronmino(t,r,c)
        print ('end reached')
        return False
    print ('test')
    print (tetrominos)

    print(backtrack())

    # (place_tetronmino(1, 0, 0))
    # print (grid)

    #NOT TESTED YET





# See PyCharm help at https://www.jetbrains.com/help/pycharm/