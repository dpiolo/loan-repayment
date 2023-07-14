
def integrate(F, a, b, N):
    """
    Approximates the definite integral of a function using the trapezoidal rule.

    Parameters:
        F (function): The function to be integrated.
        a (float): The left endpoint of the interval.
        b (float): The right endpoint of the interval.
        N (int): The number of trapezoids to use for the approximation.

    Returns:
        float: The approximate value of the definite integral.
    """
    h = (b - a) / N 
    integral = (F(a) + F(b)) / 2

    for i in range(1, N):
        x = a + i * h  
        integral += F(x)
    integral *= h  

    return integral

if __name__ == "__main__":
    def f(x):
      return x**2
    area = integrate(f,0.5,2.,50000)
    print(f"area: {area}")