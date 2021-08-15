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
    if lan == 'r':
        for i in range(len(fraze)):
            if fraze[i].islower():
                shifred += rus_lower_alphabet[(rus_lower_alphabet.find(fraze[i]) + key) % len(rus_lower_alphabet)]
            elif fraze[i].isupper():
                shifred += rus_upper_alphabet[(rus_upper_alphabet.find(fraze[i]) + key) % len(rus_upper_alphabet)]
            else:
                shifred += fraze[i]
                
    if lan == 'e':
        for i in range(len(fraze)):
            if fraze[i].islower():
                shifred += en_lower_alphabet[(en_lower_alphabet.find(fraze[i]) + key) % len(en_lower_alphabet)]
            elif fraze[i].isupper():
                shifred += en_upper_alphabet[(en_upper_alphabet.find(fraze[i]) + key) % len(en_upper_alphabet)]
            else:
                shifred += fraze[i]
        
        
        
        
        
    return shifred
#def deshifr()
lan = 'e'
chif = 'ch'
key = 3
f = 'gfif'
print(shifr(lan,chif,key,f))
