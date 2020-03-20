#                   DESAFIO 92
#  Crie um programa que leia NOME, ANO DE NASCIMENTO e CARTEIRA DE TRABALHO e cadastre(COM IDADE) em um DICIONARIO .
#  Se 'CTPS' for diferente de ZERO, o dicionario recebera tambem o ANO DE CONTRATACAO e o SALARIO. Calcule e acrescente
#  alem da IDADE com quantos anos a pessoa vai se aposentar  [35 ANOS DE CTPS]
from time import sleep
import datetime
CurrentY = datetime.date.today().year


info = dict()
info["NAME"] = str(input('Name: '))
Ybday = int(input('Year of Birthday: '))
info["AGE"] =  CurrentY - Ybday
info["CTPS"] =  int(input('CTPS NUMBER [0 if not registered] : '))
if info["CTPS"] != 0:
   info["YHIRED"] = int(input('When were you HIRED/REGISTERED : '))
   info["YRETIRE"] = (info["YHIRED"] + 35) - Ybday
   info["INCOME"] = float(input('Monthly Income: $'))
print("'''" * 10)
for e, v in info.items():
    print(f'{e} has the value of {v}')
    sleep(1)
print("'''" * 10)
