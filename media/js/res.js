// 获取元素
// querySelector通过name属性获取元素
// 密码框
var passLabel = document.querySelector("[name=mima]");
// 密码框下面的提示信息
var passTxt = document.getElementById("passTxt");
// 鼠标失去焦点事件
passLabel.onblur = function () {
    if(passLabel.value.length <6 || passLabel.value.length>12){
        passTxt.innerHTML = "您的密码长度有误,建议密码长度6-12位";
    }else {
        passTxt.innerText = "";
    }
}

// 两次密码不一致---确认密码
repassLabel = document.getElementById("repassword");
repassTxt = document.getElementById("repassTxt");
repassLabel.onblur = function () {
    if (passLabel.value!=repassLabel.value){
        repassTxt.innerHTML = "您的两次密码不一致,请查正";
    } else {
        repassTxt.innerHTML = "";
    }
}

// 用户名是否有空格
var userLabel = document.querySelector("[name=username]");
var userTxt = document.getElementById("userTxt");
userLabel.onblur = function () {
    // 清除用户名里的空格----正则表达式清除空格
    var userCount = (userLabel.value).replace(/\s*/g,"");
    // 取清除空格后长度
    var userL = userCount.length;
    // 不清除空格的长度
    var userC = userLabel.value.length;
    if(userL != userC){
        userTxt.innerHTML = "您的用户名中有空格,请清除";
    }else {
        // userTxt.innerHTML = "";
    // 验证用户名是否可用  username=老王
    // 构建出需要提交后台的数据格式
    var data = "username="+userLabel.value
    // 1.创建ajax对象
    var  xhr = new XMLHttpRequest()
    // 2.对ajax状态进行监听
    xhr.onreadystatechange = function () {
        // 1 --- 正在发送请求
        // 2 --- 请求发送完毕
        // 3 --- 正在解析响应
        // 4 --- 内容解析完毕（成功）
        if(xhr.readyState==4 && xhr.status==200){
            // 请求验证的数据存在数据库里
            if(xhr.responseText){
                // 用户名已存在
                userTxt.innerHTML = "用户名已存在";
            }else {
                // 用户名不存在，可以用
                userTxt.innerHTML = "";
            }
        }
    }
    // 3.创建连接 open("请求方式","处理程序",打开异步)
    xhr.open("post","resAjax",true)
    // 4.设置请求头，代表前后端数据交互格式
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded")
    // 5.发送数据
    xhr.send(data)
    }


}

// 阻止事件---提交按钮
var btn = document.querySelector("[type=submit]");
// 点击事件
btn.onclick=function (e) {
    if(passTxt.innerHTML !="" || repassTxt.innerHTML !="" || userTxt.innerHTML!=""){
            e.preventDefault();
    }
    if(passLabel.value.length==0 || repassLabel.value.length==0 || userLabel.value.length==0){
            e.preventDefault();
    }
}
