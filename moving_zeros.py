###########################3
# from codewars: https://www.codewars.com/kata/52597aa56021e91c93000cb0
def move_zeros(array):
    zeros=[]
    output=[]
    for i in array:
        if type(i) is int and i == 0:
            zeros.append(i)
        elif type(i) is float and i == 0.0:
            zeros.append(i)
        else: output.append(i)
    for i in zeros:
        output.append(i)
    return output
