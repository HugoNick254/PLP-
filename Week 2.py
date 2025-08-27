# Creating an empty list and appending things to it

my_list = []
items = (10, 20, 30)

for item in items:
    my_list.append (item)

print(my_list)

my_list.insert(1, 15)

print(my_list)

list2 = [50, 60,70]

my_list = my_list + list2

print(my_list)


my_list.pop(-1)

print(my_list)

my_list.sort()

print(my_list)

print(f"The index of the value 30 is {my_list.index(30)}")