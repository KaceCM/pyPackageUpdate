import os

current_path = os.getcwd()


def save_outdated():
    print("~ GETTING OUTDATED PACKAGES ... ~")
    if not os.path.exists(f"{current_path}/DATA"):
        os.mkdir(f"{current_path}/DATA")
    os.system(f"pip list --outdated > DATA/piplist_outdated.txt")
    print("~ DONE ~\n")
    return True


def create_update_list(method="pre"):
    packages_name = []
    path = (
        f"{current_path}/DATA/piplist_outdated.txt"
        if method == "pre"
        else f"{current_path}/DATA/piplist_outdated_post.txt"
    )

    with open(f"{path}", "r", encoding="utf-8") as f:
        content = f.read().strip().splitlines()

    for ind, vals in enumerate(content):
        if ind > 1:
            packages_name.append(vals.split(" ")[0])

    return packages_name


def update_list(packages_list):
    if len(packages_list) == 0:
        print("~ NO PACKAGES TO UPDATE ~")
        return True

    print("~ UPDATING PACKAGES ... ~")
    for package in packages_list:
        os.system(f"pip install --upgrade {package}")
    print("~ EVERYTHING ENDED CORRECTLY. LAST CHECK... ~\n")

    return True


def check_still_outdated():
    os.system(f"pip list --outdated > DATA/piplist_outdated_post.txt")
    #os.remove(f"{current_path}/DATA/piplist_outdated.txt")
    packages_list_post = create_update_list(method="post")
    if len(packages_list_post) == 0:
        os.remove(f"{current_path}/DATA/piplist_outdated_post.txt")
        print("~ EVERYTHING IS UP TO DATE ~\n")
        return True
    still_outdated = ",\n".join(packages_list_post)
    print(
        f"~ STILL OUTDATED PACKAGES (probably dependency problems) : ~ \n{still_outdated}"
    )
    print(f"~ CHECK DATA/piplist_outdated_post.txt FOR MORE DETAILS ~\n")
    return False


def main_pip_update():
    save_outdated()
    packages_list = create_update_list()
    update_list(packages_list)
    final_state = check_still_outdated()
    return final_state


if __name__ == "__main__":
    main_pip_update()
