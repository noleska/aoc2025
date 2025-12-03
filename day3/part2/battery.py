class Cell:
    def __init__(self, jolt: int):
        self.jolt = jolt
        self.turned_on = False

    def turn_on(self):
        self.turned_on = True
    
    def is_turned_on(self):
        return self.turned_on


class Array:
    def __init__(self):
        self.cells = []

    #def add_cell(self, cell: Cell):
    #    self.cells.append(Cell())
    def add_cell(self, cell: Cell):
        self.cells.append(cell)
    
    def turn_on_max_jolt_cells(self, num_to_turn_on):
        for i in range(num_to_turn_on):
            off_cells = []
            for cell in self.cells:
                if cell.is_turned_on() == False:
                    off_cells.append(cell)
            #off_cells = [cell for cell in self.cells if cell.is_turned_on == False]
            high_jolt = max(off_cells)
            for cell in self.cells:
                if cell.jolt == high_jolt and cell.is_turned_on() == False:
                    cell.turn_on()
    
    def report_joltage(self):
        return int("".join([str(cell.jolt) for cell in self.cells if cell.is_turned_on()== True]))
    


    

    