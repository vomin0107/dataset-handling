import glob
import xml.etree.ElementTree as ET
import pandas as pd


xml_origin_files = glob.glob(r'C:\Users\minuk\Documents\dev\objects\datasets\xml_origin\*.xml')
xml_files = glob.glob(r'C:\Users\minuk\Documents\dev\objects\datasets\xml_modified\*.xml')
xml_train_files = glob.glob(r'C:\Users\minuk\Documents\dev\objects\300x300\train\xml\*.xml')
xml_test_files = glob.glob(r'C:\Users\minuk\Documents\dev\objects\300x300\test\xml\*.xml')

class_origin_dict = {}
class_dict = {}
class_train_dict = {}
class_test_dict = {}

img_cnt = 0
box_cnt = 0
for xml in xml_origin_files:
    doc = ET.parse(xml)
    root = doc.getroot()
    objects = []
    img_cnt += 1
    for tags in root.iter("object"):
        # 기본 정보 구하기
        name = tags.findtext("name")
        if name not in class_origin_dict:
            class_origin_dict[name] = 0
        else:
            prev = class_origin_dict[name]
            class_origin_dict[name] = prev + 1
        box_cnt += 1

print('img_origin: ', img_cnt, ' box_origin: ', box_cnt)
print(class_origin_dict)

img_cnt = 0
box_cnt = 0
for xml in xml_files:
    doc = ET.parse(xml)
    root = doc.getroot()
    objects = []
    img_cnt += 1
    for tags in root.iter("object"):
        # 기본 정보 구하기
        name = tags.findtext("name")
        if name not in class_dict:
            class_dict[name] = 0
        else:
            prev = class_dict[name]
            class_dict[name] = prev + 1
        box_cnt += 1

print('img_modified: ', img_cnt, ' box_modified: ', box_cnt)
print(class_dict)

img_cnt = 0
box_cnt = 0
for xml in xml_train_files:
    doc = ET.parse(xml)
    root = doc.getroot()
    objects = []
    img_cnt += 1
    for tags in root.iter("object"):
        # 기본 정보 구하기
        name = tags.findtext("name")
        if name not in class_train_dict:
            class_train_dict[name] = 0
        else:
            prev = class_train_dict[name]
            class_train_dict[name] = prev + 1
        box_cnt += 1

print('img_train: ', img_cnt, ' box_train: ', box_cnt)
print(class_train_dict)

img_cnt = 0
box_cnt = 0
for xml in xml_test_files:
    doc = ET.parse(xml)
    root = doc.getroot()
    objects = []
    img_cnt += 1
    for tags in root.iter("object"):
        # 기본 정보 구하기
        name = tags.findtext("name")
        if name not in class_test_dict:
            class_test_dict[name] = 0
        else:
            prev = class_test_dict[name]
            class_test_dict[name] = prev + 1
        box_cnt += 1

print('img_test: ', img_cnt, ' box_test: ', box_cnt)
print(class_test_dict)

df_num_of_classes = pd.DataFrame([class_origin_dict, class_dict])#, class_train_dict, class_test_dict], index=['origin','mod','train','test'])
pd.DataFrame.to_csv(df_num_of_classes, 'number_of_class.csv')