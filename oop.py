from pers import Personagem

# Classe: int, str ✅
# Metodo: upper() ✅
# Atributos: __doc__ ✅
# Objeto: tudo em python basicamente ✅
# Instancia: quando declaramos uma variavel ✅
# Polimorfismo ✅
# Herança ✅
# Abstração ✅
# Encapsulação ✅
# Decoradores ✅

# ---------------------------

gato = Personagem("Gato", 5, 1, 0.5)

class Inimigo(Personagem):
    agressivo = True

    def __str__(self):
        return f"❤   {self.vida} pontos de vida \
			   \n💪  {self.forca} pontos de força \
			   \n📅  {self.idade} anos \
			   \n{'👿  agressivo' if self.agressivo else '😇  pacifico'}"

class Jogador(Personagem):
    """Este é um personagem especial para os jogadores de nosso jogo."""
    pass

malgato = Inimigo("Gato 👿", 5, 2, 1)

jogador = Jogador("Astolfo", 20, 4, 8)

inimigo = Inimigo("Goblin", 8, 2, 7)

jogador.combate(inimigo)
# O jogador vai iniciar o combate contra inimigo

#inimigo.combate(jogador)
# O inimigo vai iniciar o combate contra jogador

int