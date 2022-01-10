from oop import Inimigo, Jogador

# instante da classe Inimigo é um objeto 
malgato = Inimigo("Gato 👿", 5, 2, 1)

jogador = Jogador("Astolfo", 20, 4, 8)

inimigo = Inimigo("Goblin", 8, 2, 7)

jogador.combate(inimigo)
# O jogador vai iniciar o combate contra inimigo

#inimigo.combate(jogador)
# O inimigo vai iniciar o combate contra jogador
