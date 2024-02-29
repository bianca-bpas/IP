'''
Problem Statement

Quantidade de diamantes é uma boa forma de medir riqueza no Minecraft pois é um dos recursos minerais mais difícil de ser encontrado e minerado no mapa.

Arthur, Luiz e Pedro decidiram fazer uma competição no Minecraft, para decidir quem iria escolher qual brega que irá tocar durantes suas longas noites de programação no CIn e pediram ajuda de Tantan para disponibilizar suas vilas como moradia para cada um. Foi combinado que a competição iria ser realizada dentro do jogo, na qual cada participante iria criar um mundo do zero e teria que encontrar o máximo de diamantes no tempo definido.

Para deixar a competição mais divertida, eles combinaram que cada um iria definir uma restrição para o programa que computaria qual o maior valor de diamantes encontrado pelos participantes.

Luiz definiu que o programa não poderia utilizar nenhuma estrutura condicional em seu código, como IF e outras;
Pedro proibiu a utilização de quaisquer funções de bibliotecas externas para calcular o máximo da quantidade de diamantes do vencedor;
Arthur falou que, para encontrar o valor final da quantidade máxima de diamantes, seria obrigatório utilizar a seguinte função para encontrar o máximo entre 2 valores: x = (a + b + (|a - b|)) / 2.
Visando deixar a solução mais simples, Arthur e Pedro chegaram a um acordo e decidiram que seria permitido utilizar funções externas para calcular o valor absoluto de um número (abs(), em Python).

Sua tarefa é escrever o programa que vai auxiliar os três a descobrir o vencedor da competição, em acordo com todas as restrições.
'''

def maior_valor(valor1, valor2):
    maior = (valor1 + valor2 + (abs(valor1 - valor2))) / 2
    return maior
    
# quantidade média de diamantes obtidos por hora
diamantes_coletados = (int(input()) , int(input()), int(input()))

# duração da competição em horas
duracao = int(input())

# calculando o maior valor obtido
contador = 1
while contador <= len(diamantes_coletados)-1:
    maior = diamantes_coletados[0]
    maior = maior_valor(maior, diamantes_coletados[contador])
    contador += 1

# valor máximo de diamantes obtido na competição
diamantes_maximo = maior * duracao
print(f"{diamantes_maximo:.0f}")
