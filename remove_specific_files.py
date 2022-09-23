import glob
import os

# 파일이 있는 폴더 경로
test_path = './default_flip_rotate_light_blur/test/*'
train_path = './default_flip_rotate_light_blur/train/*'

test_files = glob.glob(test_path)
for test_file in test_files:
    file_name = test_file.split('\\')[1]
    if 'blur' in file_name or 'flip' in file_name:
        print(test_file)
        if os.path.isfile(test_file):
            os.remove(test_file)
            # os.rmdir(path, option) # remove directory

train_files = glob.glob(train_path)
for train_file in train_files:
    file_name = train_file.split('\\')[1]
    if 'blur' in file_name or 'flip' in file_name:
        print(train_file)
        if os.path.isfile(train_file):
            os.remove(train_file)
            # os.rmdir(path, option) # remove directory

print('Done.')