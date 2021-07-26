# CALCULO DE 𝝅 COM THREADS 

Trabalho da Matéria de Sistemas Operacionais, onde foi solicitado fazer o cálculo do Valor de PI utilizando a série de Leibniz, fazendo o uso de Threads executando em paralelo.


# Arquivos

Neste Repositório contem o arquivo principal onde está Codado o programa.

## Resultados

Logo abaixo estará o resultado dos testes feitos para executar o programa, foi colocado em cada uma 5 Execuções para 1,2,4,8,16,32 Threads, calculando até o 10^9 termo da série.

#### EXECUÇÃO COM 1 THREAD

 - Coeficiente de variacao:0.48%
 - Media tempo de Execução: 0.032204
 - Desvio padrão: 0.01536
 -  VALOR DE PI: 3.1415920

#### EXECUÇÃO COM 2 THREADS

 - Coeficiente de variacao:0.60% 
 - Media tempo de Execução: 0.02003
 - Desvio padrão: 0.01207
 -  VALOR DE PI: 3.1415804

#### EXECUÇÃO COM 4 THREADS

 - Coeficiente de variacao:1.83% 
 - Media tempo de Execução: 0.01149
 - Desvio padrão: 0.02106 
 - VALOR DE PI: 3.1416208


#### EXECUÇÃO COM 8 THREADS

 - Coeficiente de variacao:1.63%
 - Media tempo de Execução: 0.00729
 - Desvio padrão: 0.01188
 - VALOR DE PI: 3.1416187


#### EXECUÇÃO COM 16 THREADS

 - Coeficiente de variacao:1.54%
 - Media tempo de Execução: 0.00985
 - Desvio padrão: 0.01520
 - VALOR DE PI: 3.1416238


#### EXECUÇÃO COM 32 THREADS

 - Coeficiente de variacao:0.87%
 - Media tempo de Execução: 0.00844
 - Desvio padrão: 0.00734
 - VALOR DE PI: 3.1415465

## Execução

No Windows basta apenas salvar o arquivo e executar, sendo necessário você ter o Python instalado. No Linux, digite `python "calculoPiThreads.py" ou python3 "calculoPiThreads.py".`
