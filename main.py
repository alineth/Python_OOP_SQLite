#Importa nosso arquivo Pessoa.py no diretório model

from model.Pessoa import Pessoa 

#Exemplo de uso

aline = Pessoa(1, "Aline Thiel")
print(aline)

#Quero mostrar só o nome

print(aline.nome)