# Поиск анаграмм с помощью лямбда-функций и сортировки
is_anagram = lambda x1, x2: sorted(x1) == sorted(x2)


print(is_anagram("elvis", "lives"))
print(is_anagram("elvise", "livees"))
print(is_anagram("elvis", "dead"))
# print(is_anagram("funeral", "real fun"))
