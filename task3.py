def my_decorator(is_tip: int, is_tip2: str):
    def decorator(func):
        def wrapper():
            result = func()
            if is_tip:
                return result
            if is_tip2:
                return result
            return f"result: {result}"
        return wrapper
    return decorator
@my_decorator(is_tip=3, is_tip2='')
def a():
    return 'number'
def b():
    return 'line'

print(a())
print(b())