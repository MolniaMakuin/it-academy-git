my_list = [1,2,[3,4,[5,6]]]
def function(list_1):
    for i in my_list:
        if type(list_1) == list:
            return 1 + max(list(i))
        else:
            return i*function(i-1)
print(function(my_list))