#problem of advent's day 1 from https://adventofcode.com/ (2019)

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
    while math.floor(fuel/3)-2 > 0:
        fuel=math.floor(fuel/3)-2
        tot_fuel+=fuel
print(tot_fuel)
