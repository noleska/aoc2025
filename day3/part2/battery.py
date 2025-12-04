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
        self.cells_len = len(self.cells)

    #def add_cell(self, cell: Cell):
    #    self.cells.append(Cell())
    def add_cell(self, cell: Cell):
        self.cells.append(cell)


    def turn_on_max_jolt_cells(self, num_to_turn_on):
        last_cell_index_turned_on = 0
        for ntto in range(num_to_turn_on-1):
            last_index = num_to_turn_on - ntto 
            working_array = self.cells[last_cell_index_turned_on:-last_index+1]
            wa_jolts = [x.jolt for x in working_array]
            wa_max_jolt = max(wa_jolts)
            max_jolt_cell_index = wa_jolts.index(wa_max_jolt) + last_cell_index_turned_on 
            self.cells[max_jolt_cell_index].turn_on()
            last_cell_index_turned_on = max_jolt_cell_index + 1
        # weird base case because you can't iterate last index to zero
        working_array = self.cells[last_cell_index_turned_on:]
        wa_jolts = [x.jolt for x in working_array]
        wa_max_jolt = max(wa_jolts)
        max_jolt_cell_index = wa_jolts.index(wa_max_jolt)+last_cell_index_turned_on
        self.cells[max_jolt_cell_index].turn_on()
        last_cell_index_turned_on = max_jolt_cell_index


    def report_all_cell_jolts(self):
        out = ""
        for cell in self.cells:
            out = out + str(cell.jolt)
        return out
    
    def report_joltage(self):
        return int("".join([str(cell.jolt) for cell in self.cells if cell.is_turned_on()== True]))
    


    

    