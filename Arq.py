#Importando Biblioteca
import pandas as pd

#Criando um DataFrame
arq = pd.DataFrame(columns = ['Disciplina','Trabalhos','Avaliacao','AB1', 'AB2'],
index =['Ana', 'Carlos', 'Carol', 'Edvaldo', 'Lucas','Gabriel','Natanael','Henrique'], data = [['Fisica', 7.7,6.5,7.0,6.0], ['Fiscia', 7.9, 8.6,6.6,8.5], ['Fisica', 7.5,8.8,6.5,6.6], ['Fisica',10.,10.,10.,10.], ['Fisica', 6.5,6.,7.,5.5], ['Fisica', 9.9,9.6,9.4,8.9], ['Fisica', 7.9,9.8,8.7,7.5], ['Fisica', 7.,8.6,9.,5.]])

print(arq)