import numpy as  np
import pandas as pd


def dataCleansing (filename):
    df = pd.read_csv(filename)
    n = len(df.T)

    col = list(range(0,n))
    df = pd.read_csv(filename, names = col)

    df = df.drop([0], axis =1)
    df = df.T.reset_index(drop=True).T

    df.to_csv(filename,  encoding='utf-8', columns=None, header=None, index=None, index_label=None, line_terminator='\n')
    return None


# Given raw data from GAP, this function deletes the first column and save the data in the same file

dataCleansing('characterTableS.csv')