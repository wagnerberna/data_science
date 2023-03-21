library(readxl)

dados <- read_excel('dados.xlsx', col_types = c('text', 'numeric', 'text', 'numeric', 'text'), na = 'NA')

View(dados)
