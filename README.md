API Data Analysis Tool

一个基于 Python 的网络数据获取与分析工具，可以自动获取公开 API 数据，完成数据解析、统计分析和 Excel 文件导出。

1. 项目功能

- 使用 Requests 发送 HTTP GET 请求
- 使用 JSON 解析 API 返回数据
- 使用 Pandas 将数据转换为 DataFrame
- 统计文章总数
- 按用户 ID 统计文章数量
- 根据关键词筛选文章
- 自动导出 Excel 文件

2. 技术栈

- Python
- Requests
- Pandas
- JSON
- OpenPyXL

3. 项目结构

api-data-analysis-tool/
├── day7_analysis.py
├── README.md
├── requirements.txt
└── .gitignore

4. 环境安装

建议使用 Python 3.12。

安装依赖：

python -m pip install -r requirements.txt

5. 运行项目

python day7_analysis.py

6. 数据来源

项目使用 JSONPlaceholder 公开模拟 API：

https://jsonplaceholder.typicode.com/posts

该接口用于学习和测试，不提供真实业务数据。

7. 输出结果

程序运行后会自动生成 output 文件夹，包含：

- all_posts.xlsx：全部文章数据
- user_statistics.xlsx：用户文章数量统计
- keyword_posts.xlsx：关键词筛选结果

8. 学习目标

通过本项目练习 Python 网络请求、JSON 数据解析、Pandas 数据处理和 Excel 自动化导出。