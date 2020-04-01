def show_section(file):
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
    f = open(file, "r")
    commands = f.read()
    f.close()
    print(commands)

print("""1.Linux commands
2.Git""")
section = str(input("Choose section:\n"))

if section == "1":
    file = "commands.txt"
    r = "r"
    show_section(file)

elif section == "2":
    print("\n" + """1.Git install
2.Git commands
3.Git files state""" + "\n"*2)
    git_section = str(input("Choose section:\n"))

    if git_section == "1":
        file = "Git_install.txt"
        print_file(file)

    elif git_section == "2":
        file = "Git_commnads.txt"
        show_section(file)

    elif git_section == "3":
        file = "Git_files_state.txt"
        print_file(file)