import time

def timing_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        result = original_function(*args, **kwargs)
        end_time = time.time()
        print(f"{original_function.__name__} ran in {end_time - start_time} seconds")
        return result
    return wrapper_function

@timing_decorator
def slow_function():
    time.sleep(2)

slow_function()  # Output: slow_function ran in 2.002163887023926 seconds