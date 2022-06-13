from sklearn import svm
import os
import cv2
import numpy
import joblib
from skimage import feature
from time_log import time_log, time_err
import matplotlib.pyplot as plt

roots = [r'D:\share\202200517\sklearn', r'D:\share\202200517\sk_hot']
shape_width = 100
shape_height = 140
reshape_len = shape_width * shape_height
# hog_len = 12150
# model_file = r'D:\wechat\WeChat Files\zhughld\FileStorage\File\2022-05\SVM_MC\model\svm_efd_train_model.pkl'
# model_file = r'D:\share\202200517\model_bof_hog_1000.pkl'
model_file = r'D:\share\202200517\model_bilateral_hog.pkl'
# test_path = r'D:\wechat\WXWork\1688851339199364\Cache\File\2022-05\result3\3#bof'
test_path = r'D:\share\202200517\point5'
check_chars = ['2', '3', '5', '6', '8', '9']


def raw(frame):
    return cv2.resize(frame, (shape_width, shape_height))


def hog(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    frame = cv2.resize(frame, (shape_width, shape_height))
    frame = cv2.GaussianBlur(frame, (3, 3), 1)
    frame = cv2.equalizeHist(frame)
    frame = cv2.Laplacian(frame, cv2.CV_64F)
    return feature.hog(frame)
    # gabored = filters.gabor(frame, frequency=0.6,theta=45,n_stds=5)[0].reshape(1, -1)[0]
    # return numpy.concatenate((hogged, gabored))
    # return gabored


def hog2(frame):
    # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    frame = cv2.resize(frame, (shape_width, shape_height))
    blur = cv2.bilateralFilter(frame, 9, 75, 75)
    features = feature.hog(blur, orientations=9, pixels_per_cell=[8, 8], cells_per_block=[2, 2],  # visualize=True,
                           feature_vector=True)
    # print(features)
    return features.reshape(1, 6336)  # HOG特征


def build_pair():
    data_x = []
    data_y = []
    for root in roots:
        for char_no in os.listdir(root):
            if char_no not in check_chars:
                continue
            char_path = os.path.join(root, char_no)
            time_log(f'reading {char_path}')
            for file in os.listdir(char_path):
                image_path = os.path.join(char_path, file)
                image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                image = hog2(image)
                data_x.append(image)
                data_y.append(char_no)
    return data_x, data_y


def fit():
    data_x, data_y = build_pair()
    data = numpy.row_stack(data_x)
    data = data.reshape((len(data_x), data_x[0].size))
    svc = svm.SVC(verbose=True, probability=True, C=5,
                  decision_function_shape='ovo', gamma=0.001, kernel='rbf')
    time_log('fitting')
    svc.fit(data, data_y)
    time_log(f'dumping {model_file}')
    joblib.dump(svc, model_file)


def check_max(prob):
    li = prob[0].tolist()
    max_val = max(li)
    return check_chars[li.index(max_val)], max_val


def predict():
    # time_log(f'loading {model_file}')
    svc = joblib.load(model_file)
    for check in os.listdir(test_path):
        good = 0
        total = 0
        check_path = os.path.join(test_path, check)
        for file in os.listdir(check_path):
            file_path = os.path.join(check_path, file)
            image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            # image = cv2.resize(image, (shape_width, shape_height))
            # image = image.reshape(1, reshape_len)
            image = hog2(image)
            image = image.reshape(1, -1)
            # print(svc.predict(image), file_path)
            checked = svc.predict_proba(image)
            total += 1
            checked_char, checked_prob = check_max(checked)
            if check == checked_char and checked_prob > 0.7:
                good += 1
                time_log(f'{total + 100000}-{checked_char}-{checked_prob}: {file_path}')
            else:
                time_err(f'{total + 100000}-{checked_char}-{checked_prob}: {file_path}')
            # time_log(f'{checked_char}-{checked_prob}: {file_path}')
        time_log(f'{good}/{total}={good / total * 100}%')


if __name__ == "__main__":
    # fit()
    predict()
    # frame = cv2.imread(r'D:\wechat\WXWork\1688851339199364\Cache\File\2022-05\result3\1bof\2\2_13.png', cv2.IMREAD_GRAYSCALE)
    # plt.subplot(1, 3, 1)
    # plt.imshow(frame)
    # # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # # frame = cv2.medianBlur(frame, 3)
    # # frame = cv2.GaussianBlur(frame, (3, 3), 1)
    # frame = cv2.bilateralFilter(frame, 9, 75, 75)
    # # frame = cv2.equalizeHist(frame)
    # # frame = cv2.Canny(frame, 10, 80)
    # # frame = cv2.Laplacian(frame, cv2.CV_64F)
    # plt.subplot(1, 3, 2)
    # plt.imshow(frame)
    # # hog, vis = filters.gabor(frame, frequency=0.6,theta=45,n_stds=5)
    # # frame, hog = feature.hog(frame, visualize=True)
    # frame, hog = feature.hog(frame, orientations=9, pixels_per_cell=[8, 8], cells_per_block=[2, 2], visualize=True,
    #                   feature_vector=True)
    # plt.subplot(1, 3, 3)
    # plt.imshow(hog)
    # plt.show()
    time_log('over')
