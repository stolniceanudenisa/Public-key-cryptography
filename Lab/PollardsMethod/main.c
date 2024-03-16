#include <stdio.h>

#include "PollardsMethod.h"


unsigned long polynomialMap(unsigned long x, unsigned long n)
{
    int xModN = x % n;
    return (xModN * xModN % n + 1) % n;
}


int main()
{
    const unsigned long n = 12312311;
    bool failure;
    unsigned long factor = pollardsMethod(n, defaultPolynomialMap, 2, &failure);
    if (failure)
        printf("Could not find a non-trivial factor, n might be prime. If it is not prime, try again with different "
               "starting values or another polynomial function");
    else
        printf("Factor1: %lu \nFactor2: %lu", factor, n/factor);

    return 0;
}
