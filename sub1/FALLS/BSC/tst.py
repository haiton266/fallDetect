import os
import fnmatch

os.chdir("./sub1/FALLS/BSC")
index = 0
for file in os.listdir():
    if fnmatch.fnmatch(file, '*_acc_*'):
        with open(file, 'r') as file:
            index+=1
            file_contents = file.readlines()[17::4]
            processed_contents = [line.split()[1:] for line in file_contents]
            final_contents = [' '.join(line) for line in processed_contents]
            with open(f'{index}.txt', 'w') as file:
                for item in final_contents:
                    file.write(f'{item}\n')
