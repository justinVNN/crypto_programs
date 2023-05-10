x_1 = 3
y_1 = 1
x_2 = 2
y_2 = 0

a = -4

mod = 7

if x_1 == x_2 and y_1 == y_2:
    s_T = (3 * (x_1 ** 2) + a) % mod
    s_B = (2 * y_1) % mod
    s_B = pow(s_B, -1, mod)

    s = s_T * s_B % mod

else:
    s_T = (y_2 - y_1) % mod
    s_B = (x_2 - x_1) % mod
    s_B = pow(s_B, -1, mod)

    s = s_T * s_B % mod


x_3 = ((s ** 2) - x_1 - x_2) % mod
y_3 = (s * (x_1 - x_3) - y_1) % mod

print((x_3,y_3))
