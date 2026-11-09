text = input("Введите предложение: ")

clean_text = text.strip()

while '  ' in clean_text:
    clean_text = clean_text.replace('  ', ' ')

count = clean_text.count(' ') + 1

print(f"Количество слов: {count}")