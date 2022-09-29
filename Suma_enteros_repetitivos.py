# programa 25: Hallar la suma de los primeros 10 numeros enteros por medio de instrucciones repetitivas

print("\n---------------------------------------------------------------------------")
print("--------------Suma de los primeros n numeros enteros ------------------------")
print("---------------------------------------------------------------------------\n")

# input
n=int(input("\n Ingrese la cantidad de enteros a sumar "))

# processing
i=1
s=0

while i<=n:
    s=s+i 
    i=i+1

print("\nLa suma de los "+str(n)+" numeros enteros es: "+str(s))
print(" ")