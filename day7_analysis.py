#网络数据自动获取与分析系统
import os
import requests
import pandas as pd

# =========================
# 1. 获取网络数据
# =========================

url = "https://jsonplaceholder.typicode.com/posts"

try:
    print("正在获取网络数据...")

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()

    if not data:
        print("没有获取到数据")
        raise SystemExit

    print("数据获取成功！")

    # =========================
    # 2. 转换成 DataFrame
    # =========================

    df = pd.DataFrame(data)

    print("原始数据行数：", df.shape[0])

    # =========================
    # 3. 数据整理
    # =========================

    df = df[["userId", "id", "title", "body"]]

    # =========================
    # 4. 统计文章总数
    # =========================

    total_posts = len(df)

    print("文章总数：", total_posts)

    # =========================
    # 5. 按用户统计文章数量
    # =========================

    user_statistics = (
        df.groupby("userId")
        .size()
        .reset_index(name="文章数量")
    )

    print("\n各用户文章数量：")
    print(user_statistics)

    # =========================
    # 6. 关键词筛选
    # =========================

    keyword = "qui"

    keyword_posts = df[
        df["title"].str.contains(keyword, case=False, na=False)
    ]

    print("\n包含关键词的文章数量：", len(keyword_posts))
    print(keyword_posts[["id", "title"]].head())

    # =========================
    # 7. 保存 Excel
    # =========================

    os.makedirs("output", exist_ok=True)

    df.to_excel("output/all_posts.xlsx", index=False)

    user_statistics.to_excel(
        "output/user_statistics.xlsx",
        index=False
    )

    keyword_posts.to_excel(
        "output/keyword_posts.xlsx",
        index=False
    )

    print("\n三个 Excel 文件已经生成！")

except requests.exceptions.Timeout:
    print("请求超时，请检查网络")

except requests.exceptions.ConnectionError:
    print("网络连接失败")

except requests.exceptions.HTTPError as e:
    print("HTTP 请求错误：", e)

except ValueError:
    print("JSON 解析失败")

except Exception as e:
    print("程序运行出错：", e)