def show_section(file, mode):
    f = open(file, r)
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

    else:
        print("Goodby")

print("""1.Linux commands
2.Git""")
section = str(input("Choose\n"))

if section == "1":
    file = "commands.txt"
    r = "r"
    show_section(file, "r")

elif section == "2":
    file = "GIt.txt"
    r = "r"
    show_section(file, "r")