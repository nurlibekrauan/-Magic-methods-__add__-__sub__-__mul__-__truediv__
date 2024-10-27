# Vector & Financial Calculator Suite

### Описание
Этот проект предоставляет набор инструментов на Python для работы с векторами, финансовыми данными и временем. Включает классы для выполнения базовых арифметических операций с векторами, валютами и временем в секундах.

### Классы
- **Vector**: Класс для работы с векторами, поддерживающий операции сложения, вычитания, умножения на число и деления на число. 
- **FinancialValue**: Класс для выполнения финансовых операций и конвертации валют.
- **Clock**: Класс для представления времени в формате HH:MM:SS, поддерживает сложение секунд.

### Пример использования

#### Vector
```python
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = v1 + v2
print(v3)  # Vector([5, 7, 9])

### FinancialValue
```python
usd = FinancialValue(100, "USD")
eur = FinancialValue(80, "EUR", conversion_rate=1.1)
total = usd + eur
print(total)  # FinancialValue(172.73, USD, conversion_rate=1)

###Clock
c1 = Clock(1000)
c2 = Clock(2000)
c1 += c2
print(c1.get_time())  # Вывод времени в формате HH:MM:SS
