import os
import uuid
import cv2
import random
import string

def bin_img(filename):
    img = cv2.imread(filename, 0)
    ret, new_img = cv2.threshold(img, 175, 255, cv2.THRESH_BINARY)
    h, w = new_img.shape
    new_img = new_img[1:h-1, 1:w-1]
    return new_img

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
        if not flag and ver_li[i] > 0:
            left = i - 1
            flag = True
        if flag and ver_li[i] <= 0:
            right = i
            flag = False
            cuts.append((left, right))
    return cuts, h

def vertical2(img):
    h, w = img.shape
    ver_li = []
    for y in range(h):
        black = 0
        for x in range(w):
            if img[y, x] == 0:
                black += 1
        ver_li.append(black)
    bottom = 0
    top = 0
    flag = False
    for i in range(h):
        if not flag and ver_li[i] > 0:
            bottom = i
            flag = True
        if flag and ver_li[i] <= 0:
            top = i-1
            break
    return (bottom, top)

def Cut_image(img_name):
    img = bin_img(img_name)
    cuts, h = vertical(img)
    img_li = []
    for t in cuts:
        new_image = img[0:h, t[0]:t[1]]
        h, w = new_image.shape
        bottom, top = vertical2(new_image)
        new_image = new_image[bottom-1:top+1, 0:w]
        img_li.append(new_image)
    return img_li

def load_dataset():
    dataset = {}
    for key in range(10):
        li = []
        for i in range(5):
            file = random.choice(os.listdir('./captchas/kind2/cuts/'+str(key)))
            filename = './captchas/kind2/cuts/'+str(key)+'/'+file
            # li.append(cv2.imread(filename, 0))
            img = cv2.imread(filename, 0)
            h, w = img.shape
            bottom, top = vertical2(img)
            new_image = img[bottom - 1:top + 1, 0:w]
            li.append(new_image)
        dataset[key] = li
    for key in string.ascii_uppercase:
        li = []
        for i in range(5):
            file = random.choice(os.listdir('./captchas/kind2/cuts/'+str(key)))
            filename = './captchas/kind2/cuts/'+str(key)+'/'+file
            # li.append(cv2.imread(filename, 0))
            img = cv2.imread(filename, 0)
            h, w = img.shape
            bottom, top = vertical2(img)
            new_image = img[bottom-1:top+1, 0:w]
            li.append(new_image)
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
    print(recognize('./captchas/kind2/1eaa7103-382f-4ea6-8e27-f33504ca2c0b.png'))
