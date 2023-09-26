import numpy as np
import matplotlib.pyplot as plt

def exp1(m,stat,click):
    new_stat = stat
    while click>=1:
        click -= 1
        new_stat = np.matmul(m,new_stat)
    return new_stat

def exp2(m,stat,click):
    "Funcion para determinar la probabilidad dado un numero de rendijas, objetivos, un estado inicial y clicks transcurridos "
    new_stat = stat
    m1 = m
    for i in range(0, click):
        m = np.matmul(m1,m1)
    new_stat = np.dot(m, stat)
    return "Matriz:",np.array(m).tolist(),"Nuevo:",np.array(new_stat).tolist()

def exp3(m,stat,click):
    "Funcion para determinar la probabilidad dado un numero de rendijas, objetivos, un estado inicial y clicks transcurridos "
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = norma(m[i][j])
    new_stat = stat
    m2 = m
    for i in range(0, click):
        m = np.matmul(m2,m2)
    new_stat = np.dot(m, stat)
    for i in range(len(matriz)):
        if new_stat[i] > 1:
            new_stat[i] = 0
        for j in range(len(m)):
            if m[i][j] > 1:
                m[i][j] = 0
    return "Matriz:",np.array(matrix).tolist(),"Nuevo:",np.array(new_state).tolist()
