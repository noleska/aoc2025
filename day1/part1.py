import DCLL

dcllist = DCLL.DCLL()
for i in range(0,100):
    dcllist.append(i)

dcllist.traverse_right(count = 50)
print(dcllist.current.data)

inputlist = []
with open('input1.txt','r') as f:
    for line in f:
        inputlist.append(line.strip())

def spin(dir, count):
    if dir == 'R' :
        dcllist.traverse_right(count)
    if dir == 'L' :
        dcllist.traverse_left(count)
    return dcllist.current.data

zerocount = 0
for instruction in inputlist:
    dir = instruction[0]
    count = int(instruction[1:])
    print(count)
    spinresult = spin(dir, count)
    if spinresult == 0:
        zerocount += 1

print('zcount:', zerocount)

    
