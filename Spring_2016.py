"""
File: Spring 2016 Midterm Practice
Name: Ethan Ton
"""

"""
Question 1.

Expression:(3 and abs)(-1)
Output:
1

Expression: print(3) or 1/0
Output:
3
Error

Expression: print
Output:
Function

Expression: ([1, 2, 3] if y // (y+1) else [4, 5]) [1]
Output:
5

Expression: w(5)
Output:
3
"""

"""
Question 1b.
Expression: print(d([1, 2, 3]), d([0, 1, 2, 1, 0]))
Output:
False True
"""

"""
Question 2.
Global Frame
    y       = 3
    out     = func out(h, m)
    v       = 5
    
f1: out
parent: Global
    h       = None
    m       = 1
    inner   = func inner()
    y       = 5
    return value = func inner()
    
f2: out 
parent: Global
    h       = func ininer()
    m       = 0
    inner   = func inner()
    y       = 0
    return value = func inner()
    
f3: inner
parent: f1
    return value = 5
"""

"""
Question 2b.

Global Frame
    lazy    = func lazy(n)
    v       = 5
    
f1: lazy
parent: Global
    n       = 4
    return value = lambda func line 2
    
f2: lambda line 2
parent: f1
    k       = 1
    return value = lambda func line 2
    
f3: lazy
parent: Global 
    n       = 5
    return value = lambda func line 2
    
f4: lambda line 2
parent: f3
    k       = 0
    return value = 5
"""

#Question 4.
def has_cycle(L, k):
    def cycle_at(s):
        p = L[s]
        n = 1
        while n < k:
            if p == s:
                return False
            p = L[p]
            n += 1
        return p == s
    for j in range(len(L)):
        if cycle_at(j):
            return True
    return False

#Question 5
def count_groupings(n):
    if n == 1:
        return 1
    total = 0
    i = 1
    while i < n:
        total += count_groupings(i) * count_groupings(n - i)
        i += 1
    return total

#Question 6
def pred_maze(x0, y0, open, exit):
    def maze(dir):
        x, y = (x0, y0 - 1) if dir == "south" else (x0 -1 , y0)
        if x <= exit:
            return "exit"
        elif open(x, y):
            return pred_maze(x, y, open, exit)
        else:
            return "dead end"
    return maze