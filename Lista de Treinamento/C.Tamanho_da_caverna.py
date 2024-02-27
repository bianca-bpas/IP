'''
Problem Statement

Uma das formas de obter recursos minerais no Minecraft é cavando cavernas em baixo da terra e coletando todos os recursos encontrados.

Após escolher seu nickname, Tantan precisa juntar muitos recursos e decide ir minerar. Seu amigo Durval é especialista em mineração e, vendo o mapa, consegue escolher um bom tamanho para a caverna de mineração. Para melhores resultados, a base da caverna sempre é quadrada, com uma altura variante.

Sua tarefa é ajudar Tantan a saber qual o máximo de blocos que ele vai precisar quebrar para cavar a caverna, após Durval informar a dimensão da mesma.
'''
def area(comprimento, largura):
    area = comprimento * largura

    return area

def volume(area, altura):
    volume = area * altura

    return volume

# Recebendo informaçoes de tamanho da caverna
largura, altura = int(input()), int(input())

# Calculando o volume de blocos a ser removido pelo personagem
area = area(largura, largura) # base quadrada
volume = volume(area, altura)
print(volume)
