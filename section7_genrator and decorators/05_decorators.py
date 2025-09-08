from functools import wraps
def my_decorators(func):
    @wraps(func)
    def wrapper():
        print("Before Function run")
        func()
        print("After Function run")
    return wrapper


@my_decorators
def greet():
    print("Hello from decorator class from chaicode")
    
greet()
print(greet.__name__)