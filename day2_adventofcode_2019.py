#problem of advent's day 2 from https://adventofcode.com/ (2019)

f= open("input_day2.txt","r")
orig_list=list(map(int, f.read().split(',')))

def intcode(list_dig): #op code for the listed digits
    for n in range(len(list_dig)):
        assert(isinstance(list_dig[n],int)) #condition: insert a list of integers!
        
        if n%4==0 & n<len(list_dig)-1:
            n0=list_dig[n+3]
            n1=list_dig[n+1]
            n2=list_dig[n+2]
            if list_dig[n]==1:
                list_dig[n0] = list_dig[n1]+list_dig[n2]
            elif list_dig[n]==2:
                list_dig[n0] = list_dig[n1]*list_dig[n2]
            if list_dig[n]==99:
                break
    return list_dig[0]

numbers=[]
for i in range(len(orig_list)):
    if i ==1: numbers.append(12)
    elif i ==2: 
        numbers.append(2)
    else: numbers.append(int(orig_list[i]))
print(intcode(numbers))

#part 2:

from itertools import product
output=19690720

numbers=[]
for i in range(len(orig_list)):
    numbers.append(int(orig_list[i]))

for noun, verb in product(range(0, 100), range(0, 100)):
    numbers[1]=noun
    numbers[2]=verb
    intcode(numbers)
    if numbers[0]==output:
        print(100*numbers[1]+numbers[2])
        break
    else: 
        numbers=[]
        for i in range(len(orig_list)):
            numbers.append(int(orig_list[i]))
