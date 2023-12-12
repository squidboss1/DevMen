from functools import wraps

def count(func):
    counts = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal counts
        function_name = func.__name__
        counts[function_name] = counts.get(function_name, 0) + 1

        result = func(*args, **kwargs)

        print(f"{function_name} was called {counts[function_name]} times.")

        return result
    return wrapper


@count
def example_function():
    print("This is an example function.")

@count
def example_function2():
    print("This is another function.")

example_function()
example_function()
example_function2()
example_function()
example_function2()

