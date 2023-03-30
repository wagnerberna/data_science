import pandas as pd


df = pd.read_excel('ibge.xlsx', 'Tab 1.1.38')

colNm = [
         'Regiao',
          'MedioTotal',
          'MedioUtilizaram',
          'MedioNaoUtilizaram',
          'MedianoTotal',
          'MedianoUtilizaram',          
          'MedianoNaoUtilizaram',
          ]

df.columns = colNm

df = df.drop([0, 1 ,2 ,3 , 46, 47])

df = df.set_index(df['Regiao'])

df = df.drop(columns=['Regiao'])



df = df.drop(['Brasil'])

df = df.sort_values('MedioTotal')

df.plot(rot=90)

df = df.apply(pd.to_numeric, errors='coerce')

matCorr = df.corr()

pd.figure.clear()
df.boxplot(rot=90)