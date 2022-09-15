import cv2

def videoFace():
    # 1.jpg  2.jpg 3.jpg 4.jpg.....
    name = 1
    # 0--允许调用本地摄像头
    video = cv2.VideoCapture(0)
    # 人脸数据对比包
    faceData = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    while(True):
        # flag是否获取到了人脸
        # videoImg每一帧的人脸画面
        flag,videoImg = video.read()
        # 1水平翻转 0垂直翻转  -1垂直+水平
        videoImg=cv2.flip(videoImg,1)
        # 对比每一帧脸
        face = faceData.detectMultiScale(videoImg)
        # print(face)
        # 循环人脸数据，绘制红方格
        for x,y,w,h in face:
            cv2.rectangle(videoImg,pt1=(x,y),pt2=(x+w,y+h),color=[0,0,255],thickness=2)
            # 判断，如果识别到人脸---如果数据不是元组
            if not isinstance(face,tuple):
                # 切片范围
                facePhont = videoImg[y:y+h,x:x+w]
                cv2.imwrite("/faces/2/%s.jpg"%name,facePhont)
                print("第%s张人脸保存成功"%name)
                name+=1

        # 展示窗口，摄像头亮了
        cv2.imshow("fei",videoImg)
        # 人的眼睛频率。1S获取24帧
        sup=cv2.waitKey(1000//24)
        # ascii值== 空格=32
        if(sup==32):
            print("窗口即将关闭")
            break
    # 跳出循环，销毁窗口
    cv2.destroyAllWindows()

videoFace()



