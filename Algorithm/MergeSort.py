import random


def mergesort_2(arr,low, high):
    if low < high:
        mid = (low + high)//2
        # the first half
        mergesort_2(arr,low, mid)
        # the second half
        mergesort_2(arr,mid+1, high)
        merge2(arr,low, mid, high)


def merge2(Arr, low, mid, high) :

	temp = [0] * (high - low + 1)
	i, j, k = low, mid+1, 0

	while(i <= mid and j <= high) :
		if(Arr[i] <= Arr[j]) :
			temp[k] = Arr[i]
			k += 1; i += 1
		else :
			temp[k] = Arr[j]
			k += 1; j += 1

	while(i <= mid) :
		temp[k] = Arr[i]
		k += 1; i += 1

	while(j <= high) :
		temp[k] = Arr[j]
		k += 1; j += 1

	for i in range (low, high+1) :
		Arr[i] = temp[i - low]

if __name__ == '__main__':
    num = int(input('Enter A Number : '))
    if num > 1:
        ls = random.sample(range(1, 100), num)
    print(f'Before Merge Sort: {ls}', end='\n')
    mergesort_2(ls,0, len(ls)-1)
    print(f'After Merge Sort: {ls}', end='\n')