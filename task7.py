def decorator():
    def wrapper():
        for i in range(1,10):
            if i == 4:
                break
            else:
                print(i)
    return wrapper
@decorator
def a():
    return i

print(a())