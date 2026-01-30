def f(x):
    """Subtracts one from an integer x. """
    return x - 1

def g(x):
    """Adds one and then doubles an integer x. """
    return 2 * (x + 1)
    
def h(x, y):
    """Concatenates the digits of two different positive integers x and y. """
    len_y = 1
    z = y
    while z // 10 != 0:
        len_y += 1
        z //= 10
    return x * 10 ** len_y + y

"""The shortest small expression I can find that evaluates to 2025 (9 calls)"""
twenty_twenty_five = h(g(f(f(f(g(5))))), f(g(g(5))))
print(twenty_twenty_five)