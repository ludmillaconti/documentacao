"""
1 - Funções noemadas (def)
2 - Funções anonimas (lambda)
3 - Funções de classe (class)
"""

def nomeada_soma(x + y):
    return x + y

 anonima_soma = lambda x,y:  x + y #não tem return na lambda

 class classe_soma:
     def __init__(self, x, y):
         self.x = x #vai receber x
         self.y = y # vai receber y

     def __call__(self):
         return self.x + self.y


  """
Funções nomeadas (padrões)
  """

  def soma(x,y): #()-> argumentos ou parametros
      return x + y
  print(soma(2,2)) #tudo no python é objeto
  print(soma.__doc__) #explica o que esta dentro da função e alocação de memoria
  print(help(soma)) #tbm explica se estiver escrito dentro da função """

"""
Funções anonimas / não se deve nomear lambdas
"""

r = (lambda x: x + 2(2)) #função declara e executada ao mesmo tempo
print(r) #4

soma_2 = lambda x: x+2
print(soma_2(2)) #()dentro do soma_2 é o parametro

#quando usar função lambdas

print(list(map(lambda x: x+2, [1,2,3])))
#colocar a função dentro de uma lista pra ser vizualizavel
#map

"""
Função classe
"""
 class classe_soma:
     def __init__(self, x, y):
         self.x = x #vai receber x
         self.y = y # vai receber y

     def __call__(self):
         return self.x + self.y


print(classe_soma(2,2)) #não funciona pq precisa ser definida como um objeto

a=classe_soma(2,2)
print(a()) #()-> chamar




 class classe_soma:
     def __call__(self, x, y): #não funciona pq a função precisa ser iniciada __init__
         return x + y

print(classe_soma(2,2)) #()-> chamar



"""
Funções não compartilham escopo global
"""

from pdb import set_trace

var =7

def func():
    print(var)

func() #tem que chamar a função se vc não colocar o return

##########################################################
#locals() função interna do python que pega tudo da função local
#global() tudo que a funções enxerga no contexto global

def func():
    #set_trace()
    var = 18 #como é definido dentro da função ele é local
    print(var)

func() #tem que chamar a função se vc não colocar o return
print(var)
#printa o 18 e depois o 7

############################################################

def func():
    global var
    print(var)
    #set_trace()
    var = 18 #como é definido dentro da função ele é local
    print(var)

func() #tem que chamar a função se vc não colocar o return
print(var)
#printa o 7, 18 e 18


"""
Closure = função dentro de uma função
Precisa chamar a função externa para a interna funcionar
"""

from pdb import set_trace

def externa():
    #set_trace()
    def interna():
        print(42)
    return interna()

externa() #funciona

##############################################################

def externa():
    #set_trace()
    def interna():
        print(42)
    return interna

func = externa()
func() # tbm funciona

##############################################################

#quero escrever ola, ahoy, hello

"""
Fixa uma função principal para varias saidas
"""

def externa(id):
    dict = {'pt': 'olá', 'pi': 'ahoy', 'in': 'hello'}

    def interna(nome):
        print('{} {}'.format(dict[id], nome))
    return interna

func = externa('pt')
func('pedro')
#printa olá, pedro


"""
Decorador - padrão de projeto
"""

def decorador(teste):
    print(teste.__name__)
    def interna():
        pass
    return interna()


@decorador
def soma(x,y):
    return x+y

#decorador(soma(2,2))

print(soma(2,2))

########################################################

def decorador(func):
    def interna(x, y): #recebe argumentos da funçao soma
        print(x,y)
    return interna()

"""
decorador -> chama função interna -> chama a função decorada
"""

@decorador
def soma(x,y):
    return x+y

#decorador(soma(2,2))

print(soma(2,2))
#printa 2 2

###########################################################

def decorador(func): #função soma aqui de baixo
    def interna(x, y):
        x = x*2
        y = y*2
        return func(x,y)
    return interna


@decorador
def soma(x,y):
    return x+y


print(soma(2,2))
#printa 8

###########################################################

from inspect import getargvalues #argumentos passados pra essa função e calcula valores

from inspect import signature

signature(soma)
#printa os argumentos


def decorador(func): #função soma aqui de baixo
    def interna(x, y):
        if isinstance(x, int) and isinstance(y, int):
            return func(x,y)
        else:
            raise ValueError('insira numeros inteiros')
    return interna


@decorador
def soma(x,y):
    return x+y

def div(x, y):
    return x/y


print(soma(2,'paulo'))
#da o erro falando que é pra inserir somente inteiros

##############################################################

"""
decorador mais complexo
"""


def decorador(argumentos_decorador):
    print(argumentos_decorador)
    """
    parametros do decorador
    """
    def decorador_real(func):
        print(func.__name__)
        """
        recebe a função
        """
        def execute_function(argumentos_funcao):
            """
            executa a função
            """
            print(argumentos_funcao)
            pass
        return execute_function
    return execute_real


@decorador('anderson')
def soma(x,y):
    return x+y


soma(2,2)

###############################################################

from flask import Flask

app = Flask(__name__) #flask recebe uma rota que é a /, decora uma função e
#retorna na pagina web

@app.route('/')
def index():
    return 'ola live' #pagina principal home

@app.route('/live')
def live_page():
    return 'estamos online' #pagina secundaria

app.run() #retorna uma página da web
