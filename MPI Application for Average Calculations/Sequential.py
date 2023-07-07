import numpy as np
import time 
import os 

number_of_students = 100000000
number_of_subjects = 4

np.random.seed(3321)

data = np.random.randint(0, 101, size=(number_of_students, number_of_subjects))

start_time = time.time()
mean = np.mean(data,axis=0)
time_diff = time.time()-start_time
print(mean)

with open((os.path.join('Sequential Results','results for {} students.txt'.format(number_of_students))),'w') as file:
    file.write("Time taken for {} students is {} and the average is {}".format(number_of_students,time_diff,mean))