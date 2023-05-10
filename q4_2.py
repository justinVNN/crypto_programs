def discrete_log(a, b, n):
    """
    Brute-force method for solving the discrete logarithm problem.
    Finds an integer x such that a^x ≡ b (mod n).
    """
    x = 0
    while pow(a, x, n) != b:
        x += 1
    return x

a = 2
b = 3
n = 11

x = discrete_log(a, b, n)

print("the discrete log is: ", x)