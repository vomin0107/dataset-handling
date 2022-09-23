from PIL import Image
import os
import glob
import time


# resize 목표 해상도
SIZE = (448, 448)

# 이미지가 있는 폴더 경로
path = r'D:\workspace\dev\floor\eng\test/'
test_path = path + 'test/'
train_path = path + 'train/'
test_resized_path = test_path + 'resized/'
train_resized_path = train_path + 'resized/'
image_resized_path = r'D:\workspace\dev\floor\eng-448\test/'

# glob, os 비교
test_files = glob.glob(test_path + "*.jpg") # glob: absolute path
train_files = glob.glob(train_path + "*.jpg")
jpg_files = glob.glob(path + "*.jpg")
jpeg_files = glob.glob(path + "*.jpeg")
# os_files = os.listdir(path) # os: relative path


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def display_progress(tot, idx, t_start):
    # # os.system('cls')
    # percent = int(100 * idx / tot)
    # percent_anti = 100 - percent
    # percent_err = 50 - int(percent_anti/2) - int(percent/2)
    #
    # percent_str = str(percent) + '% ['
    # for i in range(int(percent/2)):
    #     percent_str += '#'
    # for j in range(int(percent_anti/2)):
    #     percent_str += '-'
    # if percent_err > 0:
    #     for k in range(percent_err):
    #         percent_str += '-'
    # percent_str += ']'
    # print(percent_str)
    print(idx, '/', tot, round(time.time() - t_start, 2))


def main():
    index = 0
    # total = len(test_files) + len(train_files)
    total = len(jpg_files) + len(jpeg_files)
    print(total)

    # create_folder(test_resized_path)
    # create_folder(train_resized_path)
    create_folder(image_resized_path)

    # 해상도 조절 후 저장
    # for test_image in test_files:
    #     image_file = Image.open(test_image)
    #     resize_image = image_file.resize(SIZE)
    #     resize_image.save(test_resized_path + test_image.split('test\\')[1][:-4]+'_resized.jpg')
    #     index += 1
    #     display_progress(total, index)
    #
    # for train_image in train_files:
    #     image_file = Image.open(train_image)
    #     resize_image = image_file.resize(SIZE)
    #     resize_image.save(train_resized_path + train_image.split('train\\')[1][:-4]+'_resized.jpg')
    #     index += 1
    #     display_progress(total, index)

    time_start = time.time()
    for jpg_image in jpg_files:
        image_file = Image.open(jpg_image)
        resized_image = image_file.resize(SIZE)
        resized_image.save(image_resized_path + jpg_image.split('test\\')[1])
        index += 1
        display_progress(total, index, time_start)

    for jpeg_image in jpeg_files:
        image_file = Image.open(jpeg_image)
        resized_image = image_file.resize(SIZE)
        resized_image.save(image_resized_path + jpeg_image.split('test\\')[1])
        index += 1
        display_progress(total, index, time_start)

    print('Done.')


if __name__ == '__main__':
    main()
