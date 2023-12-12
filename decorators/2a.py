from functools import wraps

class DecorateWithStars:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        if result is None:
            print("No parameters were passed")
        else:
            print('*' * len(str(result)))
            print(result)
            print('*' * len(str(result)))


@DecorateWithStars
def display_text(text):
    return text

text_to_display = 'Hello World!'
display_text(text_to_display)
