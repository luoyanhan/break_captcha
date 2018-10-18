import cv2
import uuid
import os

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
    # bottom, top = vertical2(img)
    for t in cuts:
        filename = './captchas/kind2/cuts/' + str(uuid.uuid4()) + '.png'
        # new_image = img[bottom-1:top, t[0]:t[1]]
        new_image = img[0:h, t[0]:t[1]]
        cv2.imwrite(filename, new_image)

if __name__ == "__main__":
    for file in os.listdir('./captchas/kind2/'):
        if file != 'cuts':
            filename = './captchas/kind2/' + file
            try:
                Cut_image(filename)
                # cv2.namedWindow('Im')
                # cv2.imshow('Im', cv2.imread(filename))
                # cv2.waitKey(0)
            except:
                print(filename)
    print('finished')
