"""
File: Spring 2017 Midterm Practice
Name: Ethan Ton
"""

"""
Question 1.

Expression: 1 + (4 and 6) + (5 or 0) + (0 and 8)
Output:
12

Expression: 
f = lambda x: x
g = lambda y: f(g)
g(2)(2)
Output:
Function

Expression: 0 and print(2)
Output:
0

Expression: range(1, 20)[-2]
Output:
18

Expression: w([1, 2, 3, 1, 8, 2])
Output:
[3, 1, 8, 2]

Expression: 
f = lambda x: lambda y: / lambda z: x+y+z
reduce(lambda g, x: g(x), [1, 2, 3], f)
Output:
6

"""

"""
Question 2.
Global Frame:
    h       = func h(y)
    g       = func g(f)
    
f1: h
parent: Global
    y       = func lambda()
    return value = 3
    
f2: g
parent: Global
    f       = func lambda()
    return value = 3
    
f3: func lambda line 2
parent: f1

f4: func lambda line 5
parent: Global
    return value = 3
"""

#Question 2b.
def a():
    def g():
        return 3
    return k(g)

def k(b):
    return b()
z = a()

#Question 3.
def make_checker(relation, start, end):
    def checker(f):
        for k in range(start + 1, end):
            if not relation(f(k-1), f(k)):
                return False
        return True
    return checker

"""
Question 4.
The approximate positions of planets (in AU). this is known as Bode's Law.
"""

#Question 5.
def link_insert(lnklst, value, before):
    if isempty(lnklst):
        return lnklst
    elif first(lnklst) == before:
        return link(value, lnklst)
    else:
        return link(first(lnklst), link_insert(rest(lnklst), value, before))
    
#Question 6
def up_suffix(L):
    def longest_suffix_start(L):
        k = len(L) - 1
        while(k > 0 and L[k-1] <= L[k]):
            k -= 1
        return max(k, 0)
    return L[longest_suffix_start(L):]

#Question 7.
def correspond(A< B, M):
    N = len(A)
    def can_correspond(sa, sb, M):
        if M <= 0:
            return False
        else:
            for i in range(N):
                ta = sa + A[i]
                tb = sb + B[i]
                if ta == tb:
                    return True
                elif can_correspond(ta, tb, M - 1):
                    return True
            return False
    return can_correspond("", "", M)