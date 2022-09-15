from tkinter import *


def mainMenu():
    root =Tk()#定义窗口
    root.title("人脸识别系统")#窗口吗名
    root.geometry("400x500")#窗口尺寸
    # photo = PhotoImage(file="/media/img/1.png")#定义图片路径
    # label = Label(root,image=photo)#用label控件添加图片
    # label.place(relx =0,rely=0,relwidth=1,relheight=1)#添加位置place，relx =x轴,rely=y轴,relwidth=宽度,relheight=高度)
    label2=Label(root,text="录入人脸",font=("楷体",30))#文本控件,先添加图片，后添加文字
    label2.pack(side=TOP)#文本停靠位置
    #label2.place(relx=0.3,rely=0.4)百分比计算文本位置
    entry =Entry(root)#输入框
    entry.place(relx=0.3,rely=0.3,relwidth=0.4,relheight=0.06)

    # fg文字颜色，bg背景颜色，activebackground点击状态颜色，bd边框宽度，command=lambdad:调用函数
    btn = Button(root,text="摄像头",font=30,fg="blue",bg="white",activebackground="purple",bd=10)#按钮组件
    btn.place(relx=0.3,rely=0.4,relwidth=0.4,relheight=0.1)

    btn2 = Button(root,text="处理数据", font=30, fg="blue", bg="white", activebackground="purple", bd=10)  # 按钮组件
    btn2.place(relx=0.3, rely=0.55, relwidth=0.4, relheight=0.1)

    btn3 = Button(root, text="识别人脸", font=30, fg="blue", bg="white", activebackground="purple", bd=10)  # 按钮组件
    btn3.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.1)

    root.mainloop()#加载窗口
mainMenu()



