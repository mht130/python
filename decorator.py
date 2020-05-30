def my_decorator(func):
    def a():
        print("hi")
        func()
    return a

@my_decorator
def say():
    print("abc")


# say=my_decorator(say)
say()