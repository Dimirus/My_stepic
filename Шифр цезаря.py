en_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
en_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"]

#print("Выберите язык: aнгл=e, рус=r")
#lan = input()
#print("Выберите шифрование: шифрование - ch, дешифрование - def")
#chif = input()
#print("Введите ключ шифрования")
#key = int(input())
#print("Введите фразу")
#f = input()
def shifr(lan,chif,key,fraze):
    shifred = ''
    if lan == 'ru':
        for i in range(len(fraze)):
            if fraze[i].islower():
                shifred += rus_lower_alphabet[(rus_lower_alphabet.find(fraze[i]) + key) % len(rus_lower_alphabet)]
            elif fraze[i].isupper():
                shifred += rus_upper_alphabet[(rus_upper_alphabet.find(fraze[i]) + key) % len(rus_upper_alphabet)]
            else:
                shifred += fraze[i]
                
    if lan == 'en':
        for i in range(len(fraze)):
            if fraze[i].islower():
                shifred += en_lower_alphabet[(en_lower_alphabet.find(fraze[i]) + key) % len(en_lower_alphabet)]
            elif fraze[i].isupper():
                shifred += en_upper_alphabet[(en_upper_alphabet.find(fraze[i]) + key) % len(en_upper_alphabet)]
            else:
                shifred += fraze[i]        
    return shifred
def deshifr(lan,chif,key,fraze):
    deshifred = ''
    if lan == 'ru':
        for i in range(len(fraze)):
            if fraze[i].islower():
                deshifred += rus_lower_alphabet[(rus_lower_alphabet.find(fraze[i]) - key) % len(rus_lower_alphabet)]
            elif fraze[i].isupper():
                deshifred += rus_upper_alphabet[(rus_upper_alphabet.find(fraze[i]) - key) % len(rus_upper_alphabet)]
            else:
                deshifred += fraze[i]
                
    if lan == 'en':
        for i in range(len(fraze)):
            if fraze[i].islower():
                deshifred += en_lower_alphabet[(en_lower_alphabet.find(fraze[i]) - key) % len(en_lower_alphabet)]
            elif fraze[i].isupper():
                deshifred += en_upper_alphabet[(en_upper_alphabet.find(fraze[i]) - key) % len(en_upper_alphabet)]
            else:
                deshifred += fraze[i]        
    return deshifred
lan = 'en'
chif = 'ch'
f = 'Hawnj pk swhg xabkna ukq nqj.'
for key in range(26):
    print(deshifr(lan,chif,key,f))
