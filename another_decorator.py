
def my_decorator(some_function):

    def wrapper():
        num = 10
        if num == 10:
            print 'Yes'
        else:
            print 'No'

        some_function()

        print 'Something is happening after the function!'

    return wrapper


@my_decorator
def just_some_function():
    print 'Wheeeee!'


just_some_function()
