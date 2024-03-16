from FermatsMethod import fermats_method
from PollardsMethod import pollards_method


def f(x: int) -> int:
    return x * x + 1


if __name__ == '__main__':
    fermats_method(7301, 20)
    #pollards_method(2, lambda x: x * x + 1, 8359, 20)
