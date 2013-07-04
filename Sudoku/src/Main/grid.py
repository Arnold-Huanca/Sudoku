class Grid:
    
    def __init__(self):
        self.digits   = '123456789'
        self.rows     = 'ABCDEFGHI'
        self.cols     = self.digits
        self.squares  = self.set_matrix(self.rows, self.cols)
        self.unitlist = ([self.set_matrix(self.rows, c) for c in self.cols] +
            [self.set_matrix(r, self.cols) for r in self.rows] +
            [self.set_matrix(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

        self.units = dict((s, [u for u in self.unitlist if s in u])
                     for s in self.squares)
        self.peers = dict((s, set(sum(self.units[s],[]))-set([s]))
                     for s in self.squares)

## Throughout this program we have:
##   r is a row,    e.g. 'A'
##   c is a column, e.g. '3'
##   s is a square, e.g. 'A3'
##   d is a digit,  e.g. '9'
##   u is a unit,   e.g. ['A1','B1','C1','D1','E1','F1','G1','H1','I1']
##   grid is a grid,e.g. 81 non-blank chars, e.g. starting with '.18...7...
##   values is a dict of possible values, e.g. {'A1':'12349', 'A2':'8', ...}  
      
    def set_matrix(self, A, B):
        "set_matrix product of elements in A and elements in B."
        return [a+b for a in A for b in B]
    
    
    def set_values(self,grid):#this only create the grid using a grid list
        "Convert grid into a dict of {square: char} with '0' or '.' for empties."
        chars = [c for c in grid if c in self.digits or c in '0.']
        if len(chars)==0:
            return False
        if len(chars) == 81:
            return dict(zip(self.squares, chars))

    def display(self,values):
        "Display these values as a 2-D grid."
        width = 1+max(len(values[s]) for s in self.squares)
        line = '+'.join(['-'*(width*3)]*3)
        for r in self.rows:
            print ''.join(values[r+c].center(width)+('|' if c in '36' else '')for c in self.cols)
            if r in 'CF': print line
        print
        
    def get_ini_row_ini_Col(self,key):
        self.row = key[0]
        self.col = key[1]
        if(self.row=='A' or self.row=='B' or self.row=='C'): iniRow = 0
        elif(self.row=='D' or self.row=='E' or self.row=='F'): iniRow = 3
        else: iniRow = 6        
        if(self.col=='1' or self.col<='2' or self.col=='3'): iniCol = 1
        elif(self.col=='4' or self.col<='5' or self.col=='6'): iniCol = 4
        else: iniCol = 7
        return iniRow,iniCol

    def checkSquare(self,grid,num,key):
            flag = True
            iniRow, iniCol = self.get_ini_row_ini_Col(self,key)
            limRow = iniRow + 2
            aux = iniCol
            limCol = iniCol + 2
            while iniRow <= limRow and flag:
                iniCol = aux
                while iniCol <= limCol:
                    if(grid[self.rows[iniRow]+str(iniCol)] == str(num)):
                        if grid[self.rows[iniRow]+str(iniCol)]=='0':
                            return True
                        flag = False
                        break
                    iniCol += 1
                iniRow += 1
            return flag