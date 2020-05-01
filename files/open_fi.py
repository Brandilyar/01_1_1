#вариант с абсолютным путем
with open("/Users/isakura313/Desktop/01_1/files/index.txt") as file:
    content = file.read()
    print(content)