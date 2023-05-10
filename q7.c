#include <stdio.h>

// Point structure
typedef struct {
    int x;
    int y;
} Point;

// Elliptic curve parameters
const int p = 7;  // modulo
const int a = 0;  // coefficient of x^2
const int b = -4; // coefficient of x

// Extended Euclidean algorithm
int extended_euclid(int a, int b, int *x, int *y) {
    if (a == 0) {
        *x = 0;
        *y = 1;
        return b;
    }
    int x1, y1;
    int gcd = extended_euclid(b % a, a, &x1, &y1);
    *x = y1 - (b / a) * x1;
    *y = x1;
    return gcd;
}

// Modular inverse function
int inverse_mod(int a, int m) {
    int x, y;
    int g = extended_euclid(a, m, &x, &y);
    if (g != 1) {
        return 0;
    } else {
        return (x % m + m) % m;
    }
}
// Point multiplication function
Point point_mul(int k, Point P) {
    Point Q = P;
    for (int i = 1; i < k; i++) {
        // Calculate the slope of the tangent line
        int m = ((3 * Q.x * Q.x + a) * inverse_mod(2 * Q.y, p)) % p;
        // Calculate the new point
        int x = (m * m - Q.x - Q.x) % p;
        int y = (m * (Q.x - x) - Q.y) % p;
        Q.x = x;
        Q.y = y;
    }
    return Q;
}

int main() {
    // Public parameters
    Point alpha = {1, 2}; // generator point
    int y = 3;            // Alice's secret key
    Point x_alpha = {3, 1}; // Bob's public key

    // Calculate shared key
    Point shared_key = point_mul(y, x_alpha);
    printf("Shared key: (%d, %d)\n", shared_key.x, shared_key.y);

    return 0;
}
