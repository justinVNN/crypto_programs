# Define the point addition operation
def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and (y1 + y2) % 17 == 0:
        return None
    if x1 == x2:
        m = (3*x1**2 + 2) * pow(2*y1, -1, 17) % 17
    else:
        m = (y2 - y1) * pow(x2 - x1, -1, 17) % 17
    x3 = (m**2 - x1 - x2) % 17
    y3 = (m*(x1 - x3) - y1) % 17
    return (x3, y3)

# Define the point multiplication operation
def mul(k, P):
    Q = None
    while k > 0:
        if k % 2 == 1:
            Q = add(Q, P)
        P = add(P, P)
        k //= 2
    return Q

# Solve the DLP using brute force
P = (5, 1)
Q = (16, 4)
kP = P
x = 1
while kP != Q:
    x += 1
    kP = add(kP, P)
print(f"The solution is x = {x}")
