import time


def timethis(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        func(*args, **kwargs)

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"'{func.__name__}' took {elapsed_time:.10f} seconds to execute.")

        return

    return wrapper


@timethis
def sleep_function():
    time.sleep(2)
    print("Function executed.")


sleep_function()
