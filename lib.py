from future.builtins import round


def my_round(x):
    """
    The built-in round function behaves differently in Python 2.7 and Python 3.6. We hence use this little
    (useless) function as the code we want the CI to test on the two major python versions
    and make sure our code behaves the same (thanks to the future import).
    :param x: a numerical value
    :return: the rounded value
    """
    return round(x)
