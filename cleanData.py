

with open('original_data.txt', 'r') as data:
    with open('clean_data.txt', 'w') as result:
        for line in data:
            if line.strip("\n") != '            }':
                result.write(line)


with open('clean_data.txt', 'r') as data1:
    with open('cleaner_data.txt', 'w') as result1:
        for line in data1:
            if line.strip("\n") != '            "103706": {':
                result1.write(line)
            # This line is for HDI ( 137506 )
            #if line.strip("\n") != '            "137506": {':



with open('cleaner_data.txt', 'r') as data2:
    with open('final_data.txt', 'w') as result2:
        for line in data2:
            if line.strip("\n") != '    "indicator_value": {':
                result2.write(line)

