import math
import cmath
import numpy as np
import sympy as sym

def add(x, y):
    print(f"{x} + {y} = {x + y}")

def subtract(x, y):
    print(f"{x} - {y} = {x - y}")

def multiply(x, y):
    print(f"{x} * {y} = {x * y}")

def divide(x, y):
    print(f"{x} / {y} = {x / y}")

def modulus(x, y):
    print(f"{x} % {y} = {x % y}")

def exponent(x, y):
    print(f"{x}^{y} = {pow(x, y)}")

def factorial(x):
    print(f"{x}! = {math.factorial(abs(x))}")

def complex_add(x, y):
    print(f"{x} + {y} = {complex(x + y)}")

def complex_sub(x, y):
    print(f"{x} - {y} = {x - y}")

def complex_mul(x, y):
    print(f"{x} * {y} = {complex(x * y)}")

def complex_divide(x, y):
    print(f"{x} / {y} = {complex(x / y)}")

def complex_conjugate(x):
    print(f"conjugate of {x} = {complex(np.conj(x))}")

def complex_mod(x):
    print(f"|{x}| = {complex(np.mod(x))}")

def complex_arg(x):
    print(f"arg({x}) = {complex(cmath.phase(x))}")

def sin(x):
    print(f"sin({x}) = {float(np.sin(x))}")

def cos(x):
    print(f"cos({x}) = {float(np.cos(x))}")

def tan(x):
    print(f"tan({x}) = {float(np.tan(x))}")

def arcsin(x):
    print(f"arcsin({x}) = {float(np.arcsin(x))}")

def arccos(x):
    print(f"arccos({x}) = {float(np.arccos(x))}")

def arctan(x):
    print(f"arctan({x}) = {float(np.arctan(x))}")

def sinh(x):
    print(f"sinh({x}) = {float(np.sinh(x))}")

def cosh(x):
    print(f"cosh({x}) = {float(np.cosh(x))}")

def tanh(x):
    print(f"tanh({x}) = {float(np.tanh(x))}")

def arcsinh(x):
    print(f"arcsinh({x}) = {float(np.arcsinh(x))}")

def arccosh(x):
    print(f"arccosh({x}) = {float(np.arccosh(x))}")

def arctanh(x):
    print(f"arctanh({x}) = {float(np.arctanh(x))}")

def complex_sin(x):
    print(f"sin({x}) = {float(cmath.sin(x))}")

def complex_cos(x):
    print(f"cos({x}) = {float(cmath.cos(x))}")

def complex_tan(x):
    print(f"tan({x}) = {float(cmath.tan(x))}")

def complex_arcsin(x):
    print(f"arcsin({x}) = {float(cmath.asin(x))}")

def complex_arccos(x):
    print(f"arccos({x}) = {float(cmath.acos(x))}")

def complex_arctan(x):
    print(f"arctan({x}) = {float(cmath.atan(x))}")

def arcsinh(x):
    print(f"arcsinh({x}) = {float(np.arcsinh(x))}")

def arccosh(x):
    print(f"arccosh({x}) = {float(np.arccosh(x))}")

def arctanh(x):
    print(f"arctanh({x}) = {float(np.arctannh(x))}")

def complex_sinh(x):
    print(f"sinh({x}) = {complex(cmath.sinh(x))}")

def complex_cosh(x):
    print(f"cosh({x}) = {complex(cmath.cosh(x))}")

def complex_tanh(x):
    print(f"tanh({x}) = {complex(cmath.tanh(x))}")

def complex_arcsinh(x):
    print(f"arcsinh({x}) = {complex(cmath.asinh(x))}")

def complex_arccosh(x):
    print(f"arccosh({x}) = {complex(cmath.acosh(x))}")

def complex_arctanh(x):
    print(f"arctanh({x}) = {complex(cmath.atanh(x))}")

def hypotenuse(x, y):
    print(f"hypotenuse of triangle with sides x, y = {float(np.hypot(x, y))}")

def quadratic(a, b, c):
    '''
    Takes 3 arguments, a, b, c as follows:
    ax^2 + bx + c = 0
    '''
    discriminant = (b ** 2) - (4 * a * c)
    x1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    x2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    h = (-b) / (2 * a)
    k = a * h ** 2 + b * h + c
    print(f"Solutions: {x1} and {x2}\nOrigin: ({h},{k})")

def linear_2_simultaneous(a, p, b, q, c, d, r, e, s, f):
    '''
    The letters from the simultaneous equations make up the function arguments:
    ax^p + by^q = c
    dx^r + ey^s = f
    '''
    x, y = sym.symbols("x, y")
    eqn1 = sym.Eq((a * x ** p) + (b * y ** q), c)
    eqn2 = sym.Eq((d * x ** r) + (e * y ** s), f)
    print(f"{a}x^{p} + {b}y^{q} = {c}\n{d}x^{r} + {e}y^{s} = {f}")
    print(f"solution of the eqns above: {sym.solve([eqn1, eqn2], (x, y))}")

def exponential_simultaneous(a, p, b, q, f, c, r, d, s, g):
    '''
    The letters from the simultaneous equations make up the function arguments:
    ax^p + by^q = f
    cx^r + dy^s = g
    '''
    x, y = sym.symbols("x, y")
    eqn1 = sym.Eq((a * x ** p) + (b * y ** q), f)
    eqn2 = sym.Eq((c * x ** r) + (d * y ** s), g)
    print(f"{a}x^{p} + {b}y^{q} = {f}\n{c}x^{r} + {d}y^{s} = {g}")
    print(f"solution of the eqns above: = {sym.solve([eqn1, eqn2], (x, y))}")

def root(n, x):
    """square root function in the form n√x
    Args:
        n (integer between 2 and 5): computes the nth root
        x (float or integer): the number for which the nth root is calculated
    """
    if n == 2:
        print(f"√({x}) = {math.sqrt(x)}")
    elif n == 3:
        print(f"3√({x}) = {x ** 1/3}")
    elif n == 4:
        print(f"4√({x}) = {x ** 1/4}")
    elif n == 5:
        print(f"5√({x}) = {x ** 1/5}")
    else:
        print("Input out of range, try again.")

def polynomial(a, b, c, x):
    """function for calculating polynomials in the form of f(x) = ax^2 + bx + c
    Args:
        a (float or int): x^2 coefficient
        b (float or int): x coefficient
        c (float or int): constant
        x (float or int): the number that goes in f(x)
    """
    print(f"f(x) = {a}x^2 + {b}x + {c}")
    print(f"f({x}) = {a * pow(x, 2) + (b * x) + c}")
