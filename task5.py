def decorator():
    name_pupil = ('Pasha', 'Masha')
    counter_pupil = len(name_pupil)
    print(counter_pupil)
    def my_decorator(func):
        language = ('Pasha: Russian, English')
        language2 = ('Masha: Russuan, Belarusian, English')
        print(language)
        print(language2)
    return my_decorator
new_decorator = decorator()

def decorated_function():
        print()
decorated_function = new_decorator(decorated_function)
new_decorator()