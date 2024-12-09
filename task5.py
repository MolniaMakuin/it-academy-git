def function():
    count = 0
    def numbers():
        nonlocal count
        count += 1
        return count
    return numbers
numbers = function()
print(numbers())
print(numbers())
print(numbers())