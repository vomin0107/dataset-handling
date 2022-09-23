import os
import glob
import shutil
import xml.etree.ElementTree as ET

xml_path = r'C:\Users\minuk\Documents\dev\objects\datasets\xml_modified'

def find_support(path):
    support_list = []
    count = 0

    for xml_file in glob.glob(path + '/*.xml'):
        print(xml_file)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text
                     )
            if value[3] == 'support':
                if value[0] not in support_list:
                    support_list.append(value[0])
                    shutil.copy(r'C:\Users\minuk\Documents\dev\objects\datasets\image/' + value[0],
                                './support/' + value[0])
                    count += 1

    with open('./support_list.txt', 'w+') as f:
        for name in support_list:
            f.write(name)
            f.write('\n')

    print(count)


if __name__ == '__main__':
    find_support(xml_path)