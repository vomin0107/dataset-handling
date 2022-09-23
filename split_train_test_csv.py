import csv

path_csv_dir = r'D:\workspace\dev\objects\datasets\csv/'
path_csv = path_csv_dir + 'csv_default_augmentedx9_vertexai.csv'
path_coral_csv = path_csv_dir + path_csv.split('/')[1].replace('default', 'automl')

f_origin = open(path_csv, 'r')
rdr_origin = csv.reader(f_origin)

f_unified = open(path_coral_csv, 'a', newline='')
wr = csv.writer(f_unified)

cnt = 0
for line in rdr_origin:
    filename = 'gs://first-detection/images/' + line[0]
    width = line[1]
    height = line[2]
    name_class = line[3]
    xmin = line[4]
    ymin = line[5]
    xmax = line[6]
    ymax = line[7]

    xmin_new = round(float(xmin) / float(width), 4)
    ymin_new = round(float(ymin) / float(height), 4)
    xmax_new = round(float(xmax) / float(width), 4)
    ymax_new = round(float(ymax) / float(height), 4)

    if cnt % 9 == 1:
        val = 'TEST'
    elif cnt % 9 == 2:
        val = 'VALIDATION'
    else:
        val = 'TRAINING'
    wr.writerow([val, filename, name_class, xmin_new, ymin_new,'','', xmax_new, ymax_new,'',''])
    cnt += 1

f_origin.close()
f_unified.close()
