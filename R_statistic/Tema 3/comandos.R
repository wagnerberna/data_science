

##### Bloco 1  ######


library(datasets)



df <- cars[1:6, ]



mediana <- function(vetor){
  vetor <- sort(vetor)
  n     <- length(vetor)
  if(n %% 2 == 0) {
    pos <- n / 2
    return( (vetor[pos] + vetor[pos + 1]) / 2)
  } else {
    pos <- (n + 1) / 3
    return( vetor[pos] )
  }
}

mediana(cars$speed)
mediana(cars$dist)


medianas <- c()
nomes    <- c()

for(i in 1:ncol(cars)){
  nomes    <- c(nomes, colnames(cars)[i])
  medianas <- c(medianas, mediana(cars[ ,i]))
}


cars_medianas <- data.frame('Variaveis' = nomes, 'Medianas' = medianas)










##### Bloco 2  ######




# Leitura de uma planilha salva no computador


df <- read.csv('D:/dados.csv', sep = ';', dec = ',')




# Leitura via requisição API

library(jsonlite)
df <- fromJSON("http://educacao.dadosabertosbr.com/api/escolas/buscaavancada?situacaoFuncionamento=1&energiaInexistente=on&aguaInexistente=on&esgotoInexistente=on&cozinha=on")









### Bloco 3 ####



library(readxl)

df <- data.frame(read_xlsx('D:/OneDrive/dados.xlsx'))

























