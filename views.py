from django.shortcuts import render
import cv2
import os
import numpy
import  tkinter.messagebox#提示框
import tkinter.messagebox#提示框
from sklearn.model_selection import  train_test_split#机器学习库
from sklearn.neighbors import  KNeighborsClassifier#判断邻近值
from face02 import loadData
from .models import enteriModel

# Create your views here.
from django.http import  HttpResponse#引入http协议，响应函数
from .models import  newsModel
# 视图函数
def welcome(request):
    # return  HttpResponse("ABCD")#返回字符串
    return render(request,"page.html")#返回一个网页

def facesShow(request):
    di =len(os.listdir("C:/day004/faces"))
    os.mkdir("C:/day004/faces/%s" %di)

    name = 1
    # 0--允许调用本地摄像头
    video = cv2.VideoCapture(0)
    # 人脸数据对比包
    faceData = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    while (True):
        # flag是否获取到了人脸
        # videoImg每一帧的人脸画面
        flag, videoImg = video.read()
        # 1水平翻转 0垂直翻转  -1垂直+水平
        videoImg = cv2.flip(videoImg, 1)
        # 对比每一帧脸
        face = faceData.detectMultiScale(videoImg)
        # print(face)
        # 循环人脸数据，绘制红方格
        for x, y, w, h in face:
            cv2.rectangle(videoImg, pt1=(x, y), pt2=(x + w, y + h), color=[0, 0, 255], thickness=2)
            # 判断，如果识别到人脸---如果数据不是元组
            if not isinstance(face, tuple):
                # 切片范围
                facePhont = videoImg[y:y + h, x:x + w]
                cv2.imwrite("C:/day004/faces/%s/%s"%(di,name), facePhont)
                print("第%s张人脸保存成功" % name)
                name += 1
        cv2.imshow("lururenlian", videoImg)
        sup = cv2.waitKey(1000 // 24)
        if (sup == 32):
            print("窗口即将关闭")
            break
    cv2.destroyAllWindows()
    return HttpResponse("<script type='text/javascript'>alert('发布成功');window.location=document.referrer;</script>")
def showFaceClear(request):
    # 判断faces文件夹下有多少个文件
    di = os.listdir("faces/")
    # 循环人数读取
    for ren in range(len(di)):
        # print(ren)
        # 获取0文件夹下的所有图片
        dirs = os.listdir("faces/%s/"%ren)
        # 导入人脸数据特征包
        faceData = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
        # 循环每一张人脸 1-142
        for i in range(1,len(dirs)+1):
            # print(i)
            # 读取人脸数据
            img = cv2.imread("faces/%s/%s.jpg"%(ren,i))
            # 对比脸
            face = faceData.detectMultiScale(img,scaleFactor=1.1,minNeighbors=5)
            # print(face)
            # 如果数据是元组，删除根目录下的图片
            if isinstance(face,tuple):
                try:
                    os.remove("faces/%s/%s.jpg"%(ren,i))
                    print(ren,i)
                except:
                    pass
            else:
                pass
        nameList=[]
        # 再取一次文件夹数据(文件夹数据已经发生变化)
        dirs = os.listdir("faces/%s/"%ren)
        # "1.jpg" "2.jpg"... ["88","jpg"]
        for d in dirs:
            # 提取数字，装入列表
            nameList.append(int(d.split(".")[0]))
            # aa = d.split(".")
            # print(aa)
        # print(nameList)
        # 使用numpy处理nameList
        # 数据本身不会变，变成numpy类型以后，可以使用更多方法
        npNameList=numpy.array(nameList)
        # 大于100 True  小于100  Flase
        flag = npNameList>100
        # print(flag)
        # 大于100
        moreThan100 = npNameList[flag]
        # 小于等于100  1 3 56789   123456789 range(1,101)
        lessThan100 = npNameList[npNameList<=100]
        # 生成1-100序列，作为对比参照物
        comTo100 = numpy.arange(1,101)
        # 将小于100的序列对比，查出缺失
        loseName = list(set(comTo100).difference(lessThan100))
        print(loseName)
        # 处理大于100的数据
        # 枚举，大于100补给小于100，剩下删掉
        for i,file in enumerate(moreThan100):
            try:
                # 将大于100补给小于100，修改名字
                os.rename("faces/%s/%s.jpg"%(ren,file),"faces/%s/%s.jpg"%(ren,loseName[i]))
                # 补过的图片从列表里面删掉
                loseName.remove(loseName[i])
            except:
                # 多余的图片删掉
                os.remove("faces/%s/%s.jpg"%(ren,file))
        # 剩下的图片不够补齐100
        for i in loseName:
            # 每次随机在已有的图片中取一张
            ranName = numpy.random.choice(lessThan100,size=1)[0]
            # 将随机图片从文件夹读取出来
            img = cv2.imread("faces/%s/%s.jpg"%(ren,ranName))
            # 将改过名字的图片写入文件夹
            cv2.imwrite("faces/%s/%s.jpg"%(ren,i),img)
        for i in comTo100:#循环读取100张图片
            img = cv2.imread("faces/%s/%s.jpg"%(ren,i))
            newImg = cv2.resize(img,dsize=(64,64))#修改图片尺寸，统一改成64*64
            cv2.imwrite("faces/%s/%s.jpg"%(ren,i),newImg)
        print("第%s人数据处理完毕"%(ren+1))
        tkinter.messagebox.showinfo("提示","第%s人数据处理完毕"%(ren+1))
    tkinter.messagebox.showinfo("提示","数据处理完毕")
    return HttpResponse("<script type='text/javascript'>alert('发布成功');window.location=document.referrer;</script>")
def faceShowData(request):
    # xtrain用来训练的人脸   xtest用来测试的人脸
    # ytrain标记训练人脸     ytest标记测试人脸
    xtrain, xtest, ytrain, ytest = loadData()
        # 所有人的名字，按照人脸数据包顺序
    label = ["小飞", "镜玄", "xiaofei"]
        # 算法，临近值
    knn = KNeighborsClassifier(3)
        # 开始训练，训练过的脸标记
    knn.fit(xtrain, ytrain)
        # 测试人脸
    startKnn = knn.predict(xtest)
        # 可视化窗口，循环测试
    for i in range(30):
            # 自定义窗口
        cv2.namedWindow("who", flags=cv2.WINDOW_NORMAL)
            # 窗口尺寸
        cv2.resizeWindow("who", width=300, height=300)
            # 显示测试图片，显示照片像素
        cv2.imshow("who", xtest[i].reshape(64, 64))
        print("这是：", label[startKnn[i]])
        tkinter.messagebox.showinfo("这是：", label[startKnn[i]])  # 用提示框来展示名字
        spa = cv2.waitKey()
        if (spa == 32):
            print("人脸识别系统即将关闭")
            break
    cv2.destroyAllWindows()
    return HttpResponse("<script type='text/javascript'>alert('发布成功');window.location=document.referrer;</script>")
def zhuce(request):
    if request.method == "POST":
        xing = request.POST["xingming"]
        xue = request.POST["xuehao"]
        dian = request.POST["dianhua"]
        mi = request.POST["mima"]
        gen = request.POST["gender"]
        jian = request.POST["jianjie"]
        src = request.FILES["src"]
        # 上传一个文件，分成两个部分保存
        # 即：文件本身存在项目文件夹，图片路径存入数据库src
        # m = myModel(newstitle=title, newscon=con)

        # src = models.FileField(upload_to="images")
        m = enteriModel(xingming=xing,xuehao=xue,dianhua=dian,mima=mi,gender=gen,jianjie=jian,src=src)
        # n = enterModel(xingming=xing, xuehao=xue, dianhua=dian, mima=mi)
        m.save()
        return HttpResponse("<script type ='text/javascript'>alert('注册成功');window.location.href='denglu'</script>")

    return render(request,"page.html")
def denglu(request):
    # global data
    # enter = request.POST["xuehao"]
    # print(enter)
    if request.method == "POST":
        enterXuehao = request.POST["xuehao"]
        enterMima = request.POST["mima"]
        orNo = enteriModel.objects.filter(xuehao=enterXuehao)

        if orNo:
            user = orNo[0]
            if user.mima == enterMima:
                return HttpResponse("<script type='text/javascript'>alert('登陆成功');window.location.href='private';</script>")
            else:
                return HttpResponse("<script type='text/javascript'>alert('密码有误');window.history.back();</script>")
        else:
            return HttpResponse("<script type='text/javascript'>alert('用户不存在，请注册');window.location.href='zhuce';</script>")

    # data = enteriModel.objects.get(newstitl="%s" %)
    return render(request,"home.html")
def private(request):
    allData = enteriModel.objects.all()
    return render(request,"newsList.html",{"allData":allData})
def resAjax(request):
    # 从HTML页面获取用户名
    xuehao = request.POST["xuehao"]
    # 根据post请求过来的xuehao去数据库查询
    res = enteriModel.objects.filter(xuehao=xuehao)
    return HttpResponse(res)