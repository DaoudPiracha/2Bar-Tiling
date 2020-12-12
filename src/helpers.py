import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


def render(tiling):
    '''
    tiling: takes input numpy grid st. 0 -> holes/empty
                                       1 -> vertical bar
                                       -1 -> horizontal bar

        Shows a colorized grid of tiles and holes.
        Blue = Vertical Bar
        Red = Horizontal Bar
        Black = Hole

        #FIXME: Fix axis numbers in plot

    '''

    m, n = tiling.shape
    cmap = colors.ListedColormap(['red', 'black', 'blue'])
    bounds = [-1.5, -0.5, 0.5, 1.5]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(tiling, cmap=cmap, norm=norm)

    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=3)
    ax.set_xticks(np.arange(-0.5, n, 1))
    ax.set_yticks(np.arange(-0.5, m, 1))

    plt.show()