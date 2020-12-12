import unittest
import numpy as np
from src.tiler import TrominoTiler

class TestTiler(unittest.TestCase):

    def setUp(self) -> None:
        grid = np.zeros((3, 3))
        holes = {}

        self.tiler =  TrominoTiler(grid, holes)


    def testPutHorizontalBar(self):
        self.tiler.place_tronmino(1, 0, 0)
        out = np.zeros_like(self.tiler.grid)
        out[0, 0:3] = 1.
        self.assertTrue((self.tiler.grid == out).all())

    def testInvalidHorizontalBar(self):
        self.tiler.place_tronmino(1, 0, 1)
        out = np.zeros_like(self.tiler.grid)
        self.assertTrue((self.tiler.grid == out).all())

    def testPutVerticalBar(self):
        self.tiler.place_tronmino(-1, 0, 0)
        out = np.zeros_like(self.tiler.grid)
        out[0:3, 0] = -1.

        self.assertTrue((self.tiler.grid == out).all())

    def testInvalidVerticalBar(self):
        self.tiler.place_tronmino(-1, 1, 0)
        out = np.zeros_like(self.tiler.grid)
        self.assertTrue((self.tiler.grid == out).all())

    def testRemoveSameType(self):
        self.tiler.place_tronmino(1, 0, 0)
        self.tiler.remove_tromino(1, 0, 0)
        out = np.zeros_like(self.tiler.grid)
        self.assertTrue((self.tiler.grid == out).all())

    def testRemoveDiffTypeHV(self):
        self.tiler.place_tronmino(1, 0, 0)
        self.tiler.remove_tromino(-1, 0, 0)
        out = np.zeros_like(self.tiler.grid)
        out[0, 0:3] = 1.
        self.assertTrue((self.tiler.grid == out).all())

    def testRemoveDiffTypeVH(self):
        self.tiler.place_tronmino(-1, 0, 0)
        self.tiler.remove_tromino(1, 0, 0)
        out = np.zeros_like(self.tiler.grid)
        out[0:3, 0] = -1.
        self.assertTrue((self.tiler.grid == out).all())

    def testSolverEasy(self):
        self.assertTrue(self.tiler.backtrack())

    def testSolverImpossibleCheck(self):
        self.tiler.holes = {(0,0)}
        self.assertFalse(self.tiler.backtrack())


    def testSolverMediumCase(self):
        self.tiler.grid = np.zeros((4, 6))

        self.tiler.holes = {(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (4, 5)}
        self.assertTrue(self.tiler.backtrack())
