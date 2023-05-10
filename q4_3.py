def add_points(P, Q, p, a):
    """
    Add two points P and Q on the elliptic curve y^2 = x^3 + ax + b mod p.
    Returns the sum R = P + Q.
    """
    if P == Q:
        # Point doubling
        lam = (3 * P[0]**2 + a) * pow(2 * P[1], -1, p) % p
    else:
        # Point addition
        lam = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, p) % p

    x = (lam**2 - P[0] - Q[0]) % p
    y = (lam * (P[0] - x) - P[1]) % p
    return (x, y)

def reduce_point(P, p, order):
    """
    Reduce a point P to its unique representative in the range 0 <= x, y < p and
    return the same point if it is in the range, or its negation if it is not.
    """
    x, y = P
    x %= p
    y %= p
    if y >= order:
        return (x, p - y)
    else:
        return (x, y)

# Define the elliptic curve parameters
p = 17
a = 2
b = 2

# Define the point P and Q
P = (5, 1)
Q = (16, 4)

# Compute the order of the elliptic curve
order = 19  # The order can be computed using Schoof's algorithm

# Brute force search for the DLP
k = 0
R = P
while R != Q:
    k += 1
    R = add_points(R, P, p, a)
    R = reduce_point(R, p, order)

print("The DLP is:", k)
