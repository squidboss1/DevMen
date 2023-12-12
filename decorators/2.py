from functools import wraps

def decorate_with_stars(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is None:
            print('No parameters were passed')
        else:
            print('*' * len(func(*args)))
            print(func(*args, **kwargs))
            print('*' * len(func(*args)))
    return inner

@decorate_with_stars
def display_text(text):
    return text

text_to_display = 'Hello World!'
display_text(text_to_display)
