name_of_file = input("Введите название файла")
name_of_file += ".txt"

with open(name_of_file) as file:
    for line in file:
        print(line.rstrip())