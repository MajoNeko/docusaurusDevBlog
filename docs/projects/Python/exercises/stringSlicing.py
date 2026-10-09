# 1 - Was wird von dem folgenden Programm ausgegeben?
a = "Buchhaltung"
b = "Python ist toll!"

print(a[5]) # a
print(b[-1]) # !
print(a[:4]) # Buch
print(b[11:16]) # toll!
print(a[-100:100]) # Buchhaltung
print(a[-5]) # l
#print(a[-12]) # error
print(a[4:8]) # halt


# 2 - Schneide mithilfe von Slicing aus dem String
wort = "Maximilian"

"""
die folgenden Substrings aus:
Max
Maxi
im
mili
ian
"""

print(wort[:3])
print(wort[:4])
print(wort[3:5])
print(wort[4:8])
print(wort[-3:])