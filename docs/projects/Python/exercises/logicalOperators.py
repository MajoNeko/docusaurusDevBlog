# 1 -Welche Wahrheitswerte kommen bei den folgenden logischen Ausdrücken heraus?

print(True and False and True or False) # False
print(not False or not True) #True
print(True and (False or not False)) # True
print(not (not False ^ True or not False)) # False
print(True and False ^ True and False) # False

# 2 - Worin besteht der Unterschied zwischen den beiden Operatoren ^ und or?

# or allows for True or False, True or True and False or True to evaluate to True while ^ (xor) only evaluates to True is only one of the values is True (exclusive or)

# 3 - Welche Wahrheitswerte kommen als Ergebnis heraus?
print(2 < 3 and not 2 > 5) # True
print(not True ^ False or 3 == 2 + 1) # True
print(not not not 2 % 5 == 7 % 5) # False
print(True and False ^ True and False) # False
print(True ^ False ^ 0 ^ 1 ^ (2 > 3)) # False