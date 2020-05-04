name_of_file = "pi.txt"


with open(name_of_file) as file:
    lines = file.readlines()
pi_string = ''
for line in lines:
    pi_string += line

birth =input('Введите ваш день рождения: ')
if birth in pi_string:
    index_str = pi_string.find(birth)
    print("Вы часть числа трансцидентного числа пи! Место вашего дня рождения в числе Pi "+str(index_str))
else:
    print("Числом ПИ не рождаются")