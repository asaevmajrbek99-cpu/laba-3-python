word = input("Введите слово: ")
m = int(input("Введите m: "))
n = int(input("Введите n: "))

if m == n:
    print(word)
else:
    result = "" # Пустая строка для результата
    for i in range(len(word)):
        if i == m - 1:
            result += word[n - 1] # Вставляем букву n на место m
        elif i == n - 1:
            result += word[m - 1] # Вставляем букву m на место n
        else:
            result += word[i]     # Оставляем букву как есть
            
    print(f"Результат: {result}")