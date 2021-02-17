

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

  def soma(x,y):
      return x + y
  print(soma(2,2)) #tudo no python é objeto
  print(soma.__doc__) #explica o que esta dentro da função e alocação de memoria
  print(help(soma)) #tbm explica se estiver escrito dentro da função """
  
