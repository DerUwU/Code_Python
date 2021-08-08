letra = str(input("Una letra: ")).lower()
vocales = "a","e","i","o","u"

if len(letra) >= 2:
    print("Solo una letra >:v")
    print(len(letra))
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"{letra} Es vocal")
else:
        print(f"{letra} No es vocal")