from dec import data_op

class Personagem:
    natalidade = 'Ilhas Brusil'

    # self signifa o objeto
    # o resto sao variaveis que a funcao __init__ recebe
    def __init__(self, nome, vida, forca, idade):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.idade = idade

    def __str__(self):
        return  f"❤   {self.vida} pontos de vida \
		       \n💪  {self.forca} pontos de força  \
		       \n📅  {self.idade} anos"

    @data_op
    def ataque(self, defensor):
        defensor.vida -= self.forca

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
