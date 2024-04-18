def segundo_maior(lista):
    
    if len(lista) < 2:
        return None  

    maior = max(lista[0], lista[1])
    segundo_maior = min(lista[0], lista[1])

    for num in lista[2:]:
        if num > maior:
            segundo_maior = maior
            maior = num
        elif num > segundo_maior:
            segundo_maior = num

    return segundo_maior

numeros = [10, 5, 8, 20, 15]
segundo = segundo_maior(numeros)
print("O segundo maior número na lista é:", segundo)
