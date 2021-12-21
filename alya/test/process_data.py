import random
import os

def gen_list():
    randomlist = []
    for i in range (0,3):
        number = random.randint(0,9)
        randomlist.append(number)
    return randomlist

def function1(id_string):
    ids_on_record = os.listdir(f'{base_dir}/data')
    if not id_string in ids_on_record:
        create_csv()


base_dir = '/Users/adianliusie/Documents/Projects/robot/alya_data/test'

def create_csv(id):
    file_name = f'{base_dir}/data/'

    with open(file_name, 'w') as f:
        file.write(output)


#output = gen_list()
#print(output)

create_csv('RAJAA2')
