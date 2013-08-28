def trace(func):
    def inner(*args, **kwargs):
       
        print func.__doc__
        return func(*args, **kwargs)
    return inner 


@trace
def square(x):
    """Return the square of 'x'"""
    return x * x

#def square(x):
#    return x*x

print square(10)
