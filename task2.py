import time

def my_function(is_time: True, is_time2: False):
    def function(func):
        def wrapper():
            result=func()
            for i in range(1, 7):
                if i > 4:
                    print('число больше')
                else:
                    print('число меньше')
            start = time.time()
            end = time.time()
            elapsed = end + start
            print(f'время {elapsed:.2f} seconds.')
            return result
        return wrapper
    return function
@my_function(is_time=True, is_time2=False)
def f():
    return 'в секундах'
print(f())