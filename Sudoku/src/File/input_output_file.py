'''
Created on Jul 3, 2013

@author: Arnold Huanca
'''


class IO_File():
    
    def __init__ (self, filename):
        self.filename = filename
    
    def input_file(self, sep='\n'):
        "Parse a file into a list of strings, separated by sep."
        return file(self.filename).read().strip().split(sep)
    

    def output_file(self, values):
        """Display as 2-D grid """
        export_file = open("Sudoku_Exported.txt", 'w')
        export_file.write('    SUDOKU RESOLVED \n\n')
        width = 3
        line = '+'.join(['-'*(width*3)]*3)
        for r in 'ABCDEFGHI':
            export_file.write(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in '123456789') + "\n")
            if r in 'CF':
                export_file.write(line + "\n")
        export_file.write("\n")
        export_file.close()      
