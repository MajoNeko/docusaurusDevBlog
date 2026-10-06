# 1 -Welche der folgenden Variablennamen sind in Python gültig und welche nicht?

#python123 # valid
# 0815 - invalid
#__python__ # valid
#Fehler # valid
#false # valid
#hallo_welt # valid
# True - invalid
# nicht-richtig - invalid
# tmp.2 - invalid
# yield - invalid

# 2 - Gegeben seien die folgenden Variablen:
vorname = "Mustermann"
nachname = "Max"
# Vertausche die Werte der beiden Variablen vorname und nachname, damit der Vor- und Nachname richtig zugewiesen ist.
vorname, nachname= nachname, vorname


# 3 - Gegeben sei das folgende Python-Programm:
a = 42
b = a
c = a
a = 10
b = c
# Welche Werte werden in den folgenden Zeilen ausgegeben?
print(a) #10
print(b) #42
print(c) #42

# 4 - Gegeben sei das folgende Python-Programm:
vorname = "Misa"
nachname = "Amani"
geschlecht = "weiblich"
tag = 22
monat = "September"
jahr = "1998"
print(f"""Mein Name ist {vorname} {nachname}.\nIch bin{geschlecht} und wurde am {tag}. {monat} {jahr} geboren.""")
#output: Mein Name ist Misa Amani.
# Ich binweiblich und wurde am 22. September 1998 geboren.