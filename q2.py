def calculate_encryption_exponent(d, p, q, n):
    phi = (p-1) * (q-1)
    e = pow(d, -1, phi)
    return e

def rsa_encrypt(m, e, n):
    c = pow(m, e, n)
    return c

e_e = calculate_encryption_exponent(11787, 137, 131, 17947)
print("e:", e_e)
c = rsa_encrypt(513, e_e, 17947)
print("c:", c)