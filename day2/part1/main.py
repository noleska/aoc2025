import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# read input
with open('input.txt','r') as f:
    idranges = f.readline().split(',')

def value_if_invalid(x:int):
    sx = str(x) # string ver for char indexing
    # numbers with odd position/character count are valid
    if len(sx) % 2 != 0:
        return 0
    i2 = int(len(sx)/2) # index of beginning of second half
    firsthalf = sx[0:i2]
    secondhalf = sx[i2:]
    if firsthalf == secondhalf:
        return x
    return 0

sum_of_invalid_ids = 0
for idrange in idranges:
    splitstr = idrange.split('-')
    startid = int(splitstr[0])
    endid = int(splitstr[1])
    idlist = [i for i in range(startid,endid+1)]
    for id in idlist:
        sum_of_invalid_ids += value_if_invalid(id)
    
print(sum_of_invalid_ids)