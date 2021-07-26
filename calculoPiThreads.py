import threading
import os
import timeit
import statistics
from math import sqrt

NUM_EXECUCOES = int(input('Digite quantas execuções:'))
qtThreads = int(input('Digite quantas Threads:'))
pi = 0
tam = 1000000000
exePorThread = int(tam/qtThreads)
nInicial = 0

threads = []
temposExe = []
termo = 0.0

mediaTempoExecucao = 0.0
varTempoExecucao = 0.0
class Minhathread(threading.Thread):
    def __init__(self,indice, mutex):
        self.indice = indice
        self.mutex = mutex
        threading.Thread.__init__(self)
    def run(self):
        global pi
        for i in range(self.indice,tam):
            with self.mutex:
                pi += pow(-1, i) / (2*i+1)

stdoutmutex = threading.Lock()        

for exe in range(NUM_EXECUCOES):
    inicio = timeit.default_timer()
    for i in range(qtThreads):

        thread = Minhathread(nInicial, stdoutmutex)
        thread.start()
        #print(f"calc da T[{i}]{pi}")
        threads.append(thread)
        nInicial+=exePorThread
    fim = timeit.default_timer() - inicio
    temposExe.append(fim)

for x in range(NUM_EXECUCOES):
    mediaTempoExecucao += temposExe[x]/NUM_EXECUCOES


for x in range(NUM_EXECUCOES):
    termo = temposExe[x] - mediaTempoExecucao
    varTempoExecucao += pow(termo,2)/NUM_EXECUCOES


dp = sqrt(varTempoExecucao)
coeficienteVariacao = (dp/mediaTempoExecucao)
print("Coeficiente de variacao:{:.5f}%".format(coeficienteVariacao))
print("Media tempo de Execucao:{:.5f}s".format(mediaTempoExecucao))
print("Desvio padrao:{:.5f}".format(dp))
print("VALOR DE PI:{:.7f}".format(pi*4))
