def reinput(text, key='int'):
    if key == 'int':
        try:
            value = int(input())
            return value
        except ValueError:
            print(text)
            return reinput(text)
    elif key == 'posint':
        try:
            value = int(input())
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print(text)
            return reinput(text, 'posint')


def is_integer(value, text="Value must be integer number. Enter again:"):
    try:
        value = int(value)
        return value
    except ValueError:
        print(text)
        return reinput(text)

def is_positive_int(value, text='Value must be positive integer number. Enter again:'):
    try:
        value = int(value)
        if value <= 0:
            raise ValueError
        return value
    except ValueError:
        print(text)
        return reinput(text, 'posint')
