# Магические методы __add__, __sub__, __mul__, __truediv__

# __add__() – для операции сложения;
# __sub__() – для операции вычитания;
# __mul__() – для операции умножения;
# __truediv__() – для операции деления.


class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted__(h)}:{self.__get_formatted__(m)}:{self.__get_formatted__(s)}"

    @classmethod
    def __get_formatted__(cls, x: int):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("the argument must be an integer")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("the argument must be an integer")
        sc = other
        if isinstance(sc, Clock):
            sc = sc.seconds
        self.seconds += sc
        return self


c1 = Clock(1000)
c2 = Clock(2000)
c3 = Clock(3000)
c1 += c2
print(c1.get_time())
