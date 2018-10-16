import cv2
import os
import random


def vertical(img):
    h, w = img.shape
    ver_li = []
    for x in range(w):
        black = 0
        for y in range(h):
            if img[y, x] == 0:
                black += 1
        ver_li.append(black)
    left = 0
    right = 0
    flag = False
    cuts = []
    for i in range(w):
        if not flag and ver_li[i] > 1:
            left = i - 1
            flag = True
        if flag and ver_li[i] < 1:
            right = i
            flag = False
            cuts.append((left, right))
    return cuts, h

def Cut_image(img_name):
    img = cv2.imread(img_name, 0)
    ret, img = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY_INV)
    cuts, h = vertical(img)
    image_li = []
    for t in cuts:
        new_image = img[0:h, t[0]:t[1]]
        image_li.append(new_image)
    return image_li

def load_dataset():
    dataset = {}
    for key in range(10):
        li = []
        for i in range(10):
            file = random.choice(os.listdir('./captchas/kind1/cuts/'+str(key)))
            filename = './captchas/kind1/cuts/'+str(key)+'/'+file
            li.append(cv2.imread(filename, 0))
        dataset[key] = li
    return dataset

def cal_distances(img1, img2):
    distance = 0
    h = min(img1.shape[0], img2.shape[0])
    w = min(img1.shape[1], img2.shape[1])
    for i in range(w):
        for j in range(h):
            if img1[j, i] != img2[j, i]:
                distance += 1
    return distance

def knn(img, dataset, k):
    distance_li = []
    for key, li in dataset.items():
        for im in li:
            dis = cal_distances(img, im)
            distance_li.append((key, dis))
    distance_li.sort(key=lambda x: x[1])
    label_count = {}
    for i in range(k):
        key = distance_li[i][0]
        label_count[key] = label_count.get(key, 0) + 1
    return max(label_count.items(), key=lambda x: x[1])[0]

def recognize(file):
    dataset = load_dataset()
    img_li = Cut_image(file)
    code = ''
    for img in img_li:
        code += str(knn(img, dataset, 5))
    return code



if __name__ == "__main__":
    print(recognize('./captchas/kind1/08e78c89-0930-4c8e-9ffe-b13465f2e94a.png'))