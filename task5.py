numbers = [1,1,2,3,1,4,5]
def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)
    for number in unique_numbers:
        list_of_unique_numbers.append(number)
    return list_of_unique_numbers
print(get_unique_numbers((numbers)))