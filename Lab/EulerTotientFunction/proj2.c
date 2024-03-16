#include <stdio.h>
#include <math.h>

unsigned long int phi(unsigned long n)
{
    unsigned long result = n;

    for (unsigned long d = 2; d * d <= n ; ++d)
    {
        int wasDivided = 0;
        while (n % d == 0)
        {
            wasDivided = 1;
            n /= d;
        }

        if (wasDivided)
        {
            result /= d;
            result *= (d - 1);
        }
    }

    if (n > 1)
    {
        result /= n;
        result *= (n - 1);
    }
    return result;
}

int main(void)
{
    while(1)
    {
        unsigned long v;
        printf("Input v:\n>>\t");
        scanf("%lu", &v);

        unsigned long b;
        printf("Input b:\n>>\t");
        scanf("%lu", &b);

        unsigned long lowerBound = v * v * 2 + 1; //+ 1 for an error margin
        lowerBound = (lowerBound < b) ? lowerBound : b;

        for (unsigned long i = 0; i <= lowerBound; ++i)
        {
            if (phi(i) == v)
                printf("phi(%lu) = %lu\n", i, v);
        }
        printf("\n\n");
    }
    return 0;
}
