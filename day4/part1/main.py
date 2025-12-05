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
    def __init__(self, x:int, y:int, has_paper = False):
        self.x = x
        self.y = y
        self.has_paper = has_paper

    def neighbor_roll_count(self, grid):
        neighbor_coords = [{x:self.x-1, y:self.y-1},
                           {x:self.x-1, y:self.y},
                           {x:self.x-1, y:self.y+1},
                           {x:self.x,   y:self.y-1},
                           {x:self.x,   y:self.y+1},
                           {x:self.x+1, y:self.y-1},
                           {x:self.x+1, y:self.y},
                           {x:self.x+1, y:self.y+1}]
        count = 0
        for ncoord in neighbor_coords:
            try:
                neighbor = grid[ncoord[x]][ncoord[y]]
                if neighbor.has_paper:
                    count += 1
            except Exception as e:
                pass
        return count
    
# Instantiate empty grid
empty_line = [None] * len(lines[0])
grid = [empty_line] * len(lines)

# Populate grid
x = 0
for row in lines:
    y = 0
    for item in row:
        print(item)
        grid[y][x] = Position(x=x,y=y, has_paper = (item == "@"))


# Display grid
pout = []
for row in grid:
    temp = ""
    for item in row:
        if item.has_paper:
            temp+= "@"
        else:
            temp+= "."
        #temp += str(item.has_paper)
    pout.append(temp)

for bb in pout:
    print(bb)


# Get accessible paper roll total
total = 0
for line in grid:
    for pos in line:
        #print(pos.has_paper)
        neighbor_roll_count = pos.neighbor_roll_count(grid = grid)
        #print(neighbor_roll_count)
        if pos.neighbor_roll_count(grid = grid) < 4:
            total +=1

print(total)






