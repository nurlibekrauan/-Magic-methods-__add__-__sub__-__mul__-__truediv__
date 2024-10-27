class Vector:
    def verify_vector(self, vector):
        if not all(isinstance(x, (int, float)) for x in vector):
            raise ValueError("Вектор должен состоять из чисел")


    def __init__(self, coords: list) -> None:
        self.verify_vector(coords)
        self.coords = coords

    def __add__(self, other):
        self.verify_vector(other.coords)  # Проверяем координаты другого вектора
        return Vector([x + y for x, y in zip(self.coords, other.coords)])

    def __sub__(self, other):
        self.verify_vector(other.coords)  # Проверяем координаты другого вектора
        return Vector([x - y for x, y in zip(self.coords, other.coords)])

    def __mul__(self, multiplier):
        if not isinstance(multiplier, (int, float)):
            raise ValueError("Множитель должен быть числом")
        return Vector([x * multiplier for x in self.coords])

    def __truediv__(self, divider):
        if divider == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return Vector([x / divider for x in self.coords])

    def __repr__(self):
        return f"Vector({self.coords})"


# Пример использования
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

v3 = v1 + v2        # Vector([5, 7, 9])
v4 = v1 - v2        # Vector([-3, -3, -3])
v5 = v1 * 2         # Vector([2, 4, 6])
v6 = v2 / 2         # Vector([2, 2.5, 3])

print(v3)  # Vector([5, 7, 9])
print(v4)  # Vector([-3, -3, -3])
print(v5)  # Vector([2, 4, 6])
print(v6)  # Vector([2, 2.5, 3])
