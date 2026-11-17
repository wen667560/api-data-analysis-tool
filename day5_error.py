#try:尝试执行肯出现错误的代码
#   try:
#       number=int(input("请输入一个数字："))
#       print("你输入的数字是：",number)
#except 如果发生指定异常，就执行这里的代码
#   except ValueError:
#       print("输入错误！请输入数字。")
#       print("程序继续运行。")

#############################################

"""########处理网络请求超时
import requests
url="https://jsonplaceholder.typicode.com/posts/1"
try:
    response=requests.get(url,timeout=5)
    print("请求成功！")
    print("状态码：",response.status_code)
    print("返回内容：",response.text)
except requests.exceptions.Timeout:
    print("请求超时，服务器响应太慢.")
except requests.exceptions.ConnectionError:
    print("网络连接失败，请检查网络.")
except requests.exceptions.RequestException as e:
    print("请求发生错误",e)
print("程序运行结束。")
"""

#########################################################3

"""#理解HTTP状态码和raise_for_status()
import requests
url="https://jsonplaceholder.typicode.com/posts/9999"
try:
    response=requests.get(url,timeout=5)
    #如果是状态码是4xx或5xx九抛出异常
    response.raise_for_status()
    print("请求成功！")
    print(response.json())
except requests.exceptions.HTTPError as e:
    print("服务器返回HTTP错误：",e)
except requests.exceptions.Timeout:
    print("请求超时，服务器响应太慢.")
except requests.exceptions.RequestException as e:
    print("网络请求失败",e)
print("程序运行结束。")
"""
####################################

#检查JSON解析是否成功
import requests
url="https://jsonplaceholder.typicode.com/posts/1"
try:
    response=requests.get(url,timeout=5)
    response.raise_for_status()#检查HTTP错误
    data=response.json()#解析数据
    print("文章标题",data["title"])
except requests.exceptions.Timeout:
    print("请求超时，服务器响应太慢.")
except requests.exceptions.RequestException as e:
    print("网络请求失败",e)
except ValueError: #用于捕获JSON解析过程中可能出现的解码错误
    print("返回的数据是不合法的JSON!")
