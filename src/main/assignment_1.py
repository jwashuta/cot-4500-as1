import codeop
import numpy as np
import math

# Question 1: Use double precision, calculate the resulting values (format to 5 decimal places)
#       a) 0 | 10000000111 | 1110101110010000000000000000000000000000000000000000
# formula to use: (-1)^s*2^c-1027*(1 + f)

def double_precision():
    # calculating the sign (s)
    s = 0
    print(s)
    print("\n")

    # calculating the exponent (c)
    exponent = 10000000111
    c = 0
    i = 0
    while(exponent != 0):
        exp = exponent % 10
        c = c + exp * pow(2, i)
        exponent = exponent // 10
        i += 1
    print(c)
    print("\n")

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

n = n * (10**-3)
math.floor((n*1000)/1000)
print("\n")

# Question 3: Repeat question 1 using three-digit rounding arithmetic

n = n + 0.0005
print(round(n, ndigits = 3))
print("\n")

# Question 4: Compute the absolute and relative error with the exact value form question 1 and its 3 digit rounding

# Question 5: What is the minimum number of terms needed to computer f(1) with error <10^-4?
def question_5():
    def series(x,k:int):
        return ((-1)**k) * ((x**k)/(k**3))
    
    minError = 1e-4
    currentItteration = 1
    while(abs(series(currentItteration)) > minError):
        #print(serries(1,currentItteration))
        currentItteration += 1
    print()
    print(currentItteration)

# Question 6: Determine the number of iterations necessary to solve f(x) = x^3 + 4x^2 - 10 = 0 with accuracy 10^-4
#       a) Using the Bisection Method
#       b)Using the Newton Raphson Method

def custom_derivative(value):
    return(3 * value * value) - (value ** 2) + 2

def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    iteration_counter = 0

    # finds f
    x = initial_approximation
    f = eval(sequence)

    # finds f'
    f_prime = custom_derivative(initial_approximation)

    approximation: float = f / f_prime
    while(abs(approximation) >= tolerance):
        # finds f
        x = initial_approximation
        f = eval(sequence)
        # finds f'
        f_prime = custom_derivative(initial_approximation)

        # division operation
        approximation =  f / f_prime

        # subtraction operation
        initial_approximation -= approximation
        iteration_counter += 1

if __name__ == "__main__":
    # Question 1:
    print(double_precision())
    print("\n")

    # Question 5:
    # print("\n")
    
    # Question 6:
    initial_approximation: float = -4
    tolerance: float = 7
    sequence: str = "(x**3) + 4*(x**2) - 10"
    print(newton_raphson(initial_approximation, tolerance, sequence))

