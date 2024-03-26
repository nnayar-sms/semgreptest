import black
from test3 import xx

user_input = 666

def bad(user_input):
    x = user_input
    y = evil(x)
    # ruleid: taint-labels
    sink(y)


x = user_input

def bad(user_input):
    # ok: taint-labels (no evil!)
    sink(xx)

blackit()
