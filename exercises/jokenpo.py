"""Make a two-player Rock-Paper-Scissors game."""

import os
import time

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def rps(text):
    pedra = set(['pedra', 'pe', 'pdra', 'pedr', "1"])
    papel = set(['papel', 'pap', "2", 'pape', 'ppel', 'pa', 'papl'])
    tesoura = set(['tesoura', 't', "3", 'tsoura', 'tesora'])
    while True:
        choice = input(text).lower()
        if choice in pedra:
            input("\nVocê escolheu pedra, boa sorte! Pressione qualquer tecla para continuar.")
            return "pedra"
        if choice in papel:
            input("\nVocê escolheu papel, boa sorte! Pressione qualquer tecla para continuar.")
            return "papel"
        if choice in tesoura:
            input("\nVocê escolheu tesoura, boa sorte! Pressione qualquer tecla para continuar.")
            return "tesoura"
        print("Por favor, insira o valor correspondente.")

def game(input1, input2):
    if input1 == input2:
        print("Parece que houve um empate! Ambos jogaram", input1)
    elif input1 == "pedra":
        if input2 == "tesoura":
            ganhador(p1)
        else:
            ganhador(p2)
    elif input1 == "papel":
        if input2 == "pedra":
            ganhador(p1)
        else:
            ganhador(p2)
    elif input1 == "tesoura":
        if input2 == "papel":
            ganhador(p1)
        else:
            ganhador(p2)

def ganhador(p):
    print("O jogador {0} jogou {1} e o jogador {2} jogou {3}!\n\nO vencedor é {4}!"
           .format(p1, i1, p2, i2, p))

cls()

print("Jokenpô!")
p1 = input("\nInsira o nome do primeiro jogador: ")
p2 = input("\nInsira o nome do segundo jogador: ")

cls()

print("Vamos jogar! Por favor, vire a tela para", p1)
i1 = rps("\nVai jogar com pedra, papel ou tesoura? ")

cls()

print("Agora vire a tela para", p2)
i2 = rps("\nVai jogar com pedra, papel ou tesoura? ")

cls()

p = game(i1, i2)
