def list_sum(*args):
    my_sum = 0
    for element in args:
        my_sum += element
    return my_sum


def test_answer():
    assert list_sum(3, 5) == 8


def test_answer():
    assert list_sum(2, 6, 6) == 15