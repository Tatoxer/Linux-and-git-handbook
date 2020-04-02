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
    back = input("\nBack?(y/n)\n")
    if back == "y":
        return True
    else:
        return False


check = True
while check:
    print("""1.Linux commands
2.Git""")
    section = str(input("Choose section:\n"))

    if section == "1":
        file = "../assets/commands.txt"
        r = "r"
        show_section(file)
        check = check_back()

    elif section == "2":
        print("\n" + """1.Git install
2.Git commands
3.Git files state""" + "\n"*2)
        git_section = str(input("Choose section:\n"))

        if git_section == "1":
            file = "../assets/Git_install.txt"
            print_file(file)
            check = check_back()

        elif git_section == "2":
            file = "../assets/Git_commnads.txt"
            show_section(file)
            check = check_back()

        elif git_section == "3":
            file = "../assets/Git_files_state.txt"
            print_file(file)
            check = check_back()