#Insertion Sort

main_list = []

def Insertion_sort():

	global main_list

	list_size = int(input("Enter the size of list : "))

	print("Enter the numbers in list")

	for num in range(0,list_size):
		list_value = int(input())
		main_list.append(list_value)

	sort_list(main_list)

def sort_list(main_list):

	for i in range(0, len(main_list)):

		j = i-1
		temp = main_list[i]

		while j >=0 and temp < main_list[j]:
			main_list[j+1] = main_list[j]
			j = j-1

		main_list[j+1] = temp

	print("Sorted list : " + str(main_list))

Insertion_sort()