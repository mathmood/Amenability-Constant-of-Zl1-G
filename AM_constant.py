import numpy as  np
import pandas as pd


def amenabilityConstant(fileName):
    df = pd.read_csv(fileName)
    n= len(df.T)
    am = 0
    g= 0
    col = list(range(0,n))
    df = pd.read_csv(fileName, names = col)
    for i in range(0, n):
        g = g + df.at[i, 0]**2


    dim = []
    conju = []

    for j in range(0,n):
        k =0
        for i in range(0,n): k = k + abs(df.at[i,j])**2
        conju.append(g/k)



    for k in range(0,n):
        for l in range(0,n):
            x =0
            for i in range(0,n):
                x = x + (df.at[i,0]**2 * df.at[i,l] * np.conj(df.at[i,k]) )
            am = am + (abs(x) * conju[k] * conju[l])
    am = am / (g**2)

    return am



am = amenabilityConstant('characterTableS14.csv')
print(am)



