import hashlib

# Define the Elliptic Curve
p = 7 #modulus we are working with
a = 0 #coefficient of x^2
b = -4 #coefficient of x

# Base Point G
G = (1, 2)

# Order of the base point
n = 8

# Alice's private key
y = 3

# Bob's public key
xa = (3, 1)

# Calculate Alice's public key
Ya = lambda k: k*G
PA = Ya(y)

# Calculate the shared key
S = lambda k: k*xa
K = S(y)

# Hash the shared key using SHA-256
K_bytes = f"{K[0]},{K[1]}".encode('utf-8')
shared_key = hashlib.sha256(K_bytes).hexdigest()

print(f"Shared key: ({K[0]}, {K[1]})")
