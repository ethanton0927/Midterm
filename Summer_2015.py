"""
File: Summer 2015 Midterm Practice
Name: Ethan Ton
"""

"""
Quetstion 1.

Expression: capt(vision)
Output: 
6
7

Expression: print(print(1), vision(2))
Output:
1
2
None 3

Expression: hawkeye(hammer, 3)
Output:
Error

Expression: hawkeye(capt, 3)
Output:
0

Expression: hammer(lambda ultron: ultron, -1)
Output:
0

Expression: hammer(vision, avengers)
Output:
6
6
-6
"""

"""
Question 2

Global Frame
    joy     = func joy(a, b)
    sadness = func sadness(a, b)
    x       = 1
    y       = 2
    
f1: joy
parent: Global
    a       = 1
    b       = 2
    x       = 42
    y       = 4
    return value = 38
    
f2: sadness
parent: Global
    a       = 4
    b       = 1
    return value = 4
"""

#Question 3
def make_direction(secret):
    def direction(guess):
        if secret > guess:
            return 1
        elif secret < guess:
            return -1
        else:
            return 0
    return direction

#Question 4
def naive_search(low, high, direction):
    guess, count = (low + high) // 2, 1
    print(gues)
    sign = direction(guess)
    while sign != 0:
        guess += sign
        count += 1
        sign = direction(guess)
        print(guess)
    return count

#Question 5.
O(n)

#Question 6.
def binary_search(low, high, direction):
    guess = (low + high) // 2
    print(guess)
    sign = direction(guess)
    if sign == 0:
        return 1
    elif sign < 0:
        return 1 + binary_search(low, guess, direction)
    else:
        return 1 + binary_search(guess, high, direction)
    
#Question 7
O(log n)

#Question 8. 
def subset_sum(target, lst):
    if target == 0:
        return True
    elif not lst:
        return False
    else:
        a = subset_sum(target - lst[0], lst[1:])
        b = subset_sum(target, lst[1:])
        return a or b
    
#Question 9.
def intersection(lst_of_lsts):
    elements = []
    for elem in lst_of_lsts[0]:
        condition = True
        for lst in lst_of_lsts[1:]:
            if elem not in lst:
                condition = False
        if condition:
            elements = elements + [elem]
    return elements

#Question 10.
def snadwhich(n):
    a, b = (n // 10) % 10, n % 10
    n = n // 100
    while n > 0:
        if n % 10 == b:
            return True
        else:
            a, b = n % 10, a
            n = n // 10
    return False