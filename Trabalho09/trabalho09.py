from abc import ABC, abstractmethod

class TitErradaProf(Exception):
  #titulação deve ser doutor (Professor)
  pass

class IdadeErradaProf(Exception):
  #idade deve ser igual ou maior que 30 anos (Professor)
  pass

class CursoErrado(Exception):
  #curso deve ser CCO ou SIN(Aluno)
  pass

class IdadeErradaAluno(Exception):
  #idade deve ser igual ou maior que 18 anos.(Aluno)
  pass

class CPFErrado(Exception):
  #nenhuma pessoa do cadastro pode ter o mesmo CPF.
  pass

class Pessoa(ABC):
  def __init__(self, nome, cpf, endereco,idade):   
    self.__nome = nome
    self.__cpf = cpf
    self.__endereco = endereco
    self.__idade = idade

  def getNome(self):
    return self.__nome

  def getCPF(self):
    return self.__cpf

  def getEndereco(self):
    return self.__endereco

  def getIdade(self):
    return self.__idade
  
  @abstractmethod
  def printDescricao(self):
    pass

class Professor(Pessoa):
  def __init__(self, nome, cpf, endreco, idade, titulacao):
    super().__init__(nome, cpf,endreco,idade)
    self.__titulacao = titulacao

  def getTitulacao(self):
    return self.__titulacao

  def printDescricao(self):
    print ('Nome: {} - Endereço: {} - Idade: {} - Titulação: {}'.format(self.getNome(), self.getEndereco(), self.getIdade(), self.__titulacao))

class Aluno(Pessoa):
  def __init__(self, nome, cpf, endreco, idade, curso):
    super().__init__(nome, cpf,endreco,idade)
    self.__curso = curso

  def getCurso(self):
    return self.__curso

  def printDescricao(self):
    print ('Nome: {} - Endereço: {} - Idade: {} - Curso: {}'.format(self.getNome(), self.getEndereco(), self.getIdade(), self.__curso))

if __name__ == "__main__":
  p1 = Professor("Elza Rosa Eloá da Cunha", "642.186.735-94","Travessa Santa Fé",61,"doutor")
  a1 = Aluno("Kaique Marcos Vinicius André da Mata","561.018.866-03","Beco Quarenta",20,"CCO")
  a2 = Aluno("Fernanda Heloisa Gomes","118.542.756-23","Rua José Alves dos Reis 196",19,"SIN")

  #titulação não é doutor
  p2 = Professor("Tânia Lara Luana Gonçalves", "012.122.161-05","Rua Carlos de Lima",30,"nenhuma") 

  #tem menos de 30 anos
  p3 = Professor("Igor Calebe Campos", "920.635.716-60","Rua Cinco",29,"doutor")

  #curso não é CCO, nem SIN
  a3 = Aluno("Edson Lorenzo Teixeira","641.281.575-97","Rua Amadeu Amaral",20,"ADM")

  #idade menor que 18
  a4 = Aluno("Julio Antonio Thomas dos Santos","891.392.610-50","Alameda dos Jatobás",17,"SIN")
  
  #CPF igual da Elza
  p4 = Professor("Lorenzo Pedro Rocha", "642.186.735-94","Rua Mestre Albano",35,"doutor")
  
  dados =[p1,a1,a2,p2,p3,a3,a4,p4]
  cad=[]
  for a in dados:
    nome = a.getNome().split(" ")
    print("Cadastrando {} ... ".format(nome[0]))
    try:
        if type(a) is Professor:
          if a.getTitulacao() != "doutor":
              raise TitErradaProf
          elif a.getIdade() < 30:
              raise IdadeErradaProf
        else:
          if a.getCurso() != "CCO":
            if a.getCurso() != "SIN":
              raise CursoErrado
          if a.getIdade() < 18:
              raise IdadeErradaAluno
        for b in cad:
          if a.getCPF() == b.getCPF():
            raise CPFErrado
        
    except TitErradaProf:
      print("Erro: não foi possível fazer o cadastro!")
      print("{} sua titulação deve ser doutor ".format(nome[0]))

    except IdadeErradaProf:
      print("Erro: não foi possível fazer o cadastro!")
      print("{} sua idade deve ser igual ou maior que 30 anos".format(nome[0]))

    except CursoErrado:
      print("Erro: não foi possível fazer o cadastro!")
      print("{} seu curso deve ser CCO ou SIN" .format(nome[0]))
       
    except IdadeErradaAluno:
      print("Erro: não foi possível fazer o cadastro!")
      print("{} sua idade deve ser igual ou maior que 18 anos.".format(nome[0]))
        
    except CPFErrado:
      print("Erro: não foi possível fazer o cadastro!")
      print("{} nenhuma pessoa do cadastro pode ter o mesmo CPF".format(nome[0]))
        
    else:
      cad.append(a)
      print("Pessoa cadastrada!")
    finally:
      print("Fim cadastro")
      print()
    
print("PESSOAS CADASTRADAS (atendiam aos critérios): ")
for b in cad: 
  b.printDescricao()





      