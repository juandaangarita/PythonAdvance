def is_palindrome(string: str) -> bool:
    """Return if a string is a palindrome. This function ignore if there are mayus or spaces in the string.

    :param string: The string you will evaluate
    :type string: str
    :returns: a boolean
    
    """
    string = string.replace(' ','').lower()
    return string == string[::-1]


def run():
    print(is_palindrome(1000))


if __name__ == '__main__':
    run()