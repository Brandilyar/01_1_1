
name_of_file += "pi.txt"
accur = int(input("Уточните до какого знака вам нужно число пи"))

with open(name_of_file) as file:
    pi_string = ''
    lines = file.readlines()
    for line in lines:
        pi_string +=line.strip()
    print(pi_string[:accur])

    print("Количество строчек", len(lines))