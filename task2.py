def decorator():
    countries = ('Russia', 'Ukraine')
    counter_countries = len(countries)
    print(counter_countries)
    def my_decorator(func):
        first_line = ('Russia Moscow Petersburg Novgorod Kaluga')
        second_line = ('Ukraine Kiev Donetsk Odessa')
        print(first_line)
        print(second_line)
        def wrapped():
            print('Ukraine')
            print('Russia')
            print('Russia')
            return func()
        return wrapped
    return my_decorator
new_decorator = decorator()

def decorated_function():
    print()
decorated_function = new_decorator(decorated_function)
decorated_function()