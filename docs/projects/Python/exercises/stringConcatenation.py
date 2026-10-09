# 1 - Was wird von dem folgenden Programm ausgegeben? Gib, wenn es zu einem Fehler kommt, an, welcher Fehler auftritt und warum.
a = "Developer"
b = "Akademie"
c = '.'
d = "com"

print(a + b) # DeveloperAkademie
print(a + b + c + d) #DeveloperDeveloperAkademie.com
#print(a + b - b) # type error
print(5 * c) #.....
#print(3d) # typeerror
print(a + d) # Developercom
print(a + b + d) # DeveloperAkademiecom
#print(d**2) # typeerror
print(2 * (c + d)) # .com.com
print(3 * c + 2 * d) #...comcom