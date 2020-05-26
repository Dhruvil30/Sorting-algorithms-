#Counting Sort

main_list = []

def Counting_sort():

	global main_list

	list_size = int(input("Enter the size of list : "))

	print("Enter the numbers in list")

	for num in range(0,list_size):
		list_value = int(input())
		main_list.append(list_value)

	sort_list(main_list)

def sort_list(main_list):

	max_val = max(main_list)
	count_list = [0] * max_val

	for num in main_list:
		count_list[num-1] += 1

	sorted_list = []

	for i in range(0, len(count_list)):
		while count_list[i] != 0:
			sorted_list.append(i+1)
			count_list[i] -= 1
	
	print("Sorted list : " + str(sorted_list))

Counting_sort()