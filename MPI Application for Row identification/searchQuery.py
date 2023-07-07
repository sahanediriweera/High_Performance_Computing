import pandas as pd
from mpi4py import MPI
import os

def readrows(fileName,startRow,endRow,rank,rowIndexes):
    df = pd.read_csv(fileName, skiprows=range(1, startRow))
    df = df.head(endRow - startRow + 1)

    results = []

    for i,row in enumerate(df.iterrows()):
        if i in rowIndexes:
            val = (f"rank {i} and row is {df.loc[i]}")
            results.append(val)

    return results

if __name__ == '__main__':
    rowIndexes = [0, 10, 20, 50, 100000,500000]
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    number_of_rows = 1000000//size

results = readrows('data.csv',rank*number_of_rows,(rank+1)*number_of_rows,rank,rowIndexes)

with open(os.path.join('Results',"results for rank {}.txt".format(rank)),'w') as file:
    file.writelines(results)




