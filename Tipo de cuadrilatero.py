a = input ("Digite el numero: ")
b = input ("Digite el numero: ") 
c = input ("Digite el numero: ") 
d = input ("Digite el numero: ")

if a == b and c == d:
    print ("Es un cadrado")
elif a == c and  b == d :
    print (" Es un rectangulo")
elif a == b == c or b == a == d or a == c == d or a == c == d:
    print ("Es un cuadrilatero")
else:
    print ("Es un cuadrilatero")
