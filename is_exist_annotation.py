import os
import glob

def compare_jpg_xml():
    path = r"C:\Users\hong0\PycharmProjects\image-scrapping\images"

    # glob, os 비교
    jpg_files = glob.glob(path + "\*.jpg")
    xml_files = glob.glob(path + '\*.xml')

    for jpg_name in jpg_files:
        if jpg_name.split('.')[0]+'.xml' in xml_files:
            pass
        else:
            print('no xml file : ', jpg_name)


    for xml_name in xml_files:
        if xml_name.split('.')[0]+'.xml' in xml_files:
            pass
        else:
            print('no jpg file : ', xml_name)

    print(len(jpg_files))
    print(len(xml_files))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    compare_jpg_xml()
