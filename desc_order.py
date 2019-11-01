
#used bubble sort for this sorting problem

def Descending_Order(num):
    num = str(num)
    num = list(num)
    lgt = len(num)-1
    sorted = False
    while not sorted:
        sorted=True
        for i in range(lgt):
            if num[i]<num[i+1]:
                sorted=False
                num[i], num[i+1] = num[i+1], num[i]
    out=""
    for nr in num:
        out += str(nr)
    out = int(out)
    return out
print(Descending_Order(451286)) #example

