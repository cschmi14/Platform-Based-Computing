def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def bunny_ears(n):
    '''
    Count recursively the number of bunny ears that would be if we had
    n bunnies.
    n >= 1
    bunny_ears(3) = 6 bunny ears
    '''
    if n == 1:
        return 2
    else:
        return 2 + bunny_ears(n - 1)


def powern(base,power):
    """
    Given base and n that are both 0 or more, compute recursively (no loops) the value of
    base to the n power, so powerN(3, 2) is 9 (3 squared).
    """
    if power == 0:
        return 1
    else:
        return base * powern(base, power - 1)


def array6(array, start=0):
    """
    Given an array of ints, compute recursively if the array contains a 6.
    We'll use the convention of considering only the part of the array that begins at the
    given index. In this way, a recursive call can pass index+1 to move down the array.
    The initial call will pass in index as 0.
    """
    if array[start] == 6:
        return True
    if start == len(array) - 1:
        return False
    else:
        return array6(array, start + 1)


def countX(string, index=0):
    '''
    Given a string that we'll treat as an array of characters, compute recursively
    the number of times x that appear in the string.
    '''
    if index == len(string):
        return 0
    if string[index] == 'x':
        return 1 + countX(string, index + 1)
    else:
        return 0 + countX(string, index + 1)


def no_x(string, index=0):
    """
    Given a string, compute recursively a new string where all the 'x' chars have
    been removed.
    """
    pass
    # if index == len(string):
    #     return
    # if string[index] == 'x':
    #     return no_x(string, index + 1)
    # else:
    #     return string[index] + no_x(string, index + 1)


def count8(num):
    """
    Given a non-negative int n, compute recursively (no loops) the count of the occurrences
     of 8 as a digit, except that an 8 with another 8 immediately to its left counts double,
      so 8818 yields 4. Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
      while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
    """
    if num == 0:
        return 0
    else:
        if num % 10 == 8:
            return 1 + count8(num / 10)
        else:
            return 0 + count8(num / 10)



print("factorial 4 is",factorial(4))
print("bunny ears 3 is ", bunny_ears(3))
print("powern of 2 0 is",powern(2,0))
print("powern of 4 4 is",powern(4,4))
print("array6 [1,2,3,4,5,6]",array6([1,2,3,4,5,6]))
print("array6 [1,2,3,4,5]",array6([1,2,3,4,5]))
print("array6 [6]",array6([6]))
print("countX xxhixx is", countX("xxhixx"))
print("countX hi is", countX("hi"))
print("no_x xxhixx is", no_x("xxhixx"))
print("no_x hi is", no_x("hi"))
print("count8 8818878 is ",count8(8818878))
print("count8 81878 is ",count8(81878))
print("count8 17 is ",count8(17))