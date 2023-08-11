my_file = open("test_input.txt", "r")
data = my_file.read()
datalist = data.split("\n")
list1 = [int(x) for x in datalist]
list1.sort()
print(list1)
my_file.close()
