import math

def newton(function, derivative, po, tol):
    n=0
    pn = po
    error = tol + 1
    while error > tol:
        pn = po - (float)(function(pn)/derivative(pn))
        error = math.fabs(pn - po)
        po = pn
        print("%3d          %.8f     %.6f" % (n, pn, error))
        n += 1
