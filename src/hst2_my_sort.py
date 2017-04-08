
def my_sort(list):
	output = sorted(list, key=lambda x: (x % 2 == 0, x))
	print(output)

my_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])