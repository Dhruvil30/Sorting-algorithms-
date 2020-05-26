#Selection sort

main_list = []

def Selection_sort():

	global main_list

	list_size = int(input("Enter the size of list : "))

	print("Enter the numbers in list")

	for num in range(0,list_size):
		list_value = int(input())
		main_list.append(list_value)

	sort_list(main_list)

def sort_list(main_list):

	min_value,positon,swap_value = 0

	for i in range (0,len(main_list)):
		min_value = main_list[i]
		for j in range (i+1, len(main_list)):
			if main_list[j] < min_value:
				min_value = main_list[j]
				positon = j
		swap_value = main_list[i]
		main_list[i] = min_value
		main_list[positon] = swap_value

	print("Sorted list : " + str(main_list))

Selection_sort()