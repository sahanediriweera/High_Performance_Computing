from mpi4py import MPI
import numpy as np
import time
import os

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

np.random.seed(3321)

number_of_students = 100000000
number_of_students += number_of_students%size
number_of_subjects = 4

if rank == 0:
    data = np.random.randint(0, 101, size=(number_of_students, number_of_subjects))
else:
    data = None

start_time = time.time()

local_data = np.empty(((number_of_subjects*number_of_students)//size ), dtype=int)
comm.Scatter(data, local_data, root=0)
local_data = np.reshape(local_data,(number_of_students//size,number_of_subjects))

mean = np.mean(local_data,axis=0)
global_average = comm.reduce(mean, op=MPI.SUM, root=0)

if rank ==0:

    average = global_average/size
    time_diff = time.time() - start_time
    print(average)
    with open((os.path.join('MPI results','results for {} students.txt'.format(number_of_students))),'w') as file:
        file.write("Time taken for {} students is {} and the average is {}".format(number_of_students,time_diff,average))
