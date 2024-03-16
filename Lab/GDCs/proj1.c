#include <stdio.h>
#include <gmp.h>
#include <time.h>
#include <stdlib.h>

#define MAX_RANGE 1100
#define MIN_RANGE 800

int gcdBasic(int a, int b)
{
    if (a == 0) return b;
    if (b == 0) return a;
    int div = (a < b)? a : b;
    while (div > 0)
    {
        if (a % div == 0 && b % div == 0)
            return div;
        div--;
    }
    return 1;
}
void gcdBasicBigInt(mpz_t a, mpz_t b, mpz_t result)
{
    if (mpz_cmp_ui(a, 0) == 0)
    {
        mpz_init_set(result, b);
        return;
    }
    if (mpz_cmp_ui(b, 0) == 0)
    {
        mpz_init_set(result, a);
        return;
    }

    mpz_t div;
    if(mpz_cmp(a, b) < 0)
        mpz_init_set(div, a);
    else
        mpz_init_set(div, b);

    while (mpz_cmp_ui(div, 0) > 0)
    {
        mpz_t aModDiv;
        mpz_init(aModDiv);
        mpz_mod(aModDiv, a, div);

        mpz_t bModDiv;
        mpz_init(bModDiv);
        mpz_mod(bModDiv, b, div);

        if (mpz_cmp_ui(aModDiv, 0) == 0 && mpz_cmp_ui( bModDiv, 0) == 0) {

            mpz_clear(aModDiv);
            mpz_clear(bModDiv);

            break;
        }

        mpz_clear(aModDiv);
        mpz_clear(bModDiv);

        mpz_sub_ui(div, div, 1);
    }

    mpz_init_set(result, div);
    mpz_clear(div);
}

int gcdSub(int a, int b)
{

    if (a == 0) return b;
    if (b == 0) return a;

    if (a == b) return a;

    if (a > b)
        return gcdSub(a - b, b);
    else
        return gcdSub(a, b - a);
}

int gcdMod(int a, int b)
{
    if (a == 0)
        return b;
    else
        return gcdMod(b % a, a);
}

int gcdExtended(int a, int b, int* x, int* y)
{
    if (a == 0) {
        *x = 0;
        *y = 1;
        return b;
    }

    int x1, y1;
    int gcd = gcdExtended(b % a, a, &x1, &y1);

    *x = y1 - (b / a) * x1;
    *y = x1;

    return gcd;
}
void testValues(void)
{
    const int INTERVAL_START = 8;
    const int INTERVAL_END = 12;

    for (int i = INTERVAL_START; i <= INTERVAL_END; i++)
    {
        for (int j = i; j <= INTERVAL_END; j++)
        {
            mpz_t iBig, jBig;
            mpz_init_set_ui(iBig, i);
            mpz_init_set_ui(jBig, j);

            mpz_t gcdMpz;
            gcdBasicBigInt(iBig, jBig, gcdMpz);


            char *gcdStr = mpz_get_str(NULL, 10, gcdMpz);
            printf("gcdBasicBigInt(%d, %d) = %s\n", i, j, gcdStr);
            free(gcdStr);

            mpz_clear(iBig);
            mpz_clear(jBig);
            mpz_clear(gcdMpz);
            

            int gcd = gcdBasic(i, j);
            printf("gcdBasic(%d, %d) = %d\n", i, j, gcd);

            gcd = gcdSub(i, j);
            printf("gcdSub(%d, %d) = %d\n", i, j, gcd);
            
            int x, y;
            gcd = gcdExtended(i, j, &x, &y);
            printf("gcdExtended(%d, %d) = %d\n", i, j, gcd);

            gcd = gcdMod(i, j);
            printf("gcdMod(%d, %d) = %d\n", i, j, gcd);
        
            
            printf("\n\n");
        }   
    }

}
void testTime(void)
{
    clock_t startGcdBasicBig = clock();
    for (unsigned long a = MIN_RANGE; a <= MAX_RANGE; ++a)
    {
        for (unsigned long b = MIN_RANGE; b <= MAX_RANGE; ++b)
        {
            mpz_t aBig, bBig;
            mpz_init_set_ui(aBig, a);
            mpz_init_set_ui(bBig, b);

            mpz_t gcd;
            gcdBasicBigInt(aBig, bBig, gcd);


            //char *gcdStr = mpz_get_str(NULL, 10, gcd);
            //printf("\tgcd(%lu, %lu) = %s\n", a, b, gcdStr);
            //free(gcdStr);

            mpz_clear(aBig);
            mpz_clear(bBig);
            mpz_clear(gcd);
        }
    }
    long double deltaTimeGcdBasicBig = clock() - startGcdBasicBig;
    deltaTimeGcdBasicBig /= CLOCKS_PER_SEC;
    printf("Time Basic (BigInt):\t %Lf s\n", deltaTimeGcdBasicBig);

    clock_t startGcdBasic = clock();
    for (int a = MIN_RANGE; a <= MAX_RANGE; ++a)
    {
        for (int b = MIN_RANGE; b <= MAX_RANGE; ++b)
        {
            int gcd = gcdBasic(a, b);
            (void)gcd;
        }
    }
    long double deltaTimeGcdBasic = clock() - startGcdBasic;
    deltaTimeGcdBasic /= CLOCKS_PER_SEC;
    printf("Time Basic:\t\t %Lf s\n", deltaTimeGcdBasic);

    clock_t startGcdSub = clock();
    for (int a = MIN_RANGE; a <= MAX_RANGE; ++a)
    {
        for (int b = MIN_RANGE; b <= MAX_RANGE; ++b)
        {
            int gcd = gcdSub(a, b);
            (void)gcd;
        }
    }
    long double deltaTimeGcdSub  = clock() -  startGcdSub;
    deltaTimeGcdSub /= CLOCKS_PER_SEC;
    printf("Time Substitution:\t %Lf s\n", deltaTimeGcdSub);

    clock_t startGcdExtended = clock();
    int x, y;
    for (int a = MIN_RANGE; a <= MAX_RANGE; ++a)
    {
        for (int b = MIN_RANGE; b <= MAX_RANGE; ++b)
        {
            int gcd = gcdExtended(a, b, &x, &y);
            (void)gcd;
        }
    }
    long double deltaTimeGcdExtended = clock() -  startGcdExtended;
    deltaTimeGcdExtended /= CLOCKS_PER_SEC;
    printf("Time Extended:\t\t %Lf s\n", deltaTimeGcdExtended);

    clock_t startGcdMod = clock();
    for (int a = MIN_RANGE; a <= MAX_RANGE; ++a)
    {
        for (int b = MIN_RANGE; b <= MAX_RANGE; ++b)
        {
            int gcd = gcdMod(a, b);
            (void)gcd;
        }
    }
    long double deltaTimeGcdMod = clock() -  startGcdMod;
    deltaTimeGcdMod /= CLOCKS_PER_SEC;
    printf("Time Modulo:\t\t %Lf s\n", deltaTimeGcdMod);

}

/*
 * This program has only been run on linux, using gcc. It depends on GMP (The GNU Multiple Precision Arithmetic Library)
 * in order to compile. This library was used to have integers of arbitrary precision.
 */
int main(void)
{

    testValues();
    testTime();
    return 0;
}
