"""Create a function that take a list and returns that list with each element multiplied by the sum of the list.
EX:
given: [1, 2, 3, 4, 5]
return: [15, 30, 45, 60, 75]"""

def multi(list=[]):
    newlist = []
    for item in list:
        newlist.append(item * sum(list))
    return newlist

print(multi([2, 3, 4, 5]))
