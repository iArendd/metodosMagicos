class magicInitStr:

    def __init__(self):
        self.pessoas = ['Matheus', 'Caio', 'Marcos', 'João', 'Felipe']

    '''1 - Possibilita retornar os elementos de uma list quando a class é atribuida à alguma variável'''
    def __str__(self):
        return f'magicInitStr(pessoas = {self.pessoas})'

x = magicInitStr()
print('\nResultado do magicInit e magicStr: ')
print(x)

#---------------------------------------------------------------------------------------

class magicGetItemLen:

    def __init__(self):
        self.pessoas = ['Matheus', 'Caio', 'Marcos', 'João', 'Felipe']

    '''2 - Possibilita pegar os elementos de uma list através do índice indicado quando é atribuido a uma variável'''
    def __getitem__(self, posicao):
        return self.pessoas[posicao]

a = magicGetItemLen()
print('\nResultado do magicGetItem: ')
print(a[0])

#---------------------------------------------------------------------------------------

class magicLen:

    def __init__(self):
        self.pessoas = ['Matheus', 'Caio', 'Marcos', 'João', 'Felipe']

    '''3 - Possibilita mostrar o tamanho de uma list de uma class criada pelo programador'''
    def __len__(self) -> int:

        w = 0

        while True:
            try:
                conta = self.pessoas[w]
                w += 1

            except:
                break

        return w

w = magicLen()
print('\nResultado do magicLen: ')
print(len(w))

#---------------------------------------------------------------------------------------

class magicAdd:

    def __init__(self):
        self.pessoas = ['Matheus', 'Caio', 'Marcos', 'João', 'Felipe']

    '''4 - Permite que uma list seja concatenada com outra list'''
    def __add__(self, p2):
        return self.pessoas + p2

i = magicAdd()
print('\nResultado do magicAdd: ')
print(i + ['Claudio', 'Luiz'])

#---------------------------------------------------------------------------------------

class magicMul:

    def __init__(self):
        self.pessoas = ['Matheus', 'Caio', 'Marcos', 'João', 'Felipe']
    
    '''Permite multiplicar uma list'''
    def __mul__(self, n):
        return self.pessoas * n

j = magicMul()

print('\nResultado do magicMul: ')
print(j * 2)

#---------------------------------------------------------------------------------------

class magicDelItemIndice:

    def __init__(self):
        self.pessoas = ['Matheus', 'Caio', 'Marcos', 'João', 'Felipe']
        
    def __delitem__(self, n):
        del self.pessoas[n]

        return self.pessoas


p = magicDelItemIndice()
print('\nResultado do magicDelItem - Indice: ')
print(p)
    