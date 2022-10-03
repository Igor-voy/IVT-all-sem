def func(double x):
    return ((0.8*x**2 + 1)**(1/2))/(x + (1.5*x**2 + 2)**(1/2))

def integrate(f, double a, double b, *, int n_iter = 1000):
    cdef double h, s, x, result 
    h = (b-a)/n_iter
    s = 0
    x = a 

    while x <= (b - h):
        inter = f(x)
        s += inter
        x += h 

    result = h*s 

    return round(result, 6)
