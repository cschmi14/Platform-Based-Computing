def average(list):
    avg = 0
    for x in list:
        avg += x
    return (avg / len(list))

list1 = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10]
print(average(list1))

def find_minimum(list):
    min = list[0]
    for x in list:
        if x < min:
            min = x
    return min

print(find_minimum(list1))

def find_maximum(list):
    max = list[0]
    for x in list:
        if x > max:
            max = x
    return max

print(find_maximum(list1))

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

a = 1
b = 2
a, b = swap(a, b)
print(a, b)