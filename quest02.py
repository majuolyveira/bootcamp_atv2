def numeros_primos(lista):
    def eh_primo(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primos = [num for num in lista if eh_primo(num)]
    return primos

numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
primos = numeros_primos(numeros)
print("Números primos na lista:", primos)
