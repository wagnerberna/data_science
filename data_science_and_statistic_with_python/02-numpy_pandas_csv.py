import numpy
import pandas

data = pandas.read_csv(
    "/media/wagner/HD-250GB2/Estatistica_Analise_Dados/csv/microdados_enem_2019_sp.csv",
    sep=";",
    encoding="iso-8859-1",
)

# [813772 rows x 44 columns]
print(data)

# visualizar o cabeçalhop
# [5 rows x 44 columns]
print(data.head())
