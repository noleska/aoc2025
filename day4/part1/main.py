import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


# Read input
lines = []
with open("testinput.txt",'r') as f:
    for line in f.readlines():
        lines.append(line.strip())


class Position:
    def __init__(self, row:int, col:int, has_paper = False):
        self.row = row
        self.col = col
        self.has_paper = has_paper

    def neighbor_roll_count(self, grid):
        neighbor_coords = [{'row':self.row-1, 'col':self.col-1},
                           {'row':self.row-1, 'col':self.col},
                           {'row':self.row-1, 'col':self.col+1},
                           {'row':self.row,   'col':self.col-1},
                           {'row':self.row,   'col':self.col+1},
                           {'row':self.row+1, 'col':self.col-1},
                           {'row':self.row+1, 'col':self.col},
                           {'row':self.row+1, 'col':self.col+1}]
        count = 0
        for ncoord in neighbor_coords:
            try:
                neighbor = grid[ncoord['row']][ncoord['col']]
                if neighbor.has_paper:
                    count += 1
            except Exception as e:
                pass
        return count
    
# Instantiate empty grid
gridrow = [None] * len(lines[0])
grid = [gridrow] * len(lines)
row = 0

grid[5][5] = 'x'



