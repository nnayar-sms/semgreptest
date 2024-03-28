def dirty_fn(m):
    return m  # but m is now dirty

user_input = 666
xx = dirty_fn(user_input)

