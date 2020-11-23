cook_book = {}
ingregient_name = 'ingregient_name'
quantity = 'quantity'
measure = 'measure'
list = []
dish_name = 0
list2 = [ingregient_name, quantity, measure]
with open('recipies', encoding= 'utf-8') as recipie:
    splitted_source_text = recipie.read().split('\n')
    element = ''
    for string in splitted_source_text:
        if string != '':
            element += string + '\n'
        else:
            list.append(element)
            element = ''
for recipie_sample in list:
    splitted_recipie_sample = recipie_sample.split('\n')
    cook_book[splitted_recipie_sample[dish_name]] = []
    for recipie_part in splitted_recipie_sample:
        if recipie_part == '':
            break
        else:
            if recipie_part == splitted_recipie_sample[0]:
                continue
            else:
                if recipie_part == splitted_recipie_sample[1]:
                    continue
                ingregient_list = recipie_part.split('|')
                count = 0
                for i in list2:
                    dict = {}
                    dict[i] = ingregient_list[count].strip()
                    count += 1
                    cook_book[splitted_recipie_sample[dish_name]].append(dict)
print(cook_book)














