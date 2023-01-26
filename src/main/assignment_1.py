import codeop
import numpy as np
import math

# Question 1: Use double precision, calculate the resulting values (format to 5 decimal places)
#       a) 0 | 10000000111 |pip 1110101110010000000000000000000000000000000000000000
# formula to use: (-1)^s*2^c-1027*(1 + f)

def double_precision():
    
# calculating the sign (s)

    s = 0

# calculating the exponent (c)

    exponent = 10000000111
    c = 0
    i = 0
    while(exponent != 0):
        exp = exponent % 10
        c = c + exp * pow(2, i)
        exponent = exponent // 10
        i += 1

# calculating the fraction (f)

    fraction = str(1110101110010000000000000000000000000000000000000000)
    f = 0
    i = 1
    for item in fraction:
        f = f + int(item) * ((1/2)**i)
        i += 1
    
# formula for converting binary to decimal (n)
    
    n = ((-1)**s)*(2**(c - 1023))*(1 + f)
    print(f"{n:.5f}")
    print("\n")

# Question 2: Repeat question 1 using three-digit chopping arithmetic

    new_n = n
    new_n = n * (10**-3)
    print((math.floor(new_n*1000))/1000)
    print("\n")

# Question 3: Repeat question 1 using three-digit rounding arithmetic

    new_n = new_n + 0.0005
    print(round(new_n, ndigits = 3))
    print("\n")

# Question 4: Compute the absolute and relative error with the exact value form question 1 and its 3 digit rounding

    def absolute_error(x, xbar):
        return abs(x-xbar)

    def relative_error(x, xbar):
        return 0 if x == 0 else absolute_error(x, xbar) / abs(x)
    
    def abs_rel_error():
        number = 491.5625
        rounded_number = 492
        print(absolute_error(number, rounded_number))
        print(relative_error(number, rounded_number))
        return
    abs_rel_error()
    print("\n")

# Question 5: What is the minimum number of terms needed to computer f(1) with error <10^-4?

def error():
    def series(x, k: int):
        return ((-1)**k) * ((x**k) / (k**3))
    
    minError = 1e-4
    currentItteration = 1

    while(abs(series(1, currentItteration)) > minError):
        currentItteration += 1
    
    print(currentItteration - 1)

# Question 6: Determine the number of iterations necessary to solve f(x) = x^3 + 4x^2 - 10 = 0 with accuracy 10^-4
#       a) Using the Bisection Method
#       b) Using the Newton Raphson Method

#Part A(Bisection Method)

def bisection(a: int, b: int, tolerance: float):
    y = b - a
    x = math.log(y,10)
    z = math.log(tolerance, 10)
    equation = (x - z) / (math.log(2,10))
    print(math.ceil(equation))


#def question_6():
    #def f(x):
       # return x**3 + 4(x**2) - 10
    #def f_prime(x):
        #return 3(x**2) + 8*x
    #def my_bisection(f, a, b, tol):
        #m = (a + b) / 2
    #if np.abs(f(m)) < tol:
       #return m
    #elif np.sign(f(a)) == np.sign(f(m)):
       #return my_bisection(f, m, b, tol)
       #return my_bisection(f, m, b, tol) 

#def my_newton(f, df, x0, tol):

   # if abs(f(x0)) < tol:
        #return x0
    #else: None

#print(my_bisection(f, -4, 7, .0001))
#print(my_newton(f, -4, 7, .0001))


if __name__ == "__main__":
    # Question 1-4:
    double_precision()
    #Question 5
    error()
    print("\n")
    #Question 6
    #Bisection Part (1)
    a = -2
    b = 5
    tolerance: float = 10**-4
    bisection(a, b, tolerance)


    #print(newton_raphson(initial_approximation, tolerance, sequence))


