import os


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

import battery

# read input
input_values_list = []
with open('input.txt','r') as f:
    for val in f.readlines():
        input_values_list.append(val.strip())

for input_value in input_values_list:
    batt_array = battery.Array()
    [batt_array.add_cell(battery.Cell(int(x)) for x in list(input_value))]
    batt_array.turn_on_max_jolt_cells(12)
    print(batt_array.report_joltage)
    

print('hello')
    
