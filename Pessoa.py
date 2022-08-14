class Pessoa:

    def __init__(self):
        self.pessoas = ['Matheus', 'Caio', 'Marcos', 'João', 'Felipe']

    '''1 - Possibilita retornar os elementos de uma list quando a class é atribuida à alguma variável'''
    def __str__(self):
        return f'Pessoa(pessoas = {self.pessoas})'

    '''2 - Possibilita pegar os elementos de uma list através do índice indicado quando é atribuido a uma variável'''
    def __getitem__(self, posicao):
        return self.pessoas[posicao]

    '''3 - Possibilita mostrar o tamanho de uma list de uma class criada pelo programador'''
    def __len__(self) -> int:

        tam = 0

        while True:
            try:
                conta = self.pessoas[tam]
                tam += 1

            except:
                break

        return tam

x = Pessoa()
print(x[0])

tam = Pessoa()
print(len(tam))

#---------------------------------------------------------------------------------------

class Pessoa2:

    def __init__(self):
        self.pessoas2 = ['Matheus', 'Caio', 'Marcos', 'João', 'Felipe']

    '''4 - Permite que uma list seja concatenada com outra list'''
    def __add__(self, p2):
        return self.pessoas2 + p2

i = Pessoa2()
print(i + ['Claudio', 'Luiz'])