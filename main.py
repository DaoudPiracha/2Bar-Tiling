import numpy as np
from helpers import render

class TrominoTiler():
    def __init__(self, grid, holes, RENDER = False):
        self.grid = grid
        self.holes = holes
        self.RENDER = RENDER
        self.trominos = {
             1: [(0,0), (0,1), (0,2)],
            -1: [(0,0), (1,0), (2,0)],
            }

    def checkCoord(self, r, c, search_state):
        '''
        checks if given r,c lies within grid and if it is unoccupied
        '''
        m,n  = self.grid.shape

        if (r, c) in self.holes: return False
        if r >= 0 and r < m and c >= 0 and c < n:
            if self.grid[r][c] == search_state: return True
        return False


    def place_tronmino(self, tromino, r, c):
        '''
        if possible, place tromino on grid, starting at (r,c)
        tromino expected to be key in dict trominos

        returns: Boolean True if placed else False
        '''
        coords = [[r + i, c + j] for i, j in trominos[tromino]]
        coords_empty = [self.checkCoord(i, j, search_state=0.)
                        for i, j in coords]

        if not all(coords_empty): return False
        else:
            for i, j in coords:
                self.grid[i][j] = tromino
        return True

    def remove_tromino(self, tromino, r, c):
        '''
        if specificed tromino exists at (r,c), remove from grid
        tromino expected to be key in dict trominos
        '''
        coords = [(r + i, c + j) for i, j in trominos[tromino]]
        coords_full = [self.checkCoord(i, j, search_state=tromino)
                       for i, j in coords]

        if all(coords_full):
            for i, j in coords:
                self.grid[i][j] = 0


    def backtrack(self):
        '''
        Backtracking approach places tromino on empty tile,
        continues to search in remaining space, exits if
        tiling found or exhausted all search space
        '''

        #check if all required tiles covered
        m,n  = self.grid.shape
        if np.sum(np.abs(self.grid)) == m*n - len(self.holes):
            return True
        # check if remaining tiles untilable
        if np.sum(np.abs(self.grid)) %3 != 0:
            return False

        # TODO: Early exit: if a component is not tileable using mod
        # TODO: Early exit : if component does not have holes, try liner time algorithm

        #TODO: Iterate over remaining empty tiles
        for r in range(m):
            for c in range(n):
                if self.grid[r][c] == 0.:
                    for t in self.trominos:

                        if not self.place_tronmino(t, r,c):
                            continue
                        #backtrack over changed grid
                        if self.backtrack() == True:
                            return True
                        self.remove_tromino(t,r,c)

        return False

if __name__ == '__main__':

    grid = np.zeros((4,6))

    holes = set([(0,3), (4,4), (4,5)])
    trominos = {
        1: [(0,0), (0,1), (0,2)],
        -1: [(0,0), (1,0), (2,0)],
        }
    RENDER = True


    tiling_search = TrominoTiler(grid, holes, RENDER)

    if tiling_search.backtrack():
        print ('Tiling Possible: ')
        print (grid)
        if RENDER: render(grid)
    else:
        print ('No Tiling Exists')
