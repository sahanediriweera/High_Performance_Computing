import numpy as np
import matplotlib.pyplot as plt 

number_of_students = np.array([12,52,100, 1000, 10000, 100000, 1000000, 10000000, 100000000])
mpi_results = np.array([0.0032966136932373047, 0.0035424232482910156, 0.018476486206054688, 0.0005736351013183594, 0.001850128173828125, 0.0018374919891357422, 0.023200511932373047, 0.22089409828186035, 4.941363096237183])
sequential_results = np.array([4.887580871582031e-05, 5.6743621826171875e-05, 5.125999450683594e-05, 8.416175842285156e-05,0.0002346038818359375,0.0017294883728027344, 0.018389463424682617, 0.18597912788391113, 2.0190863609313965])

print(len(number_of_students), len(mpi_results), len(sequential_results))

ratio = mpi_results/sequential_results

x_log = np.log10(number_of_students)

plt.plot(x_log, ratio, 'bo-')
plt.xlabel('Log(Number of Students)')
plt.ylabel('Ratio of MPI Processing time to Sequential Processing Time')
plt.title('MPI to Sequential Processing Time\nVs\nNumber of Students in in memmory version')
plt.grid(True)

plt.savefig('in memmory plot.png')

print("Plot saved as plot.png")