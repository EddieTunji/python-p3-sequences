my_list = [1, 2, 3, 4]
print(my_list[2])

s = [4, 6, 9, 3, 5, 1, 2]
1 in s

s + s

s * 2

s[1]

s[5]

s[-3]

s[2:5]

s[2:8:2]

s[-4:]

s[-1], s[-2]

s[-1, -2]

my_list = [3, 6, 4, 2, 1, 5]
my_list.sort()
print(my_list)

my_list = ["Cabbage", "Apple", "Banana", "Potato"]
my_list.sort()
print(my_list)
my_list.sort(key = len)
print(my_list)
my_list.sort(key = len, reverse=True)
print(my_list)

my_list = [('John', 2), ('Steve', 1), ('Joe', 3)]

def sort_tuple(tuple_value):

    return tuple_value[1]

my_list.sort(key = sort_tuple)
print(my_list)

my_list = [3, 6, 4, 2, 1, 5]
sorted_list = sorted(my_list)
print(my_list)
print(sorted_list)

my_list = [0, 1, 2, 3]
my_list[0] = None
print(my_list)
my_list[3] = Some

my_list = [0, 1, 2, 3]
my_list.append(4)
print(my_list)

my_list = ['a', 'b', 'c', 'd', 'f']
my_list.insert(4, "e")
print(my_list)

my_list.insert(1000, "g")
print(my_list)
del(my_list[2])
print(my_list)
del(my_list[1:3])
print(my_list)

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
my_list.pop()
print(my_list)
my_list.remove('f')
print(my_list)
my_list.clear()
print(my_list)

for n in range(5):
    print(n)

my_range = range(4)
print(my_range)

my_range = range(2, 10, 2)
print(my_range)