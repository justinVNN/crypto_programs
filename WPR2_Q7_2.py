# Define the elliptic curve and base point
p = 7
a = 0
b = -4
alpha = (1, 2)

# Define Alice's secret key
y = 3

# Bob sends his public key
x = 5
x_alpha = (3, 1)

# Define point addition and scalar multiplication functions
def add_points(p, q):
    if p is None:
        return q
    if q is None:
        return p
    if p[0] == q[0] and p[1] != q[1]:
        return None
    if p == q:
        m = (3 * p[0]**2 + a) * pow(2 * p[1], -1, p)
    else:
        m = (q[1] - p[1]) * pow(q[0] - p[0], -1, p)
    x = (m**2 - p[0] - q[0]) % p
    y = (m * (p[0] - x) - p[1]) % p
    return (x, y)

def scalar_multiply(k, p):
    if k % p == 0 or p is None:
        return None
    if k < 0:
        return scalar_multiply(-k, add_points(None, p))
    q = None
    for i in range(k.bit_length()):
        q = add_points(q, q)
        if (k >> i) & 1:
            q = add_points(q, p)
    return q

# Calculate Alice's public key
y_alpha = scalar_multiply(y, alpha)

# Calculate the shared key
shared_key = scalar_multiply(x, y_alpha)

print("Alice's public key:", y_alpha)
print("Shared key:", shared_key)
