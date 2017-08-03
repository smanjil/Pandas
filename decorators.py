

def my_decorator(some_function):

    def wrapper():
        print 'Something is happening before the function is called!'

        some_function()

        print 'Something is happening after the function is called!'

    return wrapper


@my_decorator
def just_some_function():
    print 'Wheeeeee'


#just_some_function = my_decorator(just_some_function)

just_some_function()
