import glob
import shutil
import xml.etree.ElementTree as ET
import cv2
import numpy as np


xml_files = glob.glob(r'C:\Users\minuk\Documents\dev\objects\datasets\origin\xml_modified/*.xml')
jpg_files = glob.glob(r'C:\Users\minuk\Documents\dev\objects\datasets\origin\image/*.jpg')
jpeg_files = glob.glob(r'C:\Users\minuk\Documents\dev\objects\datasets\origin\image/*.jpeg')


def indent(elem, level = 0):
    i = "\n" + level * "   "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "   "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def display_progress():
    global index, total
    # os.system('cls')
    print(index, ' / ', total)
    index += 1


total = len(jpg_files) + len(jpeg_files)
index = 1

for jpeg in jpeg_files:
    name = jpeg.split('\\')[-1]
    zeros = np.zeros((720, 1280, 3), dtype=np.uint8)
    img = cv2.imread(jpeg)
    re_img = cv2.resize(img, (720, 720))
    zeros[0:, 280:1000] = re_img

    cv2.imwrite('img_wide/'+name, zeros)
    display_progress()

for jpg in jpg_files:
    name = jpg.split('\\')[-1]
    zeros = np.zeros((720, 1280, 3), dtype=np.uint8)
    img = cv2.imread(jpg)
    re_img = cv2.resize(img, (720, 720))
    zeros[0:, 280:1000] = re_img

    cv2.imwrite('img_wide/'+name, zeros)
    display_progress()


for xml in xml_files:
    name = xml.split('\\')[-1]
    doc = ET.parse(xml)
    root = doc.getroot()
    width = int(root.find("size").findtext("width"))
    height = int(root.find("size").findtext("height"))
    root.find("size").find("width").text = "1280"
    root.find("size").find("height").text = "720"
    objects = []
    for obj in root.iter("object"):

        # 기존 좌표 구하기
        xmin = int(obj.find("bndbox").findtext("xmin"))
        ymin = int(obj.find("bndbox").findtext("ymin"))
        xmax = int(obj.find("bndbox").findtext("xmax"))
        ymax = int(obj.find("bndbox").findtext("ymax"))

        xmin_tag = obj.find("bndbox").find("xmin")
        ymin_tag = obj.find("bndbox").find("ymin")
        xmax_tag = obj.find("bndbox").find("xmax")
        ymax_tag = obj.find("bndbox").find("ymax")

        xmin_tag.text = str(int((xmin * 720 / width) + 280))
        ymin_tag.text = str(int(ymin * 720 / height))
        xmax_tag.text = str(int((xmax * 720 / width) + 280))
        ymax_tag.text = str(int(ymax * 720 / height))

    indent(root)
    # ET.dump(root)
    doc.write("xml_wide/" + name, encoding="utf-8", xml_declaration=False)
