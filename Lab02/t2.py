def MergeSort(arr, temp_arr, left, right):

	count = 0

	if left < right:

		mid = (left + right)//2
		count += MergeSort(arr, temp_arr, left, mid)

		count += MergeSort(arr, temp_arr, mid + 1, right)

		count += merge(arr, temp_arr, left, mid, right)
	return count

def merge(arr, temp_arr, left, mid, right):
	i = left	    # Starting index of left subarray
	j = mid + 1     # Starting index of right subarray
	k = left	    # Starting index of to be sorted subarray
	count = 0

	while i <= mid and j <= right:
    
		if arr[i] <= arr[j]:
			temp_arr[k] = arr[i]
			k += 1
			i += 1
		else:
			# Inversion will occur.
			temp_arr[k] = arr[j]
			count += (mid-i + 1)
			k += 1
			j += 1

	while i <= mid:
		temp_arr[k] = arr[i]
		k += 1
		i += 1

	while j <= right:
		temp_arr[k] = arr[j]
		k += 1
		j += 1

	for loop_var in range(left, right + 1):
		arr[loop_var] = temp_arr[loop_var]

	return count


n = int(input())
arr = list(map(int, input().split()))
temp_arr = [0]*n
result = MergeSort(arr, temp_arr, 0, n-1)
print(result)

# REF: https://www.geeksforgeeks.org/inversion-count-in-array-using-merge-sort/