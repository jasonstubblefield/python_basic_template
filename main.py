import custom_math

def do_math(a, b):

    result = custom_math.add(a, b)

    return result

if __name__ == '__main__':

    a = 1

    b = 2

    print(do_math(a, b))

def test_add_positive_numbers():
    assert do_math(1, 2) == 3

def test_add_negative_numbers():
    assert do_math(-1, -1) == -2

def test_add_zero():
    assert do_math(0, 0) == 0