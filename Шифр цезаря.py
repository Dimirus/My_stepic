en = 'abcdefghijklmnopqrstuvwxyz'
ru = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
symbol = [" ", ",", ".", "!", "?"]
print("Выберите шифрование: шифрование - lock, дешифрование - unlock")
chif = input()
print("Введите ключ шифрования. Если не знаете, введите '?'")
key = input()
print("Введите фразу")
f = input()
def coder(chif,key,fraze):
    if chif == 'lock':
        key = int(key)
    else:
        key = - int(key)
    coded = ''
    if 'A' <= fraze[0] <= 'Z' or 'a' <= fraze[0] <= 'z':
        for i in range(len(fraze)):
            if fraze[i].islower():
                coded += en[(en.find(fraze[i]) + key) % len(en)]
            elif fraze[i].isupper():
                coded += en[(en.find(fraze[i].lower()) + key) % len(en)].upper()
            else:
                coded += fraze[i]
    else:
        for i in range(len(fraze)):
            if fraze[i].islower():
                coded += ru[(ru.find(fraze[i]) + key) % len(ru)]
            elif fraze[i].isupper():
                coded += ru[(ru.find(fraze[i].lower()) + key) % len(ru)].upper()
            else:
                coded += fraze[i]
    return coded
if key == "?": 
    if 'A' <= f[0] <= 'Z' or 'a' <= f[0] <= 'z':
        for key in range(len(en)):
            print(coder(chif,key,f))
    else:
        for key in range(1,len(ru)):
            print(coder(chif,key,f))
else:
    print(coder(chif,key,f))
