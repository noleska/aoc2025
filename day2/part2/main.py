import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# read input
with open('input.txt','r') as f:
    idranges = f.readline().split(',')


def divisors(x):
    # find whole-number divisors of char len of input
    sx = str(x)
    divisors = [1]
    for i in range (2,int(len(sx)/2)+1):
        if int(len(sx)) % i == 0:
            divisors.append(i)
    #print(len(str(x)),divisors)
    return divisors


def split_by_divisors(x):
    ''' split a number string into all possible equally divided (by character number) sets
        and return those sets as a list of lists of strings
    ''' 
    sx = str(x)
    ref_index_sets = []
    for divisor in divisors(x):
        ref_indices = []
        num_of_subsets = int(len(sx)/divisor)
        for i in range(0,num_of_subsets):
            ref_indices.append([i*divisor,(i*divisor)+divisor])
        ref_index_sets.append(ref_indices)

    out = []
    for ref_set in ref_index_sets:
        this_set = []
        for slc in ref_set:
            this_set.append(sx[slc[0]:slc[1]])
        #print(str(x),len(str(x)),divisors(x),'\n',this_set)
        out.append(this_set)
    return out


def value_if_invalid(x:int):
    sx = str(x) # string ver for char indexing
    if len(sx) < 2: # a single-digit number can't contain repeats
        return 0
    value_sets = split_by_divisors(x)
    for value_set in value_sets:
        if len(set(value_set)) <= 1:
            print(x)
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