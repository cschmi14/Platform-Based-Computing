first_name = "Carter"
last_name = "Schmidt"
full_name = first_name + last_name
repeat = first_name * 5
print(repeat)

last_character = first_name[-1]
print(last_character)
first_two_characters = first_name[:2]
print(first_two_characters)

if 'C' in first_name:
    print("'C' in first name")

for c in first_name:
    if c == 'C':
        print("'C' in first name")
        break

for i in range(0, len(first_name)):
    if first_name[i] == 'r':
        print("'r' in first name at index", i)
        break

name2 = "Carter"
if first_name == name2:
    print("strings are same")

upper = first_name.upper()
print(upper)
print(first_name)

list1 = [1, 2, 3, 4, 5]
list2 = []
list2.append(10)
list2.append(20)
list2.append(30)
list2.append(40)
list2.append(50)

print(list1)
print(list2)
list1.remove(2)
print(list1)
list2.pop()
print(list2)
list1 += list2
list3 = []
list3 += [10, 20, 30, 40, 50]
list3 += list1
print(list3)

total = 0
for x in list2:
    total += x
print(total)
total = 0
for i in range(0, len(list2)):
    total += list3[i]
print(total)

def hello(name, greeting = "Hello"):
    print(greeting, name)

hello("Carter")
hello("Carter", "What's up")

def return_two():
    return 10, 20

x, y = return_two()
print(x, y)



