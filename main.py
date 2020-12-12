import numpy as np

from src.tiler import TrominoTiler
from src.helpers import render


if __name__ == '__main__':

    grid = np.zeros((4, 6))

    holes = {(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (4, 5)}
    trominos = {
        1: [(0, 0), (0, 1), (0, 2)],
        -1: [(0, 0), (1, 0), (2, 0)],
    }
    RENDER = True

    tiling_search = TrominoTiler(grid, holes, RENDER)


    if tiling_search.backtrack():
        print('Tiling Possible: ')
        print(grid)
        if RENDER: render(grid)
    else:
        print('No Tiling Exists')
