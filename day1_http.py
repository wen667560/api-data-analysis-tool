import requests 
#1.目标网址
#url="http://jsonplaceholder.typicode.com/posts/1"
url="http://jsonplaceholder.typicode.com/posts/2"
#2.向这个网址发送GET请求,并把服务器返回的响应保存到response
response=requests.get(url) 
#3.查看服务器返回的状态码,200请求成功，201创建成功，400请求错误，401未授权，403禁止访问，404资源不存在，500服务器内部错误
print("状态码：",response.status_code)
#4.查看服务器返回的内容，以文本形式显示
print("返回内容：")
print(response.text)
print("======")
print(response.text[:100])  #打印返回内容的前100个字符
