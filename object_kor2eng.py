import os
import shutil
import xml.etree.ElementTree as ET

origin_dir_path = r'./images'
english_dir_path = r'./to_english'


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def filename_to_english(file_names):
    file_names_len = len(file_names)

    for i in range(file_names_len):
        origin_file_name = file_names[i]
        file_name = file_names[i].split('_')[0]
        file_num = file_names[i].split('_')[1]
        print(file_name, file_num)

        origin_jpg_name = origin_file_name + '.jpg'
        origin_xml_name = origin_file_name + '.xml'

        target_path = origin_dir_path + "/" + origin_xml_name
        target_xml = open(target_path, 'rt', encoding='UTF8')

        tree = ET.parse(target_xml)

        root = tree.getroot()

        # tag to modify
        filename_tag = root.find("filename")
        # path_tag = root.find("path")
        # class_tag = root.find("name")

        if file_name == '고무줄':
            # path_tag.text = path_tag.text.replace(file_name + '_', 'band-')
            file_name = 'band'
        elif file_name == '리모컨':
            # path_tag.text = path_tag.text.replace(file_name + '_', 'remoteControl-')
            file_name = 'remoteControl'
        elif file_name == '멀티탭':
            # path_tag.text = path_tag.text.replace(file_name + '_', 'multiOutlet-')
            file_name = 'multiOutlet'
        elif file_name == '반려동물':
            # path_tag.text = path_tag.text.replace(file_name + '_', 'pet-')
            file_name = 'pet'
        elif file_name == '배변패드':
            # path_tag.text = path_tag.text.replace(file_name + '_', 'pooPad-')
            file_name = 'pooPad'
        elif file_name == '빨래감':
            # path_tag.text = path_tag.text.replace(file_name + '_', 'laundry-')
            file_name = 'laundry'
        elif file_name == '빨래건조대':
            # path_tag.text = path_tag.text.replace(file_name + '_', 'laundryBar-')
            file_name = 'laundryBar'
        elif file_name == '실내슬리퍼':
            # path_tag.text = path_tag.text.replace(file_name  + '_', 'slipper-')
            file_name = 'slipper'
        elif file_name == '의자다리':
            # path_tag.text = path_tag.text.replace(file_name + '_', 'chairLegs-')
            file_name = 'chairLegs'
        elif file_name == '장난감':
            # path_tag.text = path_tag.text.replace(file_name + '_', 'toy-')
            file_name = 'toy'
        elif file_name == '전선':
            # path_tag.text = path_tag.text.replace(file_name + '_', 'electricWire-')
            file_name = 'electricWire'
        elif file_name == '조명받침대':
            # path_tag.text = path_tag.text.replace(file_name + '_', 'stand-')
            file_name = 'stand'
        elif file_name == '초코파이똥':
            # path_tag.text = path_tag.text.replace(file_name + '_', 'poo-')
            file_name = 'poo'
        elif file_name == '커튼아랫단':
            # path_tag.text = path_tag.text.replace(file_name + '_', 'curtain-')
            file_name = 'curtain'
        elif file_name == '필기구':
            # path_tag.text = path_tag.text.replace(file_name + '_', 'stationary-')
            file_name = 'stationary'
        elif file_name == '핸드폰':
            # path_tag.text = path_tag.text.replace(file_name + '_', 'smartPhone-')
            file_name = 'smartPhone'

        jpg_name = file_name + '_' + file_num + '.jpg'
        xml_name = file_name + '_' + file_num + '.xml'

        filename_tag.text = jpg_name  # new string
        # class_tag.text = class_tag.text.replace(file_name)
        tree.write(english_dir_path + '/' + xml_name)

        shutil.copyfile(origin_dir_path + '/' + origin_jpg_name, english_dir_path + '/' + jpg_name)


def main():
    os_files = os.listdir(origin_dir_path)
    file_names = []

    for dir in os_files:
        if dir[:-4] not in file_names:
            file_names.append(dir[:-4])

    create_folder(english_dir_path)

    filename_to_english(file_names)

    print('done.')


if __name__ == '__main__':
    main()
