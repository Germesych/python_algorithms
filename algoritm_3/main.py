# Подсчет количества перестановок с помощью рекурсивных функций вычисления факториалов
n = 5

factorial = lambda n: n * factorial(n - 1) if n > 1 else 1

# Результат
print(factorial(n))