from mpi4py import MPI
import numpy as np
import csv
import time
import os



def count_csv_rows(csv_file):
    row_count = 0
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            row_count += 1
    return row_count

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

filename = 'marks_100000000.csv'

if rank == 0:
    start_time = time.time()

row_count = count_csv_rows(filename)

division = row_count//size

start_row = rank*division
end_row = division*(rank+1)-1

data = np.loadtxt(filename, delimiter=',', skiprows=start_row, max_rows=end_row-start_row+1)

local_average = np.mean(data,axis=0)

global_average = comm.reduce(local_average, op=MPI.SUM, root=0)

if rank == 0:
    final_average = global_average / size
    print("Final average:", final_average)
    time_diff = time.time()-start_time
    print(f"Time Taken {time_diff}")
    with open(os.path.join("MPI CSV","output for {} students.txt".format(row_count)),'w') as file:
        file.write(f" time taken for {row_count} students is  {time_diff} and answer is {final_average}")

