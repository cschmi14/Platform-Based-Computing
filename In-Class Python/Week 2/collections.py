list1 = [1, 2, 3, 4, 5]
repetition = [0] * 10
print(repetition)
list1_copy = list1[:]
list1_copy = list(list1)
list1_copy = list1.copy()

# Slicing

mid_list = list1[1:4]
print(mid_list)
remove_first_two = list1[2:]
print(remove_first_two)
remove_last_two = list1[:-2]
print(remove_last_two)
last_two = list1[-2:]
print(last_two)
two_three = list1[1:3]
print(two_three)

list2 = [10, 20, 30]
list3 = [100, 200, 300]
list1.extend(list2)
print(list1)
list2.append(list3)
print(list2)

print(list1.index(20))
list1.append(20)
print(list1.count(20))
print('hijoehijoehijoe'.count('joe'))

if 1000 in list1:
    list1.index(1000)
else:
    print('1000 not in list')

list_evens = []
for i in range(2, 13):
    if i % 2 == 0:
        list_evens.append(i)
print(list_evens)

list_evens2 = [x for x in range(2, 13, 2)]
print(list_evens2)

list_fifty = [x for x in range(51)]
print(list_fifty)
quiz
print(odd_list)

table = [[i + 1] * 5 for i in range(10)]
print(table)
for i in range(10):
    for j in range(5):
        table[i][j] = i + 1
        print(table[i][j], end=" ")
    print()
print(table)

dup_list = [1, 2, 3, 4, 5]
dup_list.extend(dup_list)
print(dup_list)
my_set = set(dup_list)
print(my_set)
