import numpy as np
import time 
import csv
import os

def count_csv_rows(csv_file):
    row_count = 0
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            row_count += 1
    return row_count

start_time = time.time()

filename = 'marks_100000000.csv'

row_count = count_csv_rows(filename)

data = np.loadtxt(filename, delimiter=',')
mean = np.mean(data,axis=0)
time_diff = time.time()-start_time

with open(os.path.join('Sequential','Sequential Output for {} students.txt'.format(row_count)),'w') as file:
    file.write(f"The time taken is {time_diff} and the answer is {mean}")

