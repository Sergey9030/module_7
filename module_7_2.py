def custom_write(file_name, strings):
    file = open(file_name, 'w')
    for i in strings:
        file.write(f'{i}\n')
    file.close()
    file = open(file_name, 'r')
    i = 0
    sb = file.tell()
    strings_positions = {}
    line = file.readline()
    while line != '':
        i += 1
        strings_positions.update({(i, sb): line.strip()})
        sb = file.tell()
        line = file.readline()

    return strings_positions

info = [
    'Text for tell2.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
