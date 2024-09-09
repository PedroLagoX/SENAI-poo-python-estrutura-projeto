from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco
import os
os.system("cls || clear")

# Instanciando classe.
pessoa_1 = Pessoa("Pedro", 19, Sexo.MASCULINO,
                  Endereco("Rodão", "8"))
print(pessoa_1)
