import black
from test3 import dirty_fn, xx

user_input = 666

def bad1(user_input):
    x = user_input
    y = dirty_fn(x)
    # ruleid: taint-labels
    print(y)


x = user_input

def bad2(user_input):
    # ok: taint-labels (no evil!)
    print(xx)

#blackit()

bad1(777)
bad2("ignored")
