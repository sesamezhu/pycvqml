from sklearn import svm
import os
import cv2
import numpy
import joblib
from time_log import time_log

root = r'D:\share\202200517\sklearn'
shape_width = 100
shape_height = 140
reshape_len = shape_width * shape_height * 3
model_file = 'model.pkl'


def rgb2gray(color):
    return color[0] + color[1] + color[2]


def fit():
    data_x = []
    data_y = []
    for char_no in os.listdir(root):
        char_path = os.path.join(root, char_no)
        time_log(f'reading {char_path}')
        for file in os.listdir(char_path):
            image_path = os.path.join(char_path, file)
            image = cv2.imread(image_path)
            image = cv2.resize(image, (shape_width, shape_height))
            # image = numpy.asarray(image.reshape((1, reshape_len)))
            data_x.append(image)
        data_y.append(char_no)
    data = numpy.row_stack(data_x)
    data = data.reshape((len(data_x), reshape_len))
    svc = svm.SVC(C=10000, gamma=0.001, tol=0.01, verbose=True)
    time_log('fitting')
    svc.fit(data, data_y)
    time_log(f'dumping {model_file}')
    joblib.dump(svc, model_file)


time_log(f'loading {model_file}')
svc = joblib.load(model_file)

test_path = r'D:\share\202200517\check'
for check in os.listdir(test_path):
    check_path = os.path.join(test_path, check)
    for file in os.listdir(check_path):
        file_path = os.path.join(check_path, file)
        image = cv2.imread(file_path)
        image = cv2.resize(image, (shape_width, shape_height))
        image = image.reshape(1, reshape_len)
        time_log(f'{svc.predict(image)}: {file_path}')

if __name__ == "__main__":
    print()
