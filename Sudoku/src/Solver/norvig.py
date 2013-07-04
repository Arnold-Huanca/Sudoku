from Main.grid import Grid
from Solver.solve_algorithm import Solve_Algorithm

"""this class is using some attributes from grid like:squares, cols, rows and this needs a value (not a grid) to print""" 
class Norvig (Solve_Algorithm):

    def __init__(self):
        self.grid=Grid()
        
    ##########try to fill the grid  with possible values########################    
    def grid_to_dict(self,grid):#this resolve the grid inserted and return the grid filled
        """Convert grid to a dict of possible values, {square: digits}, or
        return False if a contradiction is detected."""
        ## To start, every square can be any digit; then eliminate_other_value values from the grid.
        values = dict((s,self.grid.digits) for s in self.grid.squares)
        for s,d in self.grid.set_values(grid).items():
            if d in self.grid.digits and not self.eliminate_other_value(values, s, d):
                return False ## (Fail if we can't eliminate_other_value d to square s.)
        return values

    ################ Constraint Propagation ################
    
    def eliminate_other_value(self, values, s, d):
        """Eliminate all the other values (except d) from values[s] and propagate.
        Return values, except return False if a contradiction is detected."""
        other_values = values[s].replace(d, '')
        if all(self.eliminate(values, s, d2) for d2 in other_values):
            return values
        else:
            return False
        
    def eliminate(self,values, s, d):
        """Eliminate d from values[s]; propagate when values or places <= 2.
        Return values, except return False if a contradiction is detected."""
        if d not in values[s]:
            return values ## Already eliminated
        values[s] = values[s].replace(d,'')
        ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
        if len(values[s]) == 0:
            return False ## Contradiction: removed last value
        elif len(values[s]) == 1:
            d2 = values[s]
            if not all(self.eliminate(values, s2, d2) for s2 in self.grid.peers[s]):
                return False
        ## (2) If a unit u is reduced to only one place for a value d, then put it there.
        for u in self.grid.units[s]:
            dplaces = [s for s in u if d in values[s]]
            if len(dplaces) == 0:
                return False ## Contradiction: no place for this value
            elif len(dplaces) == 1:
                # d can only be in one place in unit; eliminate_other_value it there
                if not self.eliminate_other_value(values, dplaces[0], d):
                    return False
        return values
    
################ Solve ################
    def solve(self,gridA): 
        return self.search(self.grid_to_dict(gridA))
 
################ Search ################   
    def search(self,values):
        "Using depth-first search and propagation, try all possible values."
        if values is False:
            return False ## Failed earlier
        if all(len(values[s]) == 1 for s in self.grid.squares):
            return values ## Solved!
        ## Chose the unfilled square s with the fewest possibilities
        n,s = min((len(values[s]), s) for s in self.grid.squares if len(values[s]) > 1)
        return self.return_some_value(self.search(self.eliminate_other_value(values.copy(), s, d))
                    for d in values[s])
      
    
    def return_some_value(self,seq):
        "Return return_some_value element of seq that is true."
        for e in seq:
            if e: return e
        return False
        