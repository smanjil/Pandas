
def parent():
    print 'Printing from the parent() function..'

    def first_child():
        return 'Printing from the first child() function..'


    def second_child():
        return 'Printing from the second child() function..'


    print first_child()
    print second_child()


parent()
