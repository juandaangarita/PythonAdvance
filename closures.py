# hola 3 -> HolaHolaHola
# Facundo 2 ->FacundoFacundo
def make_repeater_of(n):

    def repeater(string):
        assert type(string) == str, "You can only use strings"
        return string * n
    
    return repeater


def make_division_by(n):
    """This closures returns a function that return the division of an x number by n
    """

    def division(x):
        assert type(x) == int, "You can only use integers"
        return x / n

    return division


def run():
    repeat5 = make_repeater_of(5)
    print(repeat5('Onix'))
    division3 = make_division_by(3)
    print(division3(15))


if __name__ == '__main__':
    run()