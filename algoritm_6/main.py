# Реализация шифра Цезаря с помощью расширенного доступа по индексу и спискового включения

## Данные
abc = "abcdefghijklmnopqrstuvwxyz"
s = "xthexrussiansxarexcoming"


## Однострочник
rt13 = lambda x: "".join([abc[(abc.find(c) + 13) % 26] for c in x])


## Результат
print(rt13(s))
print(rt13(rt13(s)))





