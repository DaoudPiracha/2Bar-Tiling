import numpy as np
from helpers import render

if __name__ == '__main__':
    m = 4
    n = 6
    grid = np.zeros((m,n))

    holes = set([(0,3), (4,4), (4,5)])
    trominos = {
        1: [(0,0), (0,1), (0,2)],
        -1: [(0,0), (1,0), (2,0)],
        }
    RENDER = True


    def checkCoord(r, c, search_state, grid=grid, holes=holes):
        '''
        checks if given r,c lies within grid and if it is unoccupied
        '''

        if (r, c) in holes: return False
        if r >= 0 and r < m and c >= 0 and c < n:
            if grid[r][c] == search_state: return True
        return False


    def place_tronmino(tromino, r, c, grid=grid):
        '''
        if possible, place tromino on grid, starting at (r,c)
        tromino expected to be key in dict trominos

        returns: Boolean True if placed else False
        '''
        coords = [[r + i, c + j] for i, j in trominos[tromino]]
        coords_empty = [checkCoord(i, j, search_state=0.) for i, j in coords]

        if not all(coords_empty): return False
        else:
            for i, j in coords:
                grid[i][j] = tromino
        return True

    def remove_tromino(tromino, r, c, grid=grid):
        '''
        if specificed tromino exists at (r,c), remove from grid
        tromino expected to be key in dict trominos
        '''
        coords = [(r + i, c + j) for i, j in trominos[tromino]]
        # TODO: make sure only removing discrete tetronimos # here is where key comes in
        coords_full = [checkCoord(i, j, search_state=tromino) for i, j in coords]

        if all(coords_full):
            for i, j in coords:
                grid[i][j] = 0


    def backtrack_tile():
        '''
        Backtracking approach places tromino on empty tile,
        continues to search in remaining space, exits if
        tiling found or exhausted all search space
        '''

        #check if all required tiles covered
        if np.sum(np.abs(grid)) == m*n - len(holes):
            return True
        # check if remaining tiles untilable
        if np.sum(np.abs(grid)) %3 != 0:
            return False

        # TODO: Early exit: if a component is not tileable using mod
        # TODO: Early exit : if component does not have holes, try liner time algorithm

        #TODO: Iterate over remaining empty tiles
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0.:
                    for t in trominos:

                        placed_tromino = place_tronmino(t, r,c)
                        if not placed_tromino: continue
                        if backtrack_tile() == True:
                            return True
                        remove_tromino(t,r,c)

        return False


    if backtrack_tile():
        print ('Tiling possible: ')
        print (grid)
        if RENDER: render(grid)
    else:
        print ('No Tiling exists')
