def is_prime(number: int) -> bool:
    """Return if a number is a prime number which means if is only has two factor 1 and itself

    :param number: The number you want to evaluate
    :type number: int
    :returns: Boolean True meaning number is a prime number

    """
    factors = [i for i in range(2, number) if number % i == 0]
    return len(factors) == 0


def run():
    print(is_prime(5))


if __name__ == '__main__':
    run()