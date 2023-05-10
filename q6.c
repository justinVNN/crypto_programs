#include <stdio.h>

int main() {
    int x, y;

    printf("Points on elliptic curve E: y^3 ≡ x^3 - 2x (mod 5)\n");
    for (x = 0; x < 5; x++) {
        for (y = 0; y < 5; y++) {
            if ((y*y*y) % 5 == ((x*x*x) - 2*x) % 5) {
                printf("(%d, %d)\n", x, y);
            }
        }
    }

    return 0;
}
