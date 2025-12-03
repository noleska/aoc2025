import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# read input
input_values_list = []
with open('input.txt','r') as f:
    for val in f.readlines():
        input_values_list.append(val.strip())

total_joltage = 0
for input_value in input_values_list:
    ints_list = [int(x) for x in list(input_value)]
    first_digit = max(ints_list[:-1])
    remainder_of_list = ints_list[ints_list.index(first_digit)+1:]
    second_digit = max(remainder_of_list)
    largest_possible_joltage = int(str(first_digit) + str(second_digit))
    total_joltage += largest_possible_joltage

print(total_joltage)
    
