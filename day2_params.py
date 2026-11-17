#######使用params传递参数
import requests
#1.设置接口地址
url="https://jsonplaceholder.typicode.com/posts"
#2.设置参数请求
params={"userId":1}
#params={"userId":1,"id":2} ##同时传递多个参数
#请求头
headers={
    "User-Agent":
    "MyPythonLearningProject/1.0","Accept":"application/json"
}

#3.发送GET请求
response=requests.get(url,params=params,headers=headers,timeout=10) #timeout是请求时间
#4.查看最终请求网址
print("请求网址：")
print(response.url)
#5.查看状态码
print("状态码：",response.status_code)
#6.查看返回内容
print("服务器返回的数据：")
print(response.text)