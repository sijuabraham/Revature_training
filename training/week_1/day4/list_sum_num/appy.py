def list_sum(*args):
    my_sum = 0
    for element in args:
        my_sum += element
    return my_sum


print(list_sum(2, 3, 4))

