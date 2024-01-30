with open('afn2.txt', 'r') as file:
    alfabeto = file.readline().replace(
        'alfabeto=', '').replace('\n', '').lstrip().split(',')
    estados = file.readline().replace(
        'estados=', '').replace('\n', '').lstrip().split(',')
    estado_inicial = file.readline().replace(
        'inicial=', '').replace('\n', '').lstrip().split(',')
    estado_final = file.readline().replace(
        'finais=', '').replace('\n', '').lstrip().split(',')
    file.readline()

    transicao = {}

    while True:
        transicoes = file.readline().replace('\n', '').lstrip().split(',')
        if transicoes != ['']:
            if len(transicoes) > 3:
                transicao.update(
                    {(transicoes[0], transicoes[3]): [transicoes[1],transicoes[2]]})
            if len(transicoes) > 4:
                transicao.update(
                    {(transicoes[0], transicoes[4]): [transicoes[1],transicoes[2],transicoes[3]]})
            if len(transicoes) > 5:
                transicao.update(
                    {(transicoes[0], transicoes[5]): [transicoes[1],transicoes[2],transicoes[3],transicoes[4]]})
            else:
                transicao.update(
                    {(transicoes[0], transicoes[2]): [transicoes[1]]})
        if transicoes == ['']:
            break

cadeia = input('Entre com a cadeia desejada: ')

atual = estado_inicial

def checaEpsilon (alfab):
    for simbolo in alfab:
        if simbolo == 'epsilon':
            return True
    return False

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

temEpsilon = checaEpsilon(alfabeto)

#Fica no loop até dar break

for simbolo in cadeia: #analisa cada elemento da cadeia
    if simbolo not in alfabeto: #se elemento analisado não faz parte do alfabeto da cadeia
        print('Simbolo nao reconhecido identificado!')
        atual = [] #atual recebe lista vazia
        break

    prox_estados = [] #prox_estados recebe lista vazia
    for estado in atual: #analisa cadeias atuais (no caso do não determinismo)
        try: #try catch para não dar erro na falta de alguma transição
            prox_estados += transicao[(estado, simbolo)] #atualiza prox_estados com os estados da transição
            if temEpsilon:
                prox_estados += transicao[(estado, 'epsilon')]
        except:
            break
    prox_estados = remove_repetidos(prox_estados)
    print(f'{atual} --{simbolo}--> {prox_estados}')
    atual = prox_estados #atualiza atual com prox_estado
    
#Checa se estados atuais possuem algum estado final, se sim, printa "cadeia aceita", se não, "cadeia rejeitada"
aceitou = False
for verificador1 in estado_final:
    for verificador2 in atual:
        if(aceitou == True):
            break
        elif verificador2 == verificador1:
            print('Cadeia Aceita!')
            aceitou = True
if aceitou == False:
    print('Cadeia Rejeitada!')