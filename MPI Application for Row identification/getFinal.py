import os

def read_directory(directory_path, output_file):
    with open(output_file, 'a') as output:
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    file_contents = file.read()                   
                    output.write(file_contents)
                    output.write('\n')

directory_path = os.path.join('Results')

output_file = os.path.join('search_queries.txt')

read_directory(directory_path, output_file)
