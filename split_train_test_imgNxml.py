import random
import os
import shutil
import argparse

dir_path = r'C:\Users\hong0\PycharmProjects\image-classify-annotate\images'  # r'.\images'


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def divide_set(file_names, ratio, model):
    file_names_len = len(file_names)
    test_file_names_len = int(file_names_len * ratio)

    for i in range(test_file_names_len):
        file_name = file_names[i]
        print(file_name)

        jpg_name = file_name + '.jpg'
        shutil.copyfile(dir_path + '/' + jpg_name, dir_path + '/test/' + jpg_name)

        if model == 'detection':
            xml_name = file_name + '.xml'
            shutil.copyfile(dir_path + '/' + xml_name, dir_path + '/test/' + xml_name)

    for i in range(test_file_names_len, file_names_len):
        file_name = file_names[i]
        print(file_name)

        jpg_name = file_name + '.jpg'
        shutil.copyfile(dir_path + '/' + jpg_name, dir_path + '/train/' + jpg_name)

        if model == 'detection':
            xml_name = file_name + '.xml'
            shutil.copyfile(dir_path + '/' + xml_name, dir_path + '/train/' + xml_name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='images directory', type=str,
                        default=dir_path)
    parser.add_argument('--ratio', help='.ratio of test set', type=float,
                        default=0.1)
    parser.add_argument('--model', help='classify or detection(include .xml)', type=str,
                        default='classify')
    args = parser.parse_args()

    os_files = os.listdir(args.path)
    file_names = []

    for name in os_files:
        if name[:-4] not in file_names:
            file_names.append(name[:-4])

    random.shuffle(file_names)

    create_folder(dir_path + '/test')
    create_folder(dir_path + '/train')

    divide_set(file_names, args.ratio, args.model)

    print('done.')


if __name__ == '__main__':
    main()
