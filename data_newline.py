with open('original_data.txt', 'r') as data:
    with open('clean_data.txt', 'w') as result:
        for line in data:
            line = line.replace(',', '\n')
            result.write(line)