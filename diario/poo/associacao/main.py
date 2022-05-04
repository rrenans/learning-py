
from escritor import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Renan')
caneta = Caneta('bic')
maquina = MaquinaDeEscrever()
# tudo que está dentro da classe caneta está indo para o atributo de ferramenta na classe escritor
escritor.ferramenta = caneta 
escritor.ferramenta.escrever()
print()