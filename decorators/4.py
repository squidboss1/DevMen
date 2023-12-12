def type_check(expected_type):
    def check_types(func):
        def wrapper(*args, **kwargs):
            for arg, arg_type in zip(args, func.__annotations__.values()):
                if not isinstance(arg, arg_type):
                    raise TypeError(f"Expected {arg_type} instead of '{arg}', which is/are '{type(arg)}'.")

            result = func(*args, **kwargs)

            return result

        return wrapper

    return check_types


@type_check(int)
def example_function(num: int):
    print(f"This is an example function with argument: {num}")
    pass


@type_check(str)
def another_function(text: str):
    print(f"This is another function with argument: {text}")
    pass


@type_check(dict)
def another_function2(dictus: dict):
    print(f"This is another function with argument: {dictus}")
    pass


# Przykłady użycia
# Poprawne
example_function(42)
example_function(4253765858678)
another_function("Hello Baby!")
another_function2({'key': 'value'})

# Niepoprawne
example_function("RandomString")
another_function(42)
another_function("text")
