#include "PollardsMethod.h"


#include <stdlib.h>


unsigned long gcd(unsigned long a, unsigned long b)
{
    if (a == 0)
        return b;
    if (b == 0)
        return a;

    // base case
    if (a == b)
        return a;


    if (a > b)
        return gcd(a - b, b);
    return gcd(a, b - a);
}

unsigned long defaultPolynomialMap(unsigned long x, unsigned long n)
{
    unsigned long xModN = x % n;
    return (xModN * xModN % n + 1) % n;
}


unsigned long pollardsMethod(unsigned long n, polynomialMapping function, unsigned long x0, bool *failure)
{
    unsigned long x = x0;
    unsigned long y = function(x, n);
    unsigned long d = 1;

    while (d == 1)
    {
        x = function(x, n);
        y = function(function(y, n), n);

        unsigned long diff = x - y;

        //if the difference would yield a negative failure (we are working mod n)
        //this would be |x - y|
        if  (diff >= n)
            diff = y - x;

        d = gcd(diff, n);


    }

    //if the gcd is d, either it is prime and has no trivial factor or it is composite, but it couldn't find a factor
    //with the given starting value/polynomial map;
    *failure = (n == d);
    return d;
}