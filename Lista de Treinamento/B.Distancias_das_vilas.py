'''
Problem Statement

O mapa do Minecraft é composto de blocos cúbicos em uma relação de igualdade com o sistema métrico, assim, cada aresta dos blocos tem 1 metro. Dessa forma, é possível identificar localidades por triplas de coordenadas X, Y, Z, na qual X representa a longitude, Y representa a elevação em blocos e Z representa a latitude.

Para simplificar a comunicação, é comum se referir a localidades apenas no plano da superfície do mapa, utilizando apenas as coordenadas X e Z, referindo-se ao ponto no X e Z informados e no Y do ponto da superfície.

Para definir distâncias entre duas localidades é utilizada a fórmula de distância euclidiana, na qual o Y das duas coordenadas pode ser omitido para definir apenas a distância nas duas dimensões. A fórmula de distância euclidiana é:

    D² = (X1 - X2)² + (Z1 - Z2)²

Para entregar os ferros para as vilas, Tantan precisaria saber quais as distâncias da sua localidade para cada vila, podendo se programar em suas viagens. Nas anotações de Tantan, as vilas estavam associadas as seguintes coordenadas:

    Hogsmeade (X: 34, Y: 110, Z: 220)
    Kakariko (X: 0, Y: 64, Z: 0)
    Solitude (X: 140, Y: 200, Z: 456)

Sua tarefa é, baseado nas coordenadas atuais de Tantan, listar as distâncias para cada uma das vilas.
'''
def distancia_euclidiana(x_origem, z_origem, x_destino, z_destino):
    distancia = (((x_origem - x_destino) ** 2) + ((z_origem - z_destino) ** 2)) ** 0.5

    return distancia

# coordenadas (x,z) das vilas
vilas = {"hogsmeade":(34, 220), "kakariko":(0, 0), "solitude":(140, 456)}

# solicitando as coordenadas atuais
x_atual, z_atual = int(input()), int(input())

for vila, coordenadas in vilas.items():
    x_vila, z_vila = coordenadas[0], coordenadas[1]
    distancia = distancia_euclidiana(x_atual, z_atual, x_vila, z_vila)
    print(f"Distancia para {vila}: {distancia:.2f}")
