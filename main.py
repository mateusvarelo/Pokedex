from view import PokedexView
from art import *

print(text2art('''{"Pokedex": "Pi"} ''', font="amall"))

print(
    "Digite um número entre 1 e 27 (Corresponde a um local onde você poderá"
    " encontrar um  pokémon) "
    )
aprint("happ") 

numero_local = input(":") 

print("Qual tipo de arquivo 1(CSV) ou 2-(JSON):") 

tipo = int(input(":"))  

pokemon = PokedexView()
pokemon.pesquisar_pokemon(numero_local,tipo)

print(pokemon.resposta())