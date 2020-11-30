def sort_and_connect():
    full_text_list = []
    sorted_full_text = ''
    with open('1.txt', encoding='utf-8') as file1:
        text1 = file1.readlines()
        text1_len = str(len(text1)) + '\n'
        file1_name = file1.name + '\n'
        text1.insert(0, text1_len)
        text1.insert(0, file1_name)
        full_text_list.append(text1)
    with open('2.txt', encoding='utf-8') as file2:
        text2 = file2.readlines()
        text2_len = str(len(text2)) + '\n'
        file2_name = file2.name + '\n'
        text2.insert(0, text2_len)
        text2.insert(0, file2_name)
        full_text_list.append(text2)
    with open('3.txt', encoding='utf-8') as file3:
        text3 = file3.readlines()
        text3_len = str(len(text3)) + '\n'
        file3_name = file3.name + '\n'
        text3.insert(0, text3_len)
        text3.insert(0, file3_name)
        full_text_list.append(text3)

    if len(full_text_list[0]) < len(full_text_list[1]) and len(full_text_list[2]):
        sorted_full_text += ''.join(full_text_list[0]) + '\n'
        if len(full_text_list[1]) < len(full_text_list[2]):
            sorted_full_text += ''.join(full_text_list[1]) + '\n'
            sorted_full_text += ''.join(full_text_list[2])
        else:
            sorted_full_text += ''.join(full_text_list[2]) + '\n'
            sorted_full_text += ''.join(full_text_list[1])
    elif len(full_text_list[1]) < len(full_text_list[0]) and len(full_text_list[2]):
        sorted_full_text += ''.join(full_text_list[1]) + '\n'
        if len(full_text_list[0]) < len(full_text_list[2]):
            sorted_full_text += ''.join(full_text_list[0]) + '\n'
            sorted_full_text += ''.join(full_text_list[2])
        else:
            sorted_full_text += ''.join(full_text_list[2]) + '\n'
            sorted_full_text += ''.join(full_text_list[0])
    elif len(full_text_list[2]) < len(full_text_list[0]) and len(full_text_list[1]):
        sorted_full_text += ''.join(full_text_list[2]) + '\n'
        if len(full_text_list[0]) < len(full_text_list[1]):
            sorted_full_text += ''.join(full_text_list[0]) + '\n'
            sorted_full_text += ''.join(full_text_list[1])
        else:
            sorted_full_text += ''.join(full_text_list[1]) + '\n'
            sorted_full_text += ''.join(full_text_list[0])

    with open('ConnectedFiles.txt', 'w', encoding='utf-8') as final_file:
        final_file.write(sorted_full_text)
    return
print(sort_and_connect())