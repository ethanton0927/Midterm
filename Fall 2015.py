"""
File: Fall 2015 Midterm Practice
Name: Ethan Ton
"""

"""
Question 1.

Expression: print(None, print(None))
Output:
None
None None

Expression: jazz(5)
Output:
11

Expression: (lambda out: jazz(8))(9)
Output:
12

Expression: twist(2, lambda x: x-20(4)
Output: 
2 7 
0 4

Expression: twist(5, print)(out)
Output:
5
5 7 
None 3

Expression: twist(6, lambda hands: hands-out, 2)(-1)
Output:
6 2
3 NOne
0 -1
"""

"""
Question 2.
Global Frame
    the     = func the(donald)
    clin    = func clin(ton)
    donald  = 2
    duck    = 5

f1: clin
parent: Global
    ton     = func ton(ga)
    the     = func the(race)
    return value = func ton(ga)

f2: ton
parent: f1
    ga      = 8
    donald  = 7
    return value = 5
    
f3: the
parent: f1
    race    = 4
    return value = 8
"""

#Question 3
def find_digit(n, d):
    i, k = 0, False
    while n:
        n, last = n // 10, n % 10
        if last == d:
            k = i
        i = i + 1
    return k

#Question 3b. 
f = lambda x: find_digit(234567, x)
compose1(f, f)(y) == y

#Question 4.
def luhn_sum(n):
    def luhn_digit(digit):
        x = digit * multiplier
        return (x // 10) + x % 10
    total, multiplier = 0, 1
    while n:
        n, last = n // 10, n % 10
        total = total + luhn_digit(last)
        multiplier = 3 - multiplier
    return total

#Question 5.
return 10 * n  + luhn_sum(10 * n) % 10

#Question 6.
def decompose1(f, h):
    def g(x):
        if h(x) == f(y):
            return y
        else:
            return r(y+1)
        return r(0)
    return g

#Question 7.
decompose1(e, compose1(square, e))(3) + 2000