import random
print('Добро пожаловать в числовую угадайку')
text = -1
play = 'y'
def is_valid(text, m):
    text = int(text)
    m = int(m)
    if int(text) in range(1,m):
        return True
    else:
        return False
def body(text, m):
    n = 1
    c = random.randint(1, int(m) + 1)
    text = int(text)
    while text != c:
            n += 1
            if text < c:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                print('Введите число')
                text = int(input())
            elif text > c:
                print('Ваше число больше загаданного, попробуйте еще разок')
                print('Введите число')
                text = int(input())
            else:
                print('Вы угадали, поздравляем!')
                print('Вы затратили', n, 'попыток')
                print('Хотите играть ещё? y / n ? ')
    else:
        print('Вы угадали, поздравляем!')
        print('Вы затратили', n, 'попыток')
        print('Хотите играть ещё? y / n ?')
while play == 'y':
    print('Введите максимальное загадываемое число')
    m = input()
    print('Введите число')
    text = input()
    if is_valid(text, m):
        body(text, m)
        play = input()
    else:
        print('А может быть все-таки введем целые числа от 1 до 100?')
else:
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...') 