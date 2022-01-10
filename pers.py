

class Personagem:
    """Este é um personagem, o objeto mais básico de nosso RPG."""
    natalidade = 'Ilhas Brusil'

    # self signifa o objeto
    # o resto são variáveis que a função __init__ (função construtora) recebe
    def __init__(self, nome, vida, forca, idade):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.idade = idade

    # função dunder str para retornar as qualidades do objeto de forma mais clara
    def __str__(self):
        return  f"❤   {self.vida} pontos de vida \
		       \n💪  {self.forca} pontos de força  \
		       \n📅  {self.idade} anos"

    # abstração de um ataque encapsulado na classe Personagem
    def ataque(self, defensor):
        defensor.vida -= self.forca

    # abstração de um combate encapsulado na classe Personagem
    def combate(self, per2):

        while True:
            
            self.ataque(per2)

            if per2.vida <= 0:
                print(f"{ per2.nome } desistiu do combate!")
                break
            
            per2.ataque(self)

            if self.vida <= 0:
                print(f"{ self.nome } desistiu do combate!")
                break
