def do_math(*args, **kwargs):
    # print(type(kwargs))
    if kwargs['operation'] == 'add':
        my_sum = 0
        for element in args:
            my_sum += element

        return my_sum

    elif kwargs['operation'] == 'multiply':
        my_product = 1
        for element in args:
            my_product *= element

    return my_product


print(do_math(2, 3, operation="add"))
print(do_math(2, 3, 5, operation="multiply"))

