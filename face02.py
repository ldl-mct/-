print("人脸训练")
import tkinter.messagebox#提示框
import cv2
import  numpy
from sklearn.model_selection import  train_test_split#机器学习库
from sklearn.neighbors import  KNeighborsClassifier#判断邻近值


def loadData():
    list = []  # 存放所有人的人脸数据
    for i in range(3):  # 读取每个人
        for j in range(1, 101):  # 读取每一个的每一张脸
            img = cv2.imread("faces/%s/%s.jpg" % (i, j))
            grayImg = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)  # 降维，三维降二维，彩色变黑白
            list.append(grayImg)  # 将处理过的图片装入列表
        # print(list)
    faceList = []  # 标记人脸
    for i in range(3):
        faceList.append(i)
    faceList = faceList * 100  # 扩张100倍
    faceList = sorted(faceList)  # 按照每个人排序
    print(faceList)
    list = numpy.array(list)  # 转换numby类型
    faceList = numpy.array(faceList)
    list = list.reshape(300, 4096)  # 300张人脸，64*64=4096像素
    return train_test_split(list, faceList, test_size=0.1)  # 数据拆分，总共300张图片，90%训练270张，10%测试30张


