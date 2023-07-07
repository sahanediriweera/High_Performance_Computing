import numpy as np
import matplotlib.pyplot as plt 

number_of_students = np.array([10,50,100, 1000, 10000, 100000, 1000000, 10000000, 100000000])
mpi_results = np.array([0.0254518985748291, 0.03606724739074707,  0.022266864776611328, 0.12367630004882812, 0.13516831398010254, 0.23197221755981445, 0.8409843444824219, 9.061471223831177, 154.4647183418274])
sequential_results = np.array([0.012625694274902344, 0.012927770614624023, 0.013839960098266602, 0.014928817749023438, 0.021966218948364258, 0.11028838157653809, 2.138765573501587, 9.607653856277466, 105.88916516304016])


ratio = mpi_results/sequential_results

x_log = np.log10(number_of_students)

plt.plot(x_log, ratio, 'bo-')
plt.xlabel('Log(Number of Students)')
plt.ylabel('Ratio MPI Processing time to Sequential Processing Time')
plt.title('MPI to Sequential Processing Time\nVs\nNumber of Students in CSV version')
plt.grid(True)

plt.savefig('csv plot.png')
