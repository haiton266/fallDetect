import os
import fnmatch


index = 0
for i in range(1,32):
    directory = f"./sub{i}/ADL"
    if not os.path.exists(directory):
        print(f"{directory} is not exist!")
    else:
        os.chdir(directory)
        for folder in os.listdir():
            os.chdir(f"./{folder}")
            for file in os.listdir():
                if fnmatch.fnmatch(file, '*_acc_*'):
                    with open(file, 'r') as file:
                        file_contents = file.readlines()[17::4]
                        processed_contents = [line.split()[1:] for line in file_contents]
                        final_contents = [' '.join(line) for line in processed_contents]
                        os.chdir('../../../notFall')
                        with open(f'{index}.txt', 'w') as file:
                            for item in final_contents:
                                file.write(f'{item}\n')
                            index+=1
                        os.chdir(f'../sub{i}/ADL/{folder}')
            os.chdir('../')
        os.chdir('../../')