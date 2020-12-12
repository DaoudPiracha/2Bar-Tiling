import numpy as np
# from scipy.ndimage.measurements import label

class TrominoTiler:
    def __init__(self, grid, holes, render=False):

        self.grid = grid
        self.holes = holes
        self.RENDER = render
        self.trominos = {
            1: [(0, 0), (0, 1), (0, 2)],
            -1: [(0, 0), (1, 0), (2, 0)]
        }

    def check_coord(self, r, c, search_state):
        """
        checks if given r,c lies within grid and if it is unoccupied
        """
        m, n = self.grid.shape

        if (r, c) in self.holes:
            return False
        if 0 <= r < m and 0 <= c < n:
            if self.grid[r][c] == search_state:
                return True
        return False

    def place_tronmino(self, tromino, r, c):
        """
        if possible, place tromino on grid, starting at (r,c)
        tromino expected to be key in dict trominos

        returns: Boolean True if placed else False
        """
        coords = [[r + i, c + j] for i, j in self.trominos[tromino]]
        coords_empty = [self.check_coord(i, j, search_state=0.)
                        for i, j in coords]

        if not all(coords_empty):
            return False
        else:
            for i, j in coords:
                self.grid[i][j] = tromino
        return True

    def remove_tromino(self, tromino, r, c):
        """
        if specificed tromino exists at (r,c), remove from grid
        tromino expected to be key in dict trominos
        """
        coords = [(r + i, c + j) for i, j in self.trominos[tromino]]
        coords_full = [self.check_coord(i, j, search_state=tromino)
                       for i, j in coords]

        if all(coords_full):
            for i, j in coords:
                self.grid[i][j] = 0

    def get_components(self):
        """
        uses optimized scipy method to find and label
        connected components in graph

        SciPy source: https://stackoverflow.com/questions/46737409/finding-connected-components-in-a-pixel-array

        :return: tuple (int: components, np.array: labels)
        """

        structure = np.ones((3, 3), dtype=np.int)
        labeled, n_components = label(self.grid, structure)
        return n_components, labeled

    def check_component_parity(self, components, labelled):
        """
        takes output from get_component method,
        checks if each component is tileable

        returns: Boolean True if not all components untileable
        """

        unique, counts = np.unique(labelled, return_counts=True)
        component_sizes = dict(zip(unique, counts))
        for i in range(1, components + 1):
            if (component_sizes[i]) % 3 != 0:
                return False
        return True

    def backtrack(self, check_components=False):
        """
        Backtracking approach places tromino on empty tile,
        continues to search in remaining space, exits if
        tiling found or exhausted all search space

        FLAG Check Component: checks whether each sub-component is untileable

        """

        # check if all required tiles covered
        m, n = self.grid.shape
        if np.sum(np.abs(self.grid)) == m * n - len(self.holes):
            return True
        # check if remaining tiles untilable
        if np.sum(np.abs(self.grid)) % 3 != 0:
            return False

        # if multiple components, check if not untileable using bars, i.e mod 3
        if check_components:
            components, labelled = self.get_components()
            if components >= 2:
                if not self.check_component_parity(components, labelled):
                    return False

        # TODO: Early exit : if component does not have holes,
        #                    try liner time algorithm

        # TODO: Iterate over set of remaining empty tiles instead of all
        for r in range(m):
            for c in range(n):
                if self.grid[r][c] == 0.:
                    for t in self.trominos:

                        if not self.place_tronmino(t, r, c):
                            continue
                        # backtrack over changed grid
                        if self.backtrack() is True:
                            return True
                        self.remove_tromino(t, r, c)

        return False

