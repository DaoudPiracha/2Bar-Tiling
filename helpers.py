import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


def render(tiling):
    m, n = tiling.shape
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