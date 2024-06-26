import time

current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time_start_time}s")
    return wrapper_function()

def fast_function():
    for i in range(1000000):
        i * i

def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()
