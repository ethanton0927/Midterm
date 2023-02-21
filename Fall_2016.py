"""
File: Fall 2016 Midterm Practice
Name: Ethan Ton
"""

"""
Question 1.

Expression: equals(3==4, equals(5, equals(5,5))))
Output:
True

Expression: print(print(print(2)), print(3))
Output:
2
None
3
None None

Expression: print(nemo(print(5))())
Output:
5
None
None

Expression: if_function(nemo(3), dory, 2)
Output:
3
fish

Expression: if_function(dory, nemo(2), ray()
Output:
1
5
2
"""

"""
Question 2.
Glbal Frame
    splash      = func splash(klay, curry)
    steph       = func lambda(klay)
    curry 30
    
f1: splash
parent: Global
    klay        = func lambda(Klay)
    curry       = 5
    steph       = func labmda(klay)
    return      = func lambda(klay)
    
f2: lambda
parent: f1
    klay        = 4
    return      = 3
    
f3: lambda
parent: Global
    klay        = 6
    return      = 3
    
f4: splash
parent: Global
    klay        = 11
    curry       = 30
    return value = 6

"""

#Question 3
def counter(d):
    def count(n):
        k = 0
        while n > 0:
            n, last = n // 10, n % 10
            if last == d:
                k += 1
        return k
    return count

#3b.
def significant(n, k):
    if n < pow(10, k):
        return n
    return significant(n // 10, k)

#Question 4.
def repeat_sum(f, x, n):
    total, k = 0, 0
    while k<= n:
        total = total + x
        x = f(x)
        k = k + 1
    return total

#4b.
def sum_squares(n):
    f = lambda x: pow(round(pow(x, 0.5) + 1), 2)
    return repeat_sum(f, 0, n)

#Question 5.
def multiadder(n):
    assert n > 0
    if n == 1:
        return lambda x: x
    else:
        return lambda a: lambda b: multiadder(n-1)(a+b)
    
#Question 5b.
compose1(multiadder(4)(1000), multiadder(3)(10)(1000)(1)(2)(3))