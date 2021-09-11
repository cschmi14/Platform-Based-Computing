# Carter Schmidt
# Cite any sources you used to help with the homework including TAs and classmates

import math

def string3(str):
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
    The string length will be at least 2.
    """
    end_chars = str[len(str) - 2: len(str)]
    output = ""
    for x in range(3):
        output += end_chars
    return output

def has123(nums):
    """
    Given an list of ints, return True if the sequence of numbers
    1, 2, 3 appears in the list somewhere.
    """
    for i in range(len(nums) - 2):
        if nums[i] == 1:
            if nums[i + 1] == 2:
                if nums[i + 2] == 3:
                    return True
    return False

 #string 2 count_code
def hascode(str):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except we'll accept any letter for the 'd', so "cope" and "cooe" count.
    """
    count = 0
    for i in range(len(str) - 3):
        if str[i] == 'c':
            if str[i + 1] == 'o':
                if str[i + 3] == 'e':
                    count += 1
    return count

def samecatdog(str):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
   *** This can be simplfied using a Python API function ***
    """
    count_cat = 0
    for i in range(len(str) - 2):
        if str[i] == 'c':
            if str[i + 1] == 'a':
                if str[i + 2] == 't':
                    count_cat += 1
    count_dog = 0
    for i in range(len(str) - 2):
        if str[i] == 'd':
            if str[i + 1] == 'o':
                if str[i + 2] == 'g':
                    count_dog += 1
    return count_cat == count_dog


def centered_avg(nums):
    """
    Return the "centered" average of a list of ints, which we'll say is the mean average of the
    values, except ignoring the largest and smallest values in the list. If there are
    multiple copies of the smallest value, ignore just one copy, and likewise for the largest value.
    Use floor division to produce the final average. You may assume that the list is length 3 or more.
    """
    avg = 0
    for x in nums[1:len(nums) - 1]:
        avg += x
    return avg // (len(nums) - 2)

#Test functions
assert string3("Hello") == 'lololo', 'string3(Hello) expected lololo'
print("correct")
assert string3("ab") == 'ababab', 'string3(ab) expected ababab'
print("correct")
assert string3("Hi") == 'HiHiHi', 'string3(Hi) expected HiHiHi'
print("correct")

assert has123([1, 1, 2, 3, 1]) == True, '[1, 1, 2, 3, 1] has 123'
print("correct")
assert has123([1, 1, 2, 4, 1]) == False, '[1, 1, 2, 3, 1] does not have 123'
print("correct")
assert has123([1, 1, 2, 1, 2, 3]) == True, '[1, 1, 2, 1, 2, 3] has 123'
print("correct")

assert hascode("aaacodebbb") == 1, 'aaacodebbb has code'
print("correct")
assert hascode("aaacodebbb") == 1, 'codexxcode has code'
print("correct")
assert hascode("cozexxcope") == 2, 'cozexxcope has code'
print("correct")

assert samecatdog("catdog") == True, 'catdog appear same number of times'
print("correct")
assert samecatdog("catcat") == False, 'catcat does not appear same number of times'
print("correct")
assert samecatdog("1cat1cadodog") == True, '1cat1cadodog appear the same number of times'
print("correct")

assert centered_avg([1, 2, 3, 4, 100]) == 3, 'average [1, 2, 3, 4, 100] is 3'
print("correct")
assert centered_avg([1, 1, 5, 5, 10, 8, 7]) == 5, 'average [1, 1, 5, 5, 10, 8, 7] is 5'
print("correct")
assert centered_avg([-10, -4, -2, -4, -2, 0]) == -3, 'average [-10, -4, -2, -4, -2, 0] is -3'
print("correct")

#Problems found on https://codingbat.com/python