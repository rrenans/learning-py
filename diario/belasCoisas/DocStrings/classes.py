"""
Descrição rápida e simples.

Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type
specimen book. It has survived not only five centuries, but also the leap into
electronic typesetting, remaining essentially unchanged. It was popularised in
the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop publishing software like Aldus PageMaker
including versions of Lorem Ipsum.
"""

class MinhaClasse:
    """Documentação normal

    Conforme qualquer outra documentação que você tenha usado anteriormente.
    """
    atributo = 1
    atributo2 = 'Valor'

    def __init__(self, texto):
        """Inicializa os dados
        
        :param texto: o texto da classe
        :type texto: str
        """
        self.texto = texto
        self.exibe_texto(texto)

    @staticmethod
    def exibe_texto(texto):
        """Método que exibe um texto de 100 caracteres na tela
        
        :param texto: Um texto de 100 caracteres
        :type texto: str

        :return: O texto de 100 caracteres
        :rtype: str

        :raises ValueError: Se o texto tiver mais que 100 caracteres
        :raises TypeError: Se o texto não for uma string
        """
        if not isinstance(texto, str):
            raise TypeError('Texto precisa ser uma string.')
        
        if len(texto) > 100:
            raise ValueError('Texto precisa ter 100 caracteres ou menos')

        return texto