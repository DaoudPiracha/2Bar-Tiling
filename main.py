import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


if __name__ == '__main__':
    m = 4
    n = 6
    grid = np.zeros((m,n))

    holes = set([(0,3), (4,4), (4,5)])
    tetrominos = {
        1: [(0,0), (0,1), (0,2)],
        -1: [(0,0), (1,0), (2,0)],
        }
    render = True


    def render(tiling):
        cmap = colors.ListedColormap(['red', 'black', 'blue'])
        bounds = [-1.5, -0.5, 0.5, 1.5]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        fig, ax = plt.subplots()
        ax.imshow(tiling, cmap=cmap, norm=norm)

        # draw gridlines
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        ax.set_xticks(np.arange(-0.5, n, 1));
        ax.set_yticks(np.arange(-0.5, m, 1));

        plt.show()
    def checkCoord(r, c, search_state, grid=grid, holes=holes):
        '''
        checks if given r,c lies within grid and if it is unoccupied
        '''

        if (r, c) in holes: return False

        if r >= 0 and r < m and c >= 0 and c < n:
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

        if not all(coords_empty): return False
        else:
            for i, j in coords:
                grid[i][j] = tetromino
        return True

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
                    for t in tetrominos:

                        placed_tromino = place_tetronmino(t, r,c)
                        if not placed_tromino: continue
                        if backtrack() == True:
                            return True
                        remove_tetronmino(t,r,c)

        return False


    print(backtrack())
    print (grid)
    render(grid)
    # rendering








# See PyCharm help at https://www.jetbrains.com/help/pycharm/
