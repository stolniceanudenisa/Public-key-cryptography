#ifndef PROJECT3_POLLARDSMETHOD_H
#define PROJECT3_POLLARDSMETHOD_H

#include <stdbool.h>
/// \brief unsigned long polynomialMapping(unsigned long x, unsigned long n)\n
///         polynomialMapping: Zn -> Zn\n\n
///         It must be a polynomial mapping of degree greater than 1, preferably
/// not bijective
typedef unsigned long (*polynomialMapping)(unsigned long, unsigned long);

unsigned long defaultPolynomialMap(unsigned long x, unsigned long n);

unsigned long pollardsMethod(unsigned long n, polynomialMapping function, unsigned long x0, bool *failure);

#endif //PROJECT3_POLLARDSMETHOD_H
