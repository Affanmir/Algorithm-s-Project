import random
import threading


def multiply(matA, matB, Maxi, step_i, matC):
    core = step_i + 1
    for i in range(step_i, step_i + 1):
        for j in range(Maxi):
            for k in range(Maxi):
                matC[i][j] += matA[i][k] * matB[k][j]

def makeThreads(matA, matB, Maxi, matC):
    list_of_threads = []  # creating N number Maxi number threads
    for i in range(Maxi):
        list_of_threads.append(threading.Thread(target=multiply, args=(matA, matB, Maxi, i, matC)))

    for i in range(Maxi):  # running threads
        list_of_threads[i].start()

    for i in range(Maxi):  # joinin threads
        list_of_threads[i].join()
    return matC