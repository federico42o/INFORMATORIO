"""Determinar la suma de los cuadrados de los n primeros numeros"""


n_numeros = int(input("definir el valor de n: "))
for n in range(1, n_numeros+1):
    sumat = (n*(n+1)*((2*n)+1))//6
print(sumat)

