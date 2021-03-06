#!/usr/bin/python3


def show_section(file):
    """Reading text file and sort it In alphabet order by ';' """
    f = open(file, "r")
    commands = f.read()
    f.close()

    commands = commands.split(";")
    clear_list = []

    for i in commands:
        d = ""
        for e in i:
            if e != "\n":
                d.lower()
                d += e

        clear_list.append(d)


    clear_list.sort()
    for i in clear_list:
        print(i + "\n")


def print_file(file):
    """Printing text file"""
    f = open(file, "r")
    commands = f.read()
    f.close()
    print(commands)


def check_back():
    """Check for while loop"""
    while True:
        back = input("\nBack?(y/n)\n")
        if back == "y":
            return True
        elif back != "n":
            continue
        else:
            return False


check = True
while check:
    print("""1.Linux commands
2.Linux helper
3.Git""")
    section = str(input("Choose section:\n"))

    if section == "1":
        file = "assets/commands.txt"
        show_section(file)
        check = check_back()

    elif section == "2":
        print("""\n
1.How to install files on linux (just commands)
2.How to install Deb files (with description)
3.How to install TAR.GZ files (with description)
4.Virtual enviroment
\n""")

        section = str(input("Choose section:\n"))
        if section == "1":
            file = "assets/Linux_how_to_install_files_Short.txt"
            print_file(file)
            check = check_back()

        elif section == "2":
            file = "assets/Linux_how_to_install_files Deb_long.txt"
            print_file(file)
            check = check_back()

        elif section == "3":
            file = "assets/Linux_how_to_install_files TAR_GZ_long.txt"
            print_file(file)
            check = check_back()

        elif section == "4":
            file = "assets/Venv.txt"
            print_file(file)
            check = check_back()

    elif section == "3":
        print("\n" + """1.Git install
2.Git commands
3.Git files state""" + "\n"*2)
        git_section = str(input("Choose section:\n"))

        if git_section == "1":
            file = "assets/Git_install.txt"
            print_file(file)
            check = check_back()

        elif git_section == "2":
            file = "assets/Git_commnads.txt"
            show_section(file)
            check = check_back()

        elif git_section == "3":
            file = "assets/Git_files_state.txt"
            print_file(file)
            check = check_back()
