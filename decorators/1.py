from functools import wraps

def logged(func):
    @wraps(func)
    def inner(*args, **kwargs):
        saved_args = locals()['args']
        saved_kwargs = locals()['kwargs']
        func_result = func(*args, **kwargs)

        print(f"""You called function named: '{func.__name__}',\nwith this args: '{saved_args}',\nand kwargs: '{saved_kwargs}'.\nThis function returns: {func_result}""")

    return inner

@logged
def func(*args):
    return 3 + len(args)

func(4, 4, 4)
