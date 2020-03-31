
print("""1.Linux commands""")
section = str(input("Choose\n"))

if section == "1":
    f = open("commands.txt", "r")
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