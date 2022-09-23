import csv


path = r'W:\workspace\dev\objects\datasets\csv\csv_coral_augmentedx9_add_self_no_toy.csv'
class_dict = {}

file_csv = open(path, 'r')
rdr_origin = csv.reader(file_csv)

cnt = 1
for line in rdr_origin:
    name = line[2]
    if name not in class_dict:
        class_dict[name] = 0
    else:
        prev = class_dict[name]
        class_dict[name] = prev + 1
    cnt += 1
    print(cnt)

print(class_dict)

file_csv.close()