from typing import Callable

# compose function

def compose(*functionsList: Callable) -> Callable:
    def composed(*args, **kwargs):
        result = None
        for func in functionsList:
            if result is None:
                result = func(*args, **kwargs)
            else:
                result = func(result)
        return result
    
    return composed



# functions

def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

def subtract_three(x):
    return x - 3



# Create composed functions
composed_function = compose(add_one, multiply_by_two, subtract_three)

# Usage: composed_function(5) computes ((5 + 1) * 2) - 3, which results in 9.
result = composed_function(5)
print(result) # Output: 9
