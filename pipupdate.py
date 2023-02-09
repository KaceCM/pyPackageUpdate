import os
import subprocess
from tqdm import tqdm

current_path = os.getcwd()



def save_outdated():
    print('~ GETTING OUTDATED PACKAGES ... ~')
    os.system(f'pip list --outdated > DATA/piplist_outdated.txt')
    print('~ DONE ~')

def create_update_list():
    
    packages_name = []
    with open(f'{current_path}/DATA/piplist_outdated.txt', 'r', encoding='utf-8') as f:
        content = f.read().strip().splitlines()


    for ind, vals in enumerate(content):
        if ind > 1:
            packages_name.append(vals.split(' ')[0])
            
    return packages_name



def update_list(packages_list):
    print('~ UPDATING PACKAGES ... ~')
    for package in (packages_list):
        os.system(f'pip install --upgrade {package}')
    print('~ EVERYTHING ENDED CORRECTLY ~')

def main_pip_update():
    save_outdated()
    packages_list = create_update_list()
    update_list(packages_list)

main_pip_update()