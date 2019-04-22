import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("I'm the decorator!")
        func()
        print("after the decorator!")
    return function_that_runs_func


@my_decorator
def my_function():
    print("I'm the function!")


my_function()

##

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func():
            print("in the decorator!")
            if number == 56:
                print("Not running the function!")
            else:
                func()
            print("after the decorator!")
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(56)
def my_function_too():
    print("HellO")


my_function_too()
