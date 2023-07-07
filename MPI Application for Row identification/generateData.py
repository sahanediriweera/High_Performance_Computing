import csv
import random

def generate_csv_file(filename, number_of_records):
  with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    random.seed(3321)
    for i in range(number_of_records):
      row = [random.randint(0, 100) for _ in range(20)]
      writer.writerow(row)

if __name__ == '__main__':
  filename = 'data.csv'
  number_of_records = 1000000
  generate_csv_file(filename, number_of_records)

