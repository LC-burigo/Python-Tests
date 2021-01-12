def double(values):
    """ double the values in a list
    >>> double([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * element for element in values]


def say_hi():
    """ you can´t put "hi" for expecting
    >>> say_hi()
    'hi'
    """
    return "hi"


def True_that():
    """ you can´t put spaces after the word True...yes, it´s a little weird
    >>> True_that()
    True
    """
    return True


def make_dict(keys):
    """ in doctests, the order of the key in a dict matters. kkkkk hell noooo
    >>> make_dict(['a', 'b'])
    {'a': True, 'b': True}
    """
    return {key: True for key in keys}