from Main.grid import Grid
from Solver.solve_algorithm import Solve_Algorithm

class Brute (Solve_Algorithm):
    
    "Function to initialize global attributes"
    def __init__(self):
        
        "Var to get the values of the Sudoku grid"
        self.gridFromFile=('')
        
        "Heir from Grid class"
        self.grid = Grid()
        
        "Values of unsolved grid"
        self.values = None
        
        "Dictionary with Empty Values only"
        self.emptyValues = None
              
        "List of lists to register moves for each empty cell"
        self.moves_per_cell = None
    
    def solve(self,grid):
        self.values = self.grid.set_values(grid)
        self.emptyValues = self.grid_empty_values(self.values)
        self.moves_per_cell = [[] for i in range(len(self.emptyValues.keys()))]
        self.start()
        return self.values
        
    def grid_empty_values(self,grid):
        "Return a dict of empties."
        empties = []
        for key,value in grid.items():
            if(value == '0'):
                empties.append((key,value)) 
        return dict(empties)    
            
    def check_square(self,num,key):
        flag = True
        iniRow, iniCol = self.get_ini_row_and_ini_col(key)
        limRow = iniRow + 2
        aux = iniCol
        limCol = iniCol + 2
        while iniRow <= limRow and flag:
            iniCol = aux
            while iniCol <= limCol:
                if(self.values[self.grid.rows[iniRow]+str(iniCol)] == num):
                    flag = False
                    break
                iniCol += 1
            iniRow += 1
        return flag
       
    def check_lines(self,num, key):
        flag = True
        row = key[0]
        col = key[1]
        
        for i in range(1,10):
            if(self.values[(row+str(i))] == num):
                flag = False
                break
        if(flag):
            for j in range(0,9):
                if(self.values[self.grid.rows[j]+col] == num):
                    flag = False
                    break
        return flag
    
    def start(self):
        
        pos = 0
        empVals = self.emptyValues
        emptyKeys = sorted(empVals.keys())
        
        while pos < len(self.emptyValues):
            val = emptyKeys[pos]
            if(self.fill_cell(pos, val)):
                pos += 1
            else:
                self.values[val] = '0'
                self.moves_per_cell[pos] = []
                pos -= 1
        self.grid.display(self.values)
            
    def fill_cell(self,pos,key):
        cellSet = False
        for n in range(0,9):
            num = self.grid.digits[n]
            if(self.check_lines(num, key) and self.check_square(num, key) and not(num in self.moves_per_cell[pos])):
                cellSet = True
                self.values[key] = num
                self.moves_per_cell[pos].append(num)
                break
        return cellSet
         
    def get_ini_row_and_ini_col(self,key):
        
        row = key[0]
        col = key[1]

        if(row=='A' or row=='B' or row=='C'): iniRow = 0
        elif(row=='D' or row=='E' or row=='F'): iniRow = 3
        else: iniRow = 6
            
        if(col=='1' or col=='2' or col=='3'): iniCol = 1
        elif(col=='4' or col=='5' or col=='6'): iniCol = 4
        else: iniCol = 7
        return iniRow,iniCol
 
