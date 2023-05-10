
def montgomery_multiply_1(a, b, n, r):
    # Calculate the value of R^2 mod n
    r_squared = (r * r) % n
    
    # Calculate the value of T = a * b * R^-1 mod n
    t = (a * b * pow(r, -1, n)) % n
    
    # Calculate the value of U = (T + (T * R^-1 mod R) * n) // R
    u = (t + ((t * pow(r, -1, r_squared)) % r_squared * n)) // r
    
    # If U >= n, subtract n to get the correct result
    if u >= n:
        return u - n
    else:
        return u
    
print(montgomery_multiply_1(16,26,83,37))


def montgomery_multiply_2(a, b, n, r):
    # Step 1: Compute the parameter R = r^n mod n
    R = pow(r, n, n)

    # Step 2: Compute the Montgomery representations of a and b
    a_bar = (a * R) % n
    b_bar = (b * R) % n

    # Step 3: Compute the product c_bar = a_bar * b_bar
    c_bar = (a_bar * b_bar) % n

    # Step 4: Compute the inverse of R modulo n using the GCD method
    def extended_gcd(a, b):
        if b == 0:
            return (a, 1, 0)
        else:
            d, x, y = extended_gcd(b, a % b)
            return (d, y, x - (a // b) * y)

    _, inv_r, _ = extended_gcd(r, n)
    inv_r %= n

    # Step 5: Compute the product c = c_bar * R^-1 mod n
    c = (c_bar * inv_r) % n

    # Step 6: If c >= n, subtract n to obtain the result
    if c >= n:
        c -= n

    return c

print(montgomery_multiply_2(17,26,83,100))





