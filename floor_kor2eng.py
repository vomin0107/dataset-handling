import os
import shutil
import xml.etree.ElementTree as ET

origin_dir_path = r'D:\workspace\dev\floor'
english_dir_path = r'D:\workspace\dev\floor/eng'


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def filename_to_english(file_name):
    print(file_name)
    name = file_name.split('\\')[-1]
    category = name.split('_')[0]

    if category == '카펫':
        eng_file_name = name.replace(category, 'carpet')
    elif category == '장판':
        eng_file_name = name.replace(category, 'linoleum')
    elif category == '대리석':
        eng_file_name = name.replace(category, 'marble')
    elif category == '소음매트':
        eng_file_name = name.replace(category, 'pad')
    elif category == '마루':
        eng_file_name = name.replace(category, 'wood')

    jpg_name = eng_file_name

    shutil.copyfile(file_name, os.path.join(english_dir_path, jpg_name))


def main():
    os_files = os.listdir(origin_dir_path)
    floor_types = ['carpet', 'linoleum', 'marble', 'pad', 'wood']
    file_names = []
    # print(os_files)
    create_folder(english_dir_path)

    for type in floor_types:
        dir = os.path.join(origin_dir_path, type)
        # print(dir)
        for file in os.listdir(dir):
            filename_to_english(os.path.join(dir, file))
            # print(os.path.join(dir, file.split('.')[0]))

    # print(file_names)

    # filename_to_english(file_names)

    print('done.')


if __name__ == '__main__':
    main()
