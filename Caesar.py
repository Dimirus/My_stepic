def code(message, key, alphabet, decode=0):
    out_message = ''
    key = (key, key * (-1))[decode]
    for ch in message:
        out_message += alphabet[(alphabet.index(ch) + key + len(alphabet)) % len(alphabet)]
    return out_message


latin_alphabet = [chr(i) for i in range(32, 127)]
cyrillic_alphabet = [chr(i) for i in range(ord('А'), ord('я') + 1)] + \
                    [chr(i) for i in range(32, 65)] + \
                    [chr(i) for i in range(91, 97)] + \
                    [chr(i) for i in range(123, 127)] + ['Ё', 'ё']
print(*cyrillic_alphabet)
original = input('Введите оригинальный текст: ')
n = int(input('Введите ключ: '))

if len(original) > 0:
    if 'a' <= original[0] <= 'z' or 'A' <= original[0] <= 'Z':
        coded = code(original, n, latin_alphabet)
        print(f'Шифрованный текст: {coded}')
        print(f'Расшифрованный текст: {code(coded, n, latin_alphabet, 1)}')
    else:
        coded = code(original, n, cyrillic_alphabet)
        print(f'Шифрованный текст: {coded}')
        print(f'Расшифрованный текст: {code(coded, n, cyrillic_alphabet, 1)}')