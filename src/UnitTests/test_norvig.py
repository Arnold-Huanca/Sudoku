import unittest
from Solver.norvig import Norvig
from Main.grid import Grid


class Test_norvig(unittest.TestCase):


    def setUp(self):
        self.gridA='003020600900305001001806400008102900700000008006708200002609500800203009005010300'
        self.gridA_expected={'I6': '7', 'H9': '9', 'I2': '9', 'E8': '3', 'H3': '4', 'H7': '7', 'I7': '3', 'I4': '4', 'H5': '5', 'F9': '5', 'G7': '5', 'G6': '9', 'G5': '8', 'E1': '7', 'G3': '2', 'G2': '7', 'G1': '3', 'I1': '6', 'C8': '9', 'I3': '5', 'E5': '6', 'I5': '1', 'C9': '3', 'G9': '4', 'G8': '1', 'A1': '4', 'A3': '3', 'A2': '8', 'A5': '2', 'A4': '9', 'A7': '6', 'A6': '1', 'C3': '1', 'C2': '5', 'C1': '2', 'E6': '4', 'C7': '4', 'C6': '6', 'C5': '7', 'C4': '8', 'I9': '2', 'D8': '7', 'I8': '8', 'E4': '5', 'D9': '6', 'H8': '6', 'F6': '8', 'A9': '7', 'G4': '6', 'A8': '5', 'E7': '1', 'E3': '9', 'F1': '1', 'F2': '3', 'F3': '6', 'F4': '7', 'F5': '9', 'E2': '2', 'F7': '2', 'F8': '4', 'D2': '4', 'H1': '8', 'H6': '3', 'H2': '1', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '4', 'B6': '5', 'B7': '8', 'E9': '8', 'B1': '9', 'B2': '6', 'B3': '7', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '3', 'B8': '2', 'B9': '1', 'D1': '5'}
        self.gridB='52...6.........7.13...........4..8..6......5...........418.........3..2...87.....'
        self.gridB_expected={'G7': '6', 'G6': '5', 'G5': '2', 'G4': '8', 'G3': '1', 'G2': '4', 'G1': '9', 'G9': '3', 'G8': '7', 'C9': '2', 'C8': '6', 'C3': '4', 'C2': '1', 'C1': '3', 'C7': '5', 'C6': '7', 'C5': '8', 'C4': '9', 'E5': '7', 'E4': '2', 'F1': '4', 'F2': '5', 'F3': '3', 'F4': '6', 'F5': '9', 'F6': '8', 'F7': '2', 'F8': '1', 'F9': '7', 'B4': '5', 'B5': '4', 'B6': '2', 'B7': '7', 'B1': '8', 'B2': '9', 'B3': '6', 'B8': '3', 'B9': '1', 'I9': '5', 'I8': '4', 'I1': '2', 'I3': '8', 'I2': '3', 'I5': '6', 'I4': '7', 'I7': '1', 'I6': '9', 'A1': '5', 'A3': '7', 'A2': '2', 'E9': '4', 'A4': '3', 'A7': '4', 'A6': '6', 'A9': '9', 'A8': '8', 'E7': '3', 'E6': '1', 'E1': '6', 'E3': '9', 'E2': '8', 'E8': '5', 'A5': '1', 'H8': '2', 'H9': '8', 'H2': '6', 'H3': '5', 'H1': '7', 'H6': '4', 'H7': '9', 'H4': '1', 'H5': '3', 'D8': '9', 'D9': '6', 'D6': '3', 'D7': '8', 'D4': '4', 'D5': '5', 'D2': '7', 'D3': '2', 'D1': '1'}
        
        self.norvig=Norvig()
        self.grid=Grid()

           

    def test_solve_a_easy_grid_using_norvig(self):
        grid2=self.norvig.solve(self.gridA)
        self.assertEquals(self.gridA_expected,grid2)
        print "Easy GridA: ", self.gridA
        print "test_solve_a_easy_grid_using_norvig"
        self.grid.raw_grid = self.gridA
        self.grid.display(grid2)
        

    def test_solve_a_Hard_grid_using_norvig(self):
        grid2=self.norvig.solve(self.gridB)
        self.assertEquals(self.gridB_expected,grid2)
        print "hard GridB: ", self.gridB
        print "test_solve_a_hard_grid_using_norvig"
        self.grid.raw_grid = self.gridB
        self.grid.display(grid2)
        
        #self.assertEqual(self.grid_expected, grid1)

    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
