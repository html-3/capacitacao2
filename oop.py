# visto que temos o arquivo no mesmo nível do diretorio, podemos importar a classe desta forma
from pers import Personagem

# Pauta da Segunda Capacitação

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

# instanciamos da classe Personagem
gato = Personagem("Gato", 5, 1, 0.5)

# exemplo de herança 
class Inimigo(Personagem):
    """Este é um personagem especial para os inimigos 👿 de nosso jogo."""
    agressivo = True

    # exemplo de polimorfismo (mudamos o método __str__ da classe Personagem)
    def __str__(self):
        return f"❤   {self.vida} pontos de vida \
			   \n💪  {self.forca} pontos de força \
			   \n📅  {self.idade} anos \
			   \n{'👿  agressivo' if self.agressivo else '😇  pacifico'}"

class Jogador(Personagem):
    """Este é um personagem especial para os jogadores 🎮 de nosso jogo."""
    pass