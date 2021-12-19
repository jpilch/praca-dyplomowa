import os
from tqdm import tqdm
import cv2
import sys


DATASET_DIR = os.path.join(os.getcwd(), 'OID', 'Dataset')
CLASS_DIR, DATA_TYPE_DIR = None, None


def create_yolo_bbox(annotations_filename, bbox_format):
    global DATASET_DIR, DATA_TYPE_DIR, CLASS_DIR
    yolo_format = [None]*4
    im = cv2.imread(os.path.join('..', annotations_filename) + ".jpg")
    yolo_format[0] = bbox_format[0] + \
        int((bbox_format[2] - bbox_format[0])/2)
    yolo_format[1] = bbox_format[1] + \
        int((bbox_format[3] - bbox_format[1])/2)
    yolo_format[0] /= int(im.shape[1])
    yolo_format[1] /= int(im.shape[0])
    yolo_format[2] = (bbox_format[2] - bbox_format[0]) / int(im.shape[1])
    yolo_format[3] = (bbox_format[3] - bbox_format[1]) / int(im.shape[0])
    return yolo_format


def oid_to_yolo(class_dir_abs_path):
    global DATASET_DIR, DATA_TYPE_DIR, CLASS_DIR
    os.chdir(class_dir_abs_path)
    try:
        os.chdir('Label')
    except OSError:
        sys.exit('Label directory does not exist.')
    for label_file in tqdm(os.listdir(os.getcwd())):
        image_file_name = label_file.split('.')[0]
        yolo_format, results = list(), list()
        with open(label_file) as labelf:
            for label_line in labelf:
                for class_name in CLASSES:
                    label_line = label_line.replace(\
                    class_name, str(CLASSES.get(\
                    class_name, None)))
                labels = label_line.split()
                bbox_format = [float(labels[1]), \
                float(labels[2]), float(labels[3]), \
                float(labels[4])]
                yolo_format = create_yolo_bbox(image_file_name, \
                bbox_format)
                yolo_format.insert(0, labels[0])
                label_line = label_line.replace(label_line, \
                ' '.join(str(x) for x in yolo_format))
                results.append(label_line)
            os.chdir(class_dir_abs_path)
            with open(label_file, "w") as resultf:
                for l in results:
                    resultf.write(l)
                    resultf.write("\n")
            os.chdir("Label")
    os.chdir(DATA_TYPE_DIR)
    

def main():
    global DATASET_DIR, DATA_TYPE_DIR, CLASS_DIR
    with open("classes.txt", "r") as f:
        CLASSES = {l.strip('\n'): i for i, l in enumerate(f)}
    os.chdir(DATASET_DIR)
    for data_type_dir in os.listdir(os.getcwd()):
        DATA_TYPE_DIR = os.path.join(os.getcwd(), data_type_dir)
        os.chdir(data_type_dir)
        for class_dir in os.listdir(os.getcwd()):
            CLASS_DIR = os.path.join(os.getcwd(), class_dir)
            oid_to_yolo(os.path.join(os.getcwd(), class_dir))
        os.chdir(DATASET_DIR)


if __name__== '__main__':
    main()