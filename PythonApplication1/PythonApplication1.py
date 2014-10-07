def factor(x):
	if x > 1:
		return x * factor(x - 1)
	else:
		return 1


def bubble(arr):
	swaps = 1
	iteration = 0
	upper = len(arr) - 1
	print("Iteration:", iteration, "array:", arr)
	while swaps > 0:
		swaps = 0
		for i in range(0, upper):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
				swaps += 1
			else:
				continue
		iteration += 1
		upper -= 1
		print("Iteration:", iteration, "array:", arr)
	return arr

from pymongo import MongoClient

client = MongoClient('mongodb://192.168.169.16')
db = client.mytest
collection = db.testdata
print("Find items:", collection.count())
for item in collection.find():
	print(item)

a, b = 0, 1
print(a, b)
a, b = b, a
print(a, b)
print("Factor of:", 5, "is:", factor(5))

array = [1, 5, 4, 2, 3]
print(array, " -> ", bubble(array))

str1 = "Hello world"
print(str1)
print(str1[2:5])