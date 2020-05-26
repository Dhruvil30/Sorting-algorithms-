#Bubble Sort

main_list = []

def Bubble_sort():

	global main_list

	list_size = int(input("Enter the size of list : "))

	print("Enter the numbers in list")

	for num in range(0,list_size):
		list_value = int(input())
		main_list.append(list_value)

	sort_list(main_list)

def sort_list(main_list):

	swap_value = 0

	for i in range(0, len(main_list)):
		for j in range(i+1, len(main_list)):
			if main_list[i] > main_list[j]:
				swap_value = main_list[i]
				main_list[i] = main_list[j]
				main_list[j] = swap_value

	print("Sorted list : " + str(main_list))

Bubble_sort()