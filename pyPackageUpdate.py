import os
import subprocess
from tqdm import tqdm
current_path = os.getcwd()



def save_outdated():
    print('~ GETTING OUTDATED PACKAGES ... ~')
    os.system(f'pip list --outdated > DATA/piplist_outdated.txt')
    print('~ DONE ~\n')
    return True

def create_update_list(method='pre'):
    packages_name = []
    path = f'{current_path}/DATA/piplist_outdated.txt' if method=='pre' else f'{current_path}/DATA/piplist_outdated_post.txt'

    with open(f'{path}', 'r', encoding='utf-8') as f:
        content = f.read().strip().splitlines()

    for ind, vals in enumerate(content):
        if ind > 1:
            packages_name.append(vals.split(' ')[0])
            
    return packages_name



def update_list(packages_list):
    if len(packages_list) == 0:
        print('~ NO PACKAGES TO UPDATE ~')
        return True

    print('~ UPDATING PACKAGES ... ~')
    for package in tqdm(packages_list):
        os.system(f'pip install --upgrade {package}')
    print('~ EVERYTHING ENDED CORRECTLY ~\n')

    return True

def check_still_outdated():
    os.system(f'pip list --outdated > DATA/piplist_outdated_post.txt')
    packages_list_post = create_update_list(method='post')
    if len(packages_list_post) == 0:
        return True
    still_outdated = ', '.join(packages_list_post)
    print(f'~ STILL OUTDATED PACKAGES (probably dependency problems): {still_outdated} ~')
    print(f' CHECK DATA/piplist_outdated_post.txt FOR MORE DETAILS ~\n')
    os.remove(f'{current_path}/DATA/piplist_outdated.txt')
    return False

def main_pip_update():
    save_outdated()
    packages_list = create_update_list()
    update_list(packages_list)
    check_still_outdated()
    return True

if __name__ == '__main__':
    main_pip_update()
    