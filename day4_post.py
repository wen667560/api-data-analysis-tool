###第一次发送POst请求，提交数据，放在请求正文body,requests.post()
import requests
#1.设置接口地址
url="https://jsonplaceholder.typicode.com/posts"
#2.准备要提交的数据
data={
    "title":"我的第一条测试文章",
    "body":"这是我使用python发送post请求提交的数据。",   #文章内容
    #"userId":1    #用户编号
    "userId":2
}

#3.发送POST请求
response=requests.post(url,json=data,timeout=10)#或data=data提交表单数据或指定的请求正文；json=data以JSON格式提交数据
#4.查看状态码
print("状态码：",response.status_code)
#5.查看服务器返回的数据
#print("服务器返回的数据：")
#print(response.text)

result=response.json()
print("返回的数据：",result)
print("文章Id",result["id"])
print("文章标题",result["title"])
print("用户ID",result["userId"])