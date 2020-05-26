#Quick Sort

main_list = []

def Quick_sort():

	global main_list

	list_size = int(input("Enter the size of list : "))

	print("Enter the numbers in list : ")

	for num in range(0,list_size):
		list_value = int(input())
		main_list.append(list_value)

	sort_list(main_list,0,len(main_list)-1)

def sort_list(main_list,low,high):

	if low < high:
		mid = partition(main_list,low,high)
		sort_list(main_list,low,mid-1)
		sort_list(main_list,mid+1,high)

def partition(main_list,low,high): 
	
	pivot = main_list[low]
	i = low+1
	j = high

	while True:
		while i <= j and main_list[i] <= pivot:
			i += 1
		while i <= j and main_list[j] > pivot:
			j -= 1
		if i < j:
			swap(main_list, i, j)
		else:
			break

	swap(main_list, low, j)

	return j

def swap(main_list,num1,num2):

	temp_num = main_list[num1]
	main_list[num1] = main_list[num2]
	main_list[num2] = temp_num

Quick_sort()
print(main_list)