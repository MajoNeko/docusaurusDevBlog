# 1 - Welche Ausgaben werden durch die folgenden Code-Beispiele erzeugt?
passwort1 = "abc123"
passwort2 = "Pass Wort"
passwort3 = "u1tr4g3h31m "

print(passwort1.upper()) # ABC123
print(passwort2.lower()) # pass wort
print(passwort3.islower()) # True
print(passwort2.isupper()) # False
print(passwort1.zfill(8)) # 00abc123
print(passwort2.strip()) # Pass Wort
print(len(passwort3)) # 12
print(passwort1.isalpha()) # False
print(passwort1[3:].isnumeric()) # True
print("a;b;c;d;e".split(';')) # ['a','b','c','d','e']
print("01.23.45.67.89".split(';')) # ['01.23.45.67.89']
print(passwort2.replace("Pass",'.')) # . Wort
print(passwort3.count('3')) # 2
print(passwort2.count('s')) # 2
print(passwort3.find(2+2)) # Typeerror
print(passwort1.index("4")) # Valueerror

# 2 - Im folgenden Beispiel-Code sollst du dir überlegen, mit Hilfe welcher String-Methoden die Strings so transformiert werden können wir rechts im Kommentar dargestellt

# Beispiel:

# "ApPle" # "apple" --> "ApPle".lower()


"aPpLe"       # apple -> .lower()
"passw0r7"    # PASSW0R7 -> .upper()
"Anime"       # 000000Anime -> .zfill(11)
"florian"     # Florian -> .capitalize()
"Kaguya"      # kaguya -> .lower()
"0123456789"  # 9876543210 -> [::-1]