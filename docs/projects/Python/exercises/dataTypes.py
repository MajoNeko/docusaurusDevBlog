# 1 - Welche der folgenden Umwandlungen sind möglich und was ist das Ergebnis?
int(42.5) #42
float(-1) #-1.0
str(0.5) #"0.5"
bool(0.001) #True
str("False") #"False"
int(False) #0
float("10") #10.0
bool('0') #True
#int("False") #invalid
#float("True") #invalid

# 2 - Wie kannst du den Datentyp einer Variable in Python bestimmen?
print(type(int(42.5)))