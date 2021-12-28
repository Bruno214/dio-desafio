from math import prod

# subProgramação

# função que se repete no código para as entradas dos valores


def entradas(list_valores):
    # esse for transforma os valores que são do tipo string para inteiro
    for i in list_valores:
        # corrigindo um possivel espaço no final da sequência
        if i != '':
            v = float(i)
            lista_valores.append(v)  # armazena numa lista inicialmente vazia , para ser subtraídos
    return lista_valores


# Programa Principal

print("Seja bem Vindo!!")
print("\nDigite [ 1 ] para somar!")
print("Digite [ 2 ] para subtrair!")
print("Digite [ 3 ] para multiplicar!")
print("Digite [ 4 ] para Dividir!\n")

opcao = int(input("Escolha uma opção: "))

lista_valores = []

if opcao == 1:
    print("Digite os valores conforme o exemplo 10+10+10 e tecle enter ao final da lista de valores ")
    valores = input().split("+")
    entradas(valores)
    soma = sum(lista_valores)
    print("A soma dos valores é: " + str(soma))

elif opcao == 2:
    print("Digite os valores conforme o exemplo 10-10-10 e tecle enter ao final da lista de valores ")
    valores = input().split("-")
    entradas(valores)
    subtracao = lista_valores[0]  # recebe o primeiro valor no vetor

    # Varre o vetor ate seu tamanho e vai subtraindo, e subtracao recebe o resultado
    for i in range(1, len(lista_valores)):
        resultado = subtracao - lista_valores[i]
        subtracao = resultado

    print(f"A subtração dos valores é: {subtracao}")

elif opcao == 3:
    print("Digite os valores conforme o exemplo 10*10*10 e tecle enter ao final da lista de valores ")
    valores = input().split("*")

    entradas(valores)
    print("A multiplicação dos valores é: " + str(prod(lista_valores)))

elif opcao == 4:
    print("Digite os valores conforme o exemplo 10+10+10 e tecle enter ao final da lista de valores ")
    valores = input().split("/")

    entradas(valores)
    divisao = lista_valores[0]
    for i in range(1, len(lista_valores)):
        resultado = float(divisao / lista_valores[i])
        divisao = resultado
    print("Sua divisão deu: " + str(divisao))
else:
    print("Entre com um número valido!! \nO programa será fechado")
