"""
File: Summer 2018 Midterm Practice
Name: Ethan Ton
"""

"""
Question 1.

Expression: incredible / dash
Output: 
5.25

Expression: el(mr, 4, 0)
Output:
stretch
21

Expression: sam = fro(zen)
Output:
14

sam = where(is_my)
Expression: edna(sam, 7)
Output:
supersuit
11

Expression: vi(dash, incredible)
Output:
hidden 
3
"""

"""
Question 2.
Global Frame:
    pet     = "dog"
    bug     = 3
    to      = func to(do)
    walk    = func walk(time)
    
f1: walk(lambda: (to(pet) or not 2 * pet))
parent: Global
    pet     = "cat"
    bed     = function line 8
    return (lambda: "itch" )()

f2: time() = to("dog")
parent: f1
    bug     = 5
    do      = 'dog'
    return lambda bye: bye - bug

f3: func line 8
parent: f3
    bye     = 3
    bug     = 5
    return -2
    
f4: func line 16
parent: f1
    return 'itch'
"""

"""
Question 3.
a -> 1, 2, 3
b-> 4, 5, 6

3b.
c -> 1, 2, 3
d -> 4, 1, 2, 3, 6, 7, 6, 7
e -> 1, 2, 3, 6, 7

3c.
f -> 1, 2, 3, 3, 3
g -> 2, 3, 3, 3, 2, 3, 3, 3
h -> 1, 2, 3, 3, 3
"""

"""
Question 4. 
a1. Return a function
a2. Take in a function as input

b2. When you violate abstraction barriers, changing the implementation is no
    no longer possible
    
c. List are mutable; tuples are immutable
"""

#Question 5
def repeat_digits(n):
    last, rest = n % 10, n // 10
    if rest == 0:
        return last * 11 
    return repeat_digits(rest) * 100 + last * 11

"""
5b.
Theta(d)
"""

#Question 6
def eight_path(t):
    def helper(t, path_so_far):
        path_so_far = path_so_far + [label(t)]
        if is_leaf(t) and sum(path_so_far) % 8 == 0:
            return path_so_far
        for b in branches(t):
            result = helper(b, path_so_far)
            if result:
                return result
    return helper(t, [])

#Question 7
def sabacc_winnder(cards, player0, player1):
    if cards == 0:
        return player0
    if cards == 1:
        return player1
    take_one = sabacc_winnder(cards - 1, player1, player0)
    take_two = sabacc_winnder(cards - 2, player1, player0)
    if take_one == player0 or take_two == player0:
        return player0
    return player1

#Question 8
def thanos_messenger(word):
    assert word != '.', 'No words provided!'
    def make_new_messenger(message, skip_next):
        def new_messenger(word):
            if word == '.':
                return message + '.'
            if skip_next:
                return make_new_messenger(message, False)
            return make_new_messenger(message + " " + word, True)
        return new_messenger
    return make_new_messenger(word, True)