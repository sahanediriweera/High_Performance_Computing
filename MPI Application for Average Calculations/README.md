This Assignment is done in main two ways. The first way incorporates accessing created CSV files to store the marks values. The second method does the it by generating the values in memmory.

First Mechanism Using CSV Files

Please note the marks CSV files for 1000000,10000000, and 100000000 file are deleted due to size containstraints.

This mechanism approaches the problem in a practical approach where the results of the students are stored in a CSV file and the program reads the results CSV file and make the suitable calculations the generations are in the Marks CSV folder. The sequential program loads the CSV file into the memmory and then make the necessary calculations. The results are stored in the the folder named Sequential CSV which contains the output time taken and the number of students.The MPI program calculates by reading different rows of the data during different processses The results are as follows 

To generate the CSV files edit the number of students value in the file and run the command

python3 GenerateMarks.py

To do the Sequential Calculation change the value for CSV file name as desired in the code and run the command

python3 CSV_SequentialProgram.py

To do the MPI Calculation change the value for CSV file name as desired in the code and run the command

mpirun -n 4 python3 CSV_MPIProgram.py


![Alt text](<csv plot.png>)

Second Mechanism Using In Memmory and Scattering

This mechanism scatters the generated dataset. The sequential does the calculations using the given data and the results are in the Sequential Results folder and the MPI scatters the data into different processes and does the calculations and the results are in the MPI results folder. The final results are as follows.

To run the Sequential program change the number_of_students value as desired and run the following command

python3 Sequential.py

To run the MPI program change the num_of_students value as desired and run the following command

mpirun -n 4 python3 MPIProgram.py

![Alt text](<in memmory plot.png>)

To generate the plots run the commands

for CSV version

python3 plot_for_CSV.py

for in memmory version

python3 plotting_for_inmemmory.py