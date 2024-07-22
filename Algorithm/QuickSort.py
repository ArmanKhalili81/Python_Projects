import random

def quick(low, high):
    if low < high:
        j = partion(low, high)
        quick(low, j-1)
        quick(j+1, high)


def partion(low, high):
    i = low
    j = high
    pivotitem = ls[low]
    while (i < j) :
        while pivotitem >= ls[i] and i < len(ls):
            i+=1
        while pivotitem < ls[j] and j < len(ls):
            j-=1
        if (i < j) :
            (ls[i], ls[j]) = (ls[j],ls[i])

    (ls[low], ls[j]) = (ls[j], ls[low])
    return j


num = int(input('Enter A Number : '))
if num > 1:
    ls = random.sample(range(1, 100), num)
print(f'Before Merge Sort: {ls}', end='\n')
quick(0, len(ls)-1)
print(f'After Merge Sort: {ls}', end='\n')


     