name_of_file = 'data.txt'


with open(name_of_file) as file:
    lines = file.readlines()
data_string = []
for line in lines:
    if line.rstrip() != 1:
        temp_line=line.rstrip().split(' ')
        result = map(int,temp_line)
        data_string.extend(result)
    else:
        data_string.append(int(line.rstrip()))        
sum_data = sum(data_string)
srednee = sum(data_string)/len(data_string)

result_file = 'result.txt'
with open(result_file, 'w') as file:
    file.write('Сумма чисел в файле data.txt равна '+str(sum_data)+'\n')
    file.write('Среднее арифметическое числе в файле data.txt равно '+str(srednee)+'\n')
