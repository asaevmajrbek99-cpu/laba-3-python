s = input("Введите слово: ")
m = int(input("Введите номер первой буквы m: "))
n = int(input("Введите номер второй буквы n: "))

i = m - 1
j = n - 1

letters = list(s)

letters[i], letters[j] = letters[j], letters[i]

result = ''.join(letters)

print("Результат:", result)