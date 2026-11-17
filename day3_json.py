########第一次解析JSON

#一篇文章的数据是一个字典
#多篇文章的数据是一个列表
#列表中包含多个字典
import requests 
#1.目标网址
url="http://jsonplaceholder.typicode.com/posts/1"#posts包含多个文章
#2.向这个网址发送GET请求,并把服务器返回的响应保存到response
response=requests.get(url,timeout=10) 
#3.查看服务器返回的状态码,200请求成功，201创建成功，400请求错误，401未授权，403禁止访问，404资源不存在，500服务器内部错误
print("状态码：",response.status_code)
#4.将JSON数据解析成Python数据
data=response.json()
#5.查看数据
print("解析后的数据：")
print(data)
#6.查看数据类型
print("数据类型：",type(data))##list#len(data)查看数据数量
# print(data[0])查看第一篇文章,data[1]["title"]第二篇标题
##字典["键名"]
print("用户ID：",data["userId"])
print("文章id：",data["id"])
print("文章标题：",data["title"])
print("文章内容：",data["body"])


#遍历所有文章
#for post in data:       #依次从data列表中取出一篇文章，每次取出的内容放进post
#   print("文章ID："post["id"])
#   print("文章标题："post["title"])

#筛选特定用户的文章
#print("\n用户ID为1的文章：")
#for post in data:
#   if post["userId"]==1:
#       print(post["title"])

#for post in data[:5]:遍历前5篇文章