import os


def sort_and_connect_files(file_folder):
    files_list = os.scandir(file_folder)
    full_text_list = []
    full_text = ''
    for file in files_list:
        with open(file, encoding='utf-8') as f:
            splited_text = f.readlines()
            text_len = str(len(splited_text)) + '\n'
            file_name = file.name + '\n'
            splited_text.insert(0, text_len)
            splited_text.insert(0, file_name)
            full_text_list.append(splited_text)
    sorted_text_list = sorted(full_text_list, key=len)
    for text in sorted_text_list:
        full_text += ''.join(text) + '\n'
    return full_text


enhanced_text = sort_and_connect_files('Задача №3/Text files')


def write_a_new_file(text):
    with open('Задача №3/New_File', 'w', encoding='utf-8') as final_file:
        final_file.write(text)
    return ''


print(write_a_new_file(enhanced_text))