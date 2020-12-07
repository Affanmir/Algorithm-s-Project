
import random
import strassen
import parallel
import naive
import N
import time


if __name__ == "__main__":

    n = [2, 16, 256, 1024, 2056, 4096]
    for i in range(len(n)):
        Maxi = n[i]
        matA = [[0 for i in range(Maxi)] for j in range(Maxi)]  #input 1
        matB = [[0 for i in range(Maxi)] for j in range(Maxi)]  #input 2


        matC = [[0 for i in range(Maxi)] for j in range(Maxi)]  #output for parallel
        timeC = []

        matD = [[0 for i in range(Maxi)] for j in range(Maxi)]  #naive
        timeD = []

        matE = [[0 for i in range(Maxi)] for j in range(Maxi)] #strassen
        timeE = []

        matF = [[0 for i in range(Maxi)] for j in range(Maxi)] #numpy
        timeF = []

        for i in range(Maxi):  # making matA and matB randomly
            for j in range(Maxi):
                matA[i][j] = random.randint(0, 100)
                matB[i][j] = random.randint(0, 100)
        '''
        print("\n")
        print("Matrix A is as follows")
        for i in range(Maxi):
            print(matA[i])

        print("\n")
        print("Matrix B is as follows")
        for i in range(Maxi):
            print(matB[i])'''
        t1 = time.time()
        matC = parallel.makeThreads(matA, matB, Maxi, matC)
        t2 = time.time()
        timeC.append(t2-t1)

        t1 = time.time()
        matD = naive.multiply(matA, matB, Maxi)
        t2 = time.time()
        timeD.append(t2 - t1)

        t1 = time.time()
        matE = strassen.strassen(matA, matB)
        t2 = time.time()
        timeE.append(t2 - t1)

        t1 = time.time()
        matF = N.product(matA, matB)
        t2 = time.time()
        timeF.append(t2 - t1)

    print(timeC, timeD, timeE, timeF)
