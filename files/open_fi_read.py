name_of_file = input("Введите название файла")
name_of_file += ".txt"

negative_words = ['плохой','неудачный', 'неприятный']

with open(name_of_file) as file:
    lines = file.readlines()
    for line in lines:
        for word in negative_words:
            if line.strip() == word:
                print("Зацензурено")
                break
            # else:
            print(line.strip())
            break
    print("Количество строчек", len(lines))