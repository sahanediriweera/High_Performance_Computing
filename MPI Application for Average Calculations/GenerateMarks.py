import csv
import random
import os

num_rows = 100000000
num_columns = 4
random.seed(3321)
data = [[random.randint(0, 100) for _ in range(num_columns)] for _ in range(num_rows)]

csv_file = "marks_{}.csv".format(num_rows)

with open(os.path.join('Marks CSV',csv_file), mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

