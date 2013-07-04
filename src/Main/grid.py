class Grid:
    
    def __init__(self):
        
        self.raw_grid = None
        self.digits   = '123456789'
        self.rows     = 'ABCDEFGHI'
        self.cols     = self.digits
        self.var_name=''
        self.time_show=''
        self.squares  = self.__set_matrix__(self.rows, self.cols)
        self.unitlist = ([self.__set_matrix__(self.rows, c) for c in self.cols] +
            [self.__set_matrix__(r, self.cols) for r in self.rows] +
            [self.__set_matrix__(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

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
      
    def __set_matrix__(self, A, B):
        "__set_matrix__ product of elements in A and elements in B."
        return [a+b for a in A for b in B]
    
    
    def set_values(self,grid):#this only create the grid using a grid list
        "Convert grid into a dict of {square: char} with '0' or '.' for empties."
        chars = [c for c in grid if c in self.digits or c in '0.']
        if len(chars) == 81:
            return dict(zip(self.squares, chars))
        else: return False
        
    def display(self,values):
        
        output_file = self.__create_output_file__(self.var_name+'.txt') 
        
        "Display these values as a 2-D grid."
        width = 1+max(len(values[s]) for s in self.squares)
        line = '+'.join(['-'*(width*3)]*3)
        solved_row = ''
        for r in self.rows:
            "Before print on console, add the rows to the output var" 
            solved_row += ''.join(values[r+c].center(width)+('|' if c in '36' else '')for c in self.cols) 
            solved_row += '\n'
            
            if r in 'CF':
                "Add to output var"
                solved_row += (line+'\n')
                
        "Write the results on output file"
        output_file.write(solved_row+'\n')
        output_file.close()
        
        print (solved_row)
        
    "Function to create an output file where the results will be appended"
    def __create_output_file__(self, file_name):
        "var to open or create an output file"
        output_file = open(file_name,'w+')
        
        "First we add to the output file the grid before been solved"
        output_file.write(self.var_name+'\n\n')
        output_file.write('solved in '+self.time_show+'\n\n')
        output_file.write('The grid given to solve is:\n\n')
        output_file.write(self.raw_grid)
        output_file.write('\n\nThe grid solved is:\n\n')
        
        return output_file
    
    def validate_values(self,grid):
        "validate if the grid is wrong or have more than 81"
        chars = [c for c in grid if c in self.digits or c in '0.']
        if len(chars) == 81:
            return True
        else: return False