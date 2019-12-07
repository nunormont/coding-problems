#problem of day 1 of advent from https://adventofcode.com/

import math
f= open("input.txt","r")
masses=f.readlines()
all_fuel=0
for i in masses:
    all_fuel+=math.floor(int(i)/3)-2

print(all_fuel)

#part 2:
tot_fuel=0
for i in masses:
    fuel=math.floor(int(i)/3)-2
    tot_fuel+=fuel
    added_fuel=[]
    while math.floor(fuel/3)-2 > 0:
        fuel=math.floor(fuel/3)-2
        tot_fuel+=fuel
print(tot_fuel)
