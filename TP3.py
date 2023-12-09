''''1. Defina uma função recursiva para o cálculo de potência de dois números inteiros,
onde o primeiro número é elevado ao segundo. Não se pode usar o operador de
potência ( ** ) do python'''

def potencia(base, expoente):
    if expoente == 0:
        return 1 if base != 0 else 0
    else: #Caso recursivo: base elevada ao expoente é a base multiplicada pela base elevada ao expoente menos 1
        return base * potencia(base, expoente - 1) 
   
print("Saída 1) " ,potencia(2,3))

'''2. Calcular o somatório dos elementos ímpares de uma lista de inteiros'''

def soma_impares(lista):
    if not lista:
        return 0
    else: # Caso recursivo: soma o primeiro elemento ímpar com a soma dos ímpares restantes
        primeiro_elemento = lista[0]
        if primeiro_elemento % 2 != 0:
            return primeiro_elemento + soma_impares(lista[1:])
        else:
            return soma_impares(lista[1:])

# Soma dos ímpares de 1 a 9        
lista_2 = [i for i in range(1,10)]
print("\nSaída 2) Soma dos Impares de 1 a 9 :" ,soma_impares(lista_2))

'''3. Substituir todos elementos de um determinado valor de uma lista de inteiros por
um outro valor.'''

def substituir(valor_antigo, valor_novo, lista):
    if not lista:
        return []
    else:  # Caso recursivo: substitui o valor antigo pelo valor novo no primeiro elemento e continua com o resto da lista
        primeiro_elemento = lista[0]
        if primeiro_elemento == valor_antigo:
            return [valor_novo] + substituir(valor_antigo, valor_novo, lista[1:])
        else:
            return [primeiro_elemento] + substituir(valor_antigo, valor_novo, lista[1:])
        
lista_3 = [10, 92, 10, 92, 10]
print("\nSaída 3) " ,substituir(10, 0, lista_3))

'''4. Verificar se um número é primo''' #Teste de primalidade de Fermat

def Fermat(n, divisor=2):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    elif divisor * divisor > n: # Caso recursivo: verifica divisibilidade a partir do divisor 5
        return True
    elif n % divisor == 0 or n % (divisor + 2) == 0:
        return False
    else:
        return Fermat(n, divisor + 6)

num_1 = 92
num_2 = 17
print("\nSaída 4)")    
print(num_1, " é primo? -> " ,Fermat(num_1))
print(num_2, " é primo? -> " ,Fermat(num_2))

'''5. Criar uma função que retorna uma lista com a representação em binário de um
número inteiro'''

def binario_lista(numero):
    if numero == 0:
        return [0]
    elif numero == 1:
        return [1]
    else: # Caso recursivo: divide o número por 2 e continua chamando a função recursivamente
        return binario_lista(numero // 2) + [numero % 2] # sem divisão truncada não funciona

passar_para_binario = 6
lista_binario = binario_lista(passar_para_binario)

print("\nSaída 5) ",lista_binario)

'''6. Criar uma função que verifica se um número é perfeito — isto é — se o número é
igual a soma de seus divisores (exceto o próprio número)'''

def soma_divisores(n, divisor=1):
    if divisor >= n:
        return 0  
    elif n % divisor == 0: #Caso recursivo: Se for uma divisão perfeita, soma o divisor com o retorno da função incrementando 1 no divisor
        return divisor + soma_divisores(n, divisor + 1)
    else:
        return soma_divisores(n, divisor + 1)

def Verifica_perfeito(numero):
    return soma_divisores(numero) == numero

perfeito = 28
print("\nSaída 6) ")
print(perfeito, " é um número perfeito: ", Verifica_perfeito(perfeito))

'''7. Verificar se todos os elementos de uma lista são distintos'''

def sao_distintos(lista):
    if len(lista) <= 1:
        return True
    elif lista[0] in lista[1:]: # Caso recursivo: verifica se o primeiro elemento está presente no resto da lista
        return False
    else:
        return sao_distintos(lista[1:])
    
lista_distintos = [i for i in range(1,6)]
lista_distintos2 = [i for i in range(1,6)] + [1]

print("\nSaída 7) ")
print("Os itens da lista ", lista_distintos, " são distintos: ", sao_distintos(lista_distintos))
print("Os itens da lista ", lista_distintos2, " são distintos: ", sao_distintos(lista_distintos2))

'''8. Verificar se duas listas são disjuntas'''

def sao_disjuntas(lista1, lista2):
    if not lista1 or not lista2:
        return True
    elif lista1[0] in lista2: # Caso recursivo: verifica se o primeiro elemento de lista 1 está presente na lista 2
        return False
    else: # se não, continua verificando o resto
        return sao_disjuntas(lista1[1:], lista2)
    
lista_disjuntos = [i for i in range(1,6)]
lista_disjuntos2 = [i for i in range(6, 11)]

print("\nSaída 8) ")
print("Os itens das listas ", lista_disjuntos, " e ",lista_disjuntos2, " são disjuntos: ", sao_disjuntas(lista_disjuntos, lista_disjuntos2))

'''9. Verificar se uma lista de inteiros é um palíndromo'''

def palindromo(lista):
    if len(lista) <= 1:
        return True
    elif lista[0] == lista[-1]: # Caso recursivo: verifica se o primeiro e último elementos são iguais
        return palindromo(lista[1:-1])
    else:
        return False
    
lista_palindromo = [i for i in range(1,4)] + [2,1]
print("\nSaída 9) ")
print("A lista ", lista_palindromo, " é um palíndromo: ", palindromo(lista_palindromo))

'''10. Realizar todas a somas parciais de uma lista de inteiros'''

def somas_parciais(lista, index=0, soma_atual=0, lista_resultante=[]):
    if index == len(lista):
        return lista_resultante
    else: # Caso recursivo: Calcula as somas parciais incluindo o próximo elemento e chama recursivamente com o próximo índice
        lista_resultante.append(soma_atual + lista[index])
        return somas_parciais(lista, index + 1, soma_atual + lista[index], lista_resultante)

lista_soma = [i for i in range(1,5)]
print("\nSaída 10) ")
print("A soma parcial dos elementos da lista ", lista_soma, " é: ", somas_parciais(lista_soma))


'''11. Linearizar uma lista de listas de inteiros'''

def linearizar_listas(listas, resultado=[]):
    if not listas:
        return resultado
    else: # Caso recursivo: Adiciona os elementos da primeira lista à lista resultado e chama recursivamente com o restante das listas
        resultado.extend(listas[0])
        return linearizar_listas(listas[1:], resultado)
    
lista_de_listas = [[1,2], [3,4], [5,6,7,8], [9]]
print("\nSaída 11) ")
print("Lista ", lista_de_listas, " linearizada: ", linearizar_listas(lista_de_listas))

'''12. Deslocar elementos de uma lista de inteiros k posições para a esquerda'''

def desloca(lista, k):
    if k > len(lista):
        return "k é maior que o tamanho da lista"
    else:
        nova_lista = lista[k:] + lista[:k]
        return nova_lista

lista_deslocar = [1, 5, 6, 7, 3, 4, 1]
k = 3

print("\nSaída 12) ")
print("Lista ", lista_deslocar, " deslocada ", k, " posições à esquerda: ", desloca(lista_deslocar, k))

'''13. Remover os ultimos n elementos de uma lista de inteiros'''

def remover_ultimos(lista, n):
    if n >= len(lista):
        return []
    elif n == 0:
        return lista
    else:
        return lista[:-n]
    
lista_remover = [i for i in range(1,11)]
n = 3
print("\nSaída 13) ")
print("Removendo os ultimos ", n, " números da lista ", lista_remover, " : ", remover_ultimos(lista_remover, n))

'''14. Dadas duas listas ordenadas de forma crescente, obter a lista ordenada da intercalação delas'''

def concatena_ordenado(lista1, lista2, resultado=[]):
    if not lista1 and not lista2:
        return resultado
    elif not lista2:
        resultado.extend(lista1)
        return resultado
    elif not lista1:
        resultado.extend(lista2)
        return resultado
    else:
        if lista1[0] < lista2[0]:
            resultado.append(lista1[0])
            return concatena_ordenado(lista1[1:], lista2, resultado)
        else:
            resultado.append(lista2[0])
            return concatena_ordenado(lista1, lista2[1:], resultado)
        
lista_concat1 = [1, 3, 5, 7]
lista_concat2 = [2, 4, 6, 8, 9]
print("\nSaída 14) ")
print("Listas ", lista_concat1, " e ", lista_concat2, " concatenadas em ordem crescente: ", concatena_ordenado(lista_concat1, lista_concat2))

'''15. Trocar dinheiro'''

def trocar(valor, cedulas_disponiveis=[100, 50, 10, 5, 1], resultado=[]):
    if valor == 0:
        return resultado
    elif valor < 0 or not cedulas_disponiveis:
        return []
    else:
        cedula_atual = cedulas_disponiveis[0]
        quantidade_cedulas = valor // cedula_atual # quantas cédulas daquele valor vão fazer parte do troco
        resultado.extend([cedula_atual] * quantidade_cedulas)
        novo_valor = valor % cedula_atual # novo valor a ser trocado considerando a cédula anterior
        return trocar(novo_valor, cedulas_disponiveis[1:], resultado) # Chama recursivamente a função com o novo valor e a lista de cédulas restantes
    
valor_trocar = 162
trocado = trocar(valor_trocar)
print("\nSaída 15) ")
print("Trocar R$", valor_trocar, " : ", trocado[::-1])