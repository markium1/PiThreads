
import time
resultsPI = []
temposExecucao = []
i = 0
tam = 10000
pi = 0
def calcPI():

    global pi
    pi = 0
    for j in range(tam):
        pi += pow(-1,j) / (2*j+1)

    resultsPI.append(pi*4)


for i in range(10):
    inicio = time.time()
    calcPI()
    fim = time.time()
    temposExecucao.append(fim-inicio)
for i in range(len(resultsPI)):
    print(resultsPI[i])
    print(f'tempo->{temposExecucao[i]*1000:.2f}ms')
