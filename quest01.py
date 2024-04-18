def numeros_impares(lista):
    impares = [num for num in lista if num % 2 != 0]
    return impares


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
impares = numeros_impares(numeros)
print("Números ímpares na lista:", impares)