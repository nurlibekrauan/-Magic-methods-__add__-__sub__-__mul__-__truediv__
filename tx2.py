class Matrix:
    def verify_matrix(self, matrix):
        if not isinstance(matrix, list):
            raise TypeError("Matrix must be a list")
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("All elements in matrix must be lists")
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise ValueError("All rows in matrix must have the same length")

    def __init__(self, matrix) -> None:
        self.verify_matrix(matrix)
        self.matrix = matrix

    def __add__(self, other):
        self.verify_matrix(other.matrix)
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)

    def __sub__(self, other):
        self.verify_matrix(other.matrix)
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)

    def __mul__(self, multiplier):
        if isinstance(multiplier, Matrix):  # Умножение матриц
            if len(self.matrix[0]) != len(multiplier.matrix):
                raise ValueError("Number of columns in first matrix must be equal to the number of rows in second matrix")
            result = [[sum(self.matrix[i][k] * multiplier.matrix[k][j] for k in range(len(multiplier.matrix))) for j in range(len(multiplier.matrix[0]))] for i in range(len(self.matrix))]
            return Matrix(result)
        elif isinstance(multiplier, (int, float)):  # Умножение на число
            result = [[self.matrix[i][j] * multiplier for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
            return Matrix(result)
        else:
            raise TypeError("The second operand must be a number or a matrix")

    def __truediv__(self, divisor):
        if not isinstance(divisor, (float, int)):
            raise TypeError("The second operand must be a number")
        result = [[self.matrix[i][j] / divisor for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)

    def __repr__(self):
        return f"Matrix({self.matrix})"


# Пример использования
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

m3 = m1 + m2        # Matrix([[6, 8], [10, 12]])
m4 = m1 * m2        # Matrix([[19, 22], [43, 50]]) — умножение матриц
m5 = m1 / 2         # Matrix([[0.5, 1], [1.5, 2]])

print(m3)  # Matrix([[6, 8], [10, 12]])
print(m4)  # Matrix([[19, 22], [43, 50]])
print(m5)  # Matrix([[0.5, 1], [1.5, 2]])
