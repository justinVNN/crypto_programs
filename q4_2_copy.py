import math

# Define the group G and the primitive element alpha
G = range(0, 11)
alpha = 2

# Define the element beta whose DLP is to be solved
beta = 3

# Compute the order of the group
n = len(G)

# Choose a block size for the algorithm
m = 4

# Compute the baby-step table
baby_steps = [(i, pow(alpha, i, n)) for i in range(0, m)]

# Compute the giant-step table
giant_steps = [(j, (beta * pow(alpha, -j * m, n)) % n) for j in range(0, math.ceil(n / m))]

# Look for a match between the baby-step and giant-step tables
for i, a in baby_steps:
    for j, b in giant_steps:
        if a == b:
            # Match found, so compute the solution to the DLP
            x = i + j * m
            print("Solution found: alpha^{} = {} ≡ {} = beta (mod {})".format(x, pow(alpha, x, n), beta, n))
            break
    else:
        continue
    break
else:
    # No match found
    print("No solution found.")
