import unittest
from Solver.norvig import Norvig
from Main.grid import Grid

class Test_norvig(unittest.TestCase):


    def setUp(self):
        self.gridA='003020600900305001001806400008102900700000008006708200002609500800203009005010300'
        self.gridB='52...6.........7.13...........4..8..6......5...........418.........3..2...87.....'
        
        self.norvig=Norvig()
        self.grid=Grid()
           

    def test_solve_a_easy_grid_using_norvig(self):
        grid2=self.norvig.solve(self.gridA)
        print "Easy GridA", self.gridA
        print "test_solve_a_easy_grid_using_norvig"
        self.grid.display(grid2)

    def test_solve_a_Hard_grid_using_norvig(self):
        grid2=self.norvig.solve(self.gridB)
        print "hard GridB", self.gridB
        print "test_solve_a_hard_grid_using_norvig"
        self.grid.display(grid2)
        
        #self.assertEqual(self.grid_expected, grid1)

    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
