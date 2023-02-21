"""
File: Summer 2016 Midterm Practice
Name: Ethan Ton
"""

"""
Question 1.

Expression:print(4, 5) + 1
Output:
4 5
Error

Expression: gold [ -2]
Output:
0

Expression: win(gold)
Output:
Eat vegetables.
1

Expression: riooo = go(get,gold)
Output:
Steps to success:

Expression:use = riooo(0)
Output:
Don't cheat!
Eat vegetables.
Don't cheat!
Eat vegetables.

Expression: usa
Output:
[0, 1, 1, 2]

1b.
[0, 1, 1, 2, 3, 5]

"""

"""
Question 2.
Global
    person      = func person(name, age)
    name        = func name(guy)
    age         = age(gal)
    my_name     = 'Marv'
    my_age      = 21
    marv        = func brain(ask)
    dan         = func brain(ask)
    
f1: person
parent: Global
    name        = 'Marv'
    age         = 21
    brain       = func brain(ask)
    return value = func brain(ask)
    
f2: age
parent: Global
    gal         = func brain(ask)
    return value = 21
    
f3: brain
parent: f1
    ask         = 'age'
    return value = 21
    
f4: person
parent: Global
    name        = 'Dan'
    age         = 28
    brain       = func brain(ask)
    return value = func brain(ask)
"""

"""
Question 3.
    Expression: len(lst)
    
    Expression: [[11 - x, 11 - y] for x, y in lst]
    
    Expression: [2 * x for x in lst[0]]
"""

#Question 4.
def is_sorted(n):
    if(n < 10):
        return True
    elif n % 10 > (n // 10) % 10:
        return False
    else:
        return is_sorted(n // 10)
    
#Question 5.
def aggregate(fn, seq, pred):
    result = None
    for elem in seq :
        if pred ( elem ):
            if result == None :
                result = elem
        else :
            result = fn ( result , elem )
    return result

#Question 5b.
#Expression: fact = lambda n: aggregate(mul, range(1, n+1), lambda x: True)
#Expression: if n > 0 else 1

#Question 6
def linked_sum(lnk, total):
    if total == 0:
        return 1
    elif lnk == empty or total < 0:
        return 0
    else:
        with_first = linked_sum(lnk, total - firwst(lnk))
        without_first = linked_sum(rest(lnk), total)
        return with_first + without_first
    
#Question 7
def track_lineage(family_tree, name):
    def tracker(t, p, gp):
        if name == entry(t):
            return [p, gp]
        for c in children(t):
            res = tracker(c, entry(t), p)
            if res:
                return res
    return tracker(family_tree, None, None)

#Question 7b.
def are_cousins(family_tree, name1, name2):
    p1, gp1 = track_lineage(family_tree, name1)
    p2, gp2 = track_lineage(family_tree, name2)
    return p1 != p2 and gp1 is not None and gp1 == gp2
