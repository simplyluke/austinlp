# Yay, docstrings
# Use them!

def fact(n):
    """This function computes a factorial. It uses recursion."""
    if (n<=1): return 1
    else:
        return n * fact(n - 1)

if __name__ == "__main__":
    print fact.__doc__
    print fact(20)
