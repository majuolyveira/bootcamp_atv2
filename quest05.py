def ordenar_por_nome(lista_tuplas):
    return sorted(lista_tuplas, key=lambda x: x[0])



lista_pessoas = [("Maria"), ("João"), ("Ana"), ("Pedro")]
lista_ordenada = ordenar_por_nome(lista_pessoas)
print("Lista ordenada pelo nome das pessoas:", lista_ordenada)
