import cv2
import uuid
import os

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
    for t in cuts:
        filename = './captchas/kind1/cuts/' + str(uuid.uuid4()) + '.png'
        new_image = img[0:h, t[0]:t[1]]
        cv2.imwrite(filename, new_image)

if __name__ == "__main__":
    for file in os.listdir('./captchas/kind1/'):
        if file != 'cuts':
            filename = './captchas/kind1/' + file
            print(filename)
            Cut_image(filename)
    print('finished')
