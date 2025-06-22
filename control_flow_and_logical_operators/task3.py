a = True
b = False
c = True

result1 = a and b
print(f"Результат 'a and b' дорівнює {result1}")
# Пояснення: 'a and b' повертає False, оскільки логічний оператор 'and'
# потребує, щоб обидва операнди були True, а 'b' є False.

result2 = a or b
print(f"Результат 'a or b' дорівнює {result2}")
# Пояснення: 'a or b' повертає True, оскільки логічний оператор 'or'
# потребує, щоб хоча б один з операндів був True, і 'a' є True.

result3 = not b
print(f"Результат 'not b' дорівнює {result3}")
# Пояснення: 'not b' повертає True, оскільки логічний оператор 'not'
# інвертує значення 'b' з False на True.

result4 = (a and c) or b
print(f"Результат '(a and c) or b' дорівнює {result4}")
# Пояснення: Спочатку обчислюється вираз у дужках '(a and c)', що дорівнює True (оскільки 'a' і 'c' є True).
# Потім 'True or b' (де 'b' є False) повертає True.

result5 = a and (b or c)
print(f"Результат 'a and (b or c)' дорівнює {result5}")
# Пояснення: Спочатку обчислюється вираз у дужках '(b or c)', що дорівнює True (оскільки 'c' є True).
# Потім 'a and True' (де 'a' є True) повертає True.
