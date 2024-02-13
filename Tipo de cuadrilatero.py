a = float
b = float
c = float
d = float

a = input ("Digite el numero: ")
b = input ("Digite el numero: ") 
c = input ("Digite el numero: ") 
d = input ("Digite el numero: ")

if a == b == c == d:
    print ("Es un cuadrado")
elif a == c and  b == d or a == b  and c == d:
    print (" Es un rectangulo")
else:
    print ("Es un cuadrilatero")


