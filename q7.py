def elliptic_curve_addition(x1, y1, x2, y2, p):
    if x1 == x2 and y1 == -y2 % p:
        return None, None

    if (x1, y1) == (x2, y2):
        slope_num = (3 * x1 ** 2 - 4)
        slope_denom = (2 * y1)
    else:
        slope_num = (y2 - y1)
        slope_denom = (x2 - x1)
    inverse_denom = pow(slope_denom, -1, p)
    slope = slope_num * inverse_denom % p

    x3 = (slope ** 2 - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p 

    return x3, y3

def scalar_mult(point, scalar, p):
    new_point = point
    for _ in range(scalar - 1):
        new_point = elliptic_curve_addition(new_point[0], new_point[1], point[0], point[1], p)
    return new_point

def main():
    E_p = 7  # Curve parameter p
    alpha = (1, 2)  # Public chosen point 

    alice_secret_key = 3
    bob_pub_key = (3, 1) 

    result = scalar_mult(bob_pub_key, alice_secret_key, E_p)

    print("Shared key:", result)

if __name__ == "__main__":
    main()