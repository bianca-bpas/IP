'''
Problem Statement

Um dos recursos minerais mais úteis do Minecraft é o ferro, pois é abundante no mundo e bom para fazer armas e armaduras. No jogo, a maioria dos itens podem ser agrupados em um conjunto de 64, que é chamado de stack.

Tantan passou alguns dias apenas construindo e finalizou três vilas:

    Hogsmeade
    Kakariko
    Solitude

Como ele já tinha passado bastante tempo minerando e acumulou vários packs de ferro e decidiu dividir todos os packs igualmente entre as vilas. Para ser justo, ele prometeu jogar fora todo o ferro que sobrasse.

Sua tarefa é escrever um programa para mostrar a Tantan como utilizar os seus packs de ferro.
'''

# solicitando a quantidade de packs de ferro
p = int(input())

# calculando os valores de v e f e imprimindo na tela
if (p >= 3): 
    v = (p // 3) # quantidade de packs para cada vila
    f = (p % 3) # quantidade de packs que sobrou apos a divisao
    print(v)
    print(f)
