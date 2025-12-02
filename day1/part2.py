import DCLL2

dcllist = DCLL2.DCLL()
for i in range(0,100):
    dcllist.append(i)

dcllist.traverse_right(count = 50)
print(dcllist.current.data)

inputlist = []
with open('input2.txt','r') as f:
    for line in f:
        inputlist.append(line.strip())

def spin(dir, count):
    if dir == 'R' :
        dcllist.traverse_right(count)
    if dir == 'L' :
        dcllist.traverse_left(count)
    return dcllist.current.data

for instruction in inputlist:
    dir = instruction[0]
    count = int(instruction[1:])
    print(count)
    spin(dir, count)


print('zcount:', dcllist.zerocount)

    
