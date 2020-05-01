name = input("Введите имя для вашего дневника: ")

with open(name, 'a') as diary:
    data = input("Введите информацию: ")
    data += "\n"
    diary.write(data)
