"""
File: Summer 2017 Midterm Practice
Name: Ethan Ton
"""

"""
Question 1.

Expression: make_amoeboid('flora')
Output:
My name is flora
'flora'

Expression: print(parent(harry), print(harry))
Output:
harry (clone)
harry None

Expression: find_amoeba(lambda a: True, 'harry')
Output:
there you are, harry
There you are, harry (clone)
['harry', 'harry (clone)']

Expression: find_amoeba(lambda a: parent(a) == harry, 'harry')
Output:
[]

Expression: fine_amoeba(lamda a: make_amoeboid('gabby'), 'flora')
Output:
My name is gabby
There you are, flora
['flora']

Expression: find_amoeba(lambda a: parent(a) == 'flora', make_amoeboid('flora'))
Output:
I am but a clone
My name is flora (clone)
There you are, flora (clone)
['flora (clone)']

"""

"""
Question 2.
a.
a -> 1, 2, 3, None
b -> 1, 2, 3, None, None

b. 
a -> 1, 2, 3
b -> 1, 2, 3
c -> 1, 2, 3, 1, 2, 3
d -> 1, 2, 3

c. 
a -> 1, 2, 3
b -> 1, 2, 3, 2, 1, 2, 3, 2
c -> empty
"""

"""
Question 4.
Global Frame:
    x       = 1
    y       = 2
    r       = func r(f, g, y)
    record  = func record(default)
    
f1: record
parent: Global
    default = 1, 2, 1, 2, 3
    args    = 1, 2, 3
    wraps   = func wraps(f)
    return value = func wraps(f)
    
f2: wraps
parent: f1
    f       = func lambda(y)
    w       = func w(x)
    return value = func w(x)
    
f3: w
parent: f2
    x       = 3
    return value = 1

f4: lambda
parent: Global
    y       = 3
    return value = 1
    
f5: r
parent: Global
    f       = min
    g       = max
    y       = 3
    return value = 1
"""

"""
Question 4. 
a.
O(N)

b.
O(N^2)

c.
O(logN)

d.
O(N)
"""

#Question 5.
def replicate_links(s):
    def replicate(s, n):
        if(n > 0):
            return link(first(s), replicate(s, n - 1))
        elif is_empty(rest(s)):
            return empty
        return replicate(rest(s), first(rest(s)))
    return replicate(s, first(s))

#Question 6
def compress(lst):
    total = 0 
    result = []
    flag = False
    for element in lst:
        if(type(element) == int):
            total += element
            flag = True
        else:
            if flag:
                result += [total]
                total = 0
                flag = False
            result += [compress(element)]
    if flag:
        result += [total]
    return result

#Question 8
def list_counter(base, digits):
    total = 0
    for digit in digits:
        if digit < base:
            total *= base
            total += digit
    return total

#b.
def counter(base):
    def parse(digit, total=0):
        if digit == 'done':
            return total
        elif digit >= base:
            return lambda x: parse(x, total)
        else:
            return lambda x: parse(x, total * base + digit)
    return parse

#Question 9
def count_ways(t, total):
    def paths(t, total, can_skip):
        ways = 0
        if total == root(t):
            ways += 1
        ways += sum([paths(b, total - root(t), False) for b in branches(t)])
        if can_skip:
            ways += sum([paths(b, total, True) for b in branches(t)])
        return ways
    return paths(t, total, True)
