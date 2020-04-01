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


def read_file(file):
    f = open(file, "r")
    commands = f.read()
    f.close()
    print(commands)

print("""1.Linux commands
2.Git""")
section = str(input("Choose\n"))

if section == "1":
    file = "commands.txt"
    r = "r"
    show_section(file)

elif section == "2":
    print("""1.Git install
2.Git commands""" + "\n")
    git_section = str(input("Choose section:\n"))

    if git_section == "1":
        file = "Git_install.txt"
        read_file(file)

    elif git_section == "2":
        file = "Git_commnads.txt"
        show_section(file)