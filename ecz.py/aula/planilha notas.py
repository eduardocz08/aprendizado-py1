import csv
#gravar dados em csv
with open ('alunos.csv', 'w' , newline="") as arquivo:
     escritor = csv.writer (arquivo)
     escritor.writerow (['nome', 'nota'])
     escritor.writerow (['Ana', 8.5])
     escritor.writerow (['Carlos', 6.7])

with open ('alunos.csv', 'r') as arquivo:
     for linha in arquivo:
          print (linha)