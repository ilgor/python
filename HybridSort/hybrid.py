import sys
from timeit import default_timer as timer
from random import randint


def sort(arr):
	merge_sort(arr, 0, len(arr)-1)	


def merge_sort(arr, start, end):
	arr_size = end - start
	if arr_size > 0 and arr_size < 43:
		middle = (start + end) // 2
		merge_sort(arr, start, middle)
		merge_sort(arr, middle+1, end)
		merge(arr, start, middle+1, end)
	if arr_size >= 43:
		insersion_sort(arr, start, end)


def insersion_sort(arr, start, end):
	for i in range(start+1, end+1):
		key = arr[i]
		j = i - 1

		while j >= 0 and arr[j] > key:
			arr[j+1] = arr[j]
			j -= 1

		arr[j+1] = key


def merge(arr, start, middle, end):
	left = arr[start : middle]
	right = arr[middle : end+1]
	left.append(sys.maxsize)
	right.append(sys.maxsize)
	l = r = 0

	for n in range(start, end + 1):
		if left[l] <= right[r]:
			arr[n] = left[l]
			l += 1
		else:
			arr[n] = right[r]
			r += 1


base_arr = [randint(0,100) for n in range(10)]

arr = base_arr
start = timer()
sort(arr)
end = timer()
merge_sort_time = end - start
print(arr)

arr = base_arr
start = timer()
insersion_sort(arr, 0, len(arr)-1)
end = timer()
insersion_sort_time = end - start
print(arr)

print(merge_sort_time)
print(insersion_sort_time)
if (merge_sort_time > insersion_sort_time):
	print('insersion sort is faster')
else:
	print('merge sort is faster')