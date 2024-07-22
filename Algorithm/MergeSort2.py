import random

def mergesort(master_ls):
    if len(master_ls) > 1:
        mid = len(master_ls)//2
        ls1 = master_ls[:mid]
        ls2 = master_ls[mid:]
        # the first half
        mergesort(ls1)
        # the second half
        mergesort(ls2)
        i = j = k = 0
        while i < len(ls1) and j < len(ls2):
            if ls1[i] < ls2[j]:
                master_ls[k] = ls1[i]
                i += 1
            else:
                master_ls[k] = ls2[j]
                j += 1
            k += 1

        while i < len(ls1):
            master_ls[k] = ls1[i]
            i += 1
            k += 1

        while j < len(ls2):
            master_ls[k] = ls2[j]
            j += 1
            k += 1


if __name__ == '__main__':
    num = int(input('Enter A Number : '))
    if num > 1:
        ls = random.sample(range(1, 100), num)
    print(f'Before Merge Sort: {ls}', end='\n')
    mergesort(ls)
    print(f'After Merge Sort: {ls}', end='\n')
