import os 
import requests
import pandas as pd
#1.设置API地址
url="http://jsonplaceholder.typicode.com/posts"
#2.设置请求参数
params={"userId":1}
try:
    #3.发送GET请求
    response=requests.get(
        url,
        params=params,
        timeout=10
    )
    #4.检查HTTP状态码
    response.raise_for_status()
    #5.将JSON转换成python数据
    data=response.json()
    #6.判断是否获取到新数据
    if not data:
        print("没有获取到数据")
    else:
        #7.将数据转换为DataFrame
        df=pd.DataFrame(data)
        #8.只保留需要的三列
        df=df[["userId","id","title"]]
        #9.创建输出文件夹
        os.makedirs("output",exist_ok=True)
        #10.保存为Excel
        output_path="output/posts_user1.xlsx"
        df.to_excel(output_path,index=False)
        #11.显示分析结果
        print("数据获取成功！")
        print("数据行数：",df.shape[0])
        print("数据列数：",df.shape[1])
        print("数据预览：")
        print(df.head())
        print("Excel文件已保存到：",output_path)
except requests.exceptions.Timeout:
    print("请求超时，请检查网络")
except requests.Exceptions.Timeout:
    print("连接失败，请检查网络连接")
except requests.Exceptions.HTTPError:
    print("HTTP请求错误：",e)
except ValueError:
    print("JSON数据解析失败")
except Exception as e:
    print("程序出现其他错误：",e)

