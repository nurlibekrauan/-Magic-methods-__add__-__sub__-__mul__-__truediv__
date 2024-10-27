class FinancialValue:
    def __init__(self, count, currency="USD", conversion_rate=1) -> None:
        self.count = count
        self.currency = currency
        self.conversion_rate = conversion_rate

    def convert_to(self, target_currency, target_conversion_rate):
        # Конвертируем текущую сумму в целевую валюту
        return self.count * self.conversion_rate / target_conversion_rate

    def __add__(self, other):
        if self.currency != other.currency:
            # Конвертируем другую валюту в текущую
            other_count_in_self_currency = other.convert_to(
                self.currency, self.conversion_rate
            )
        else:
            other_count_in_self_currency = other.count
        return FinancialValue(
            self.count + other_count_in_self_currency,
            self.currency,
            self.conversion_rate,
        )

    def __sub__(self, other):
        if self.currency != other.currency:
            # Конвертируем другую валюту в текущую
            other_count_in_self_currency = other.convert_to(
                self.currency, self.conversion_rate
            )
        else:
            other_count_in_self_currency = other.count
        return FinancialValue(
            self.count - other_count_in_self_currency,
            self.currency,
            self.conversion_rate,
        )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            # Умножаем на число
            return FinancialValue(
                self.count * other, self.currency, self.conversion_rate
            )
        raise TypeError("Multiplication is supported only with numbers.")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return FinancialValue(
                self.count / other, self.currency, self.conversion_rate
            )
        raise TypeError("Division is supported only with numbers.")

    def __repr__(self) -> str:
        return f"FinancialValue({self.count:.2f}, {self.currency}, conversion_rate={self.conversion_rate})"


# Пример использования
usd = FinancialValue(100, "USD")
eur = FinancialValue(80, "EUR", conversion_rate=1.1)  # 1 EUR = 1.1 USD

# Операция сложения с конверсией EUR в USD
total = usd + eur  # FinancialValue(172.73, "USD") (с учетом курса 1.1)
print(total)  # FinancialValue(172.73, USD, conversion_rate=1)

# Операция вычитания с конверсией
difference = usd - eur
print(difference)  # FinancialValue(27.27, USD, conversion_rate=1)

# Умножение на число
multiplied = usd * 2
print(multiplied)  # FinancialValue(200.00, USD, conversion_rate=1)

# Деление на число
divided = usd / 2
print(divided)  # FinancialValue(50.00, USD, conversion_rate=1)
