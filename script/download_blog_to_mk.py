import os
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Cookie': 'username_e963f322=byron;token_e963f322=e7db5ede952aa40fa43515f6966d846ec8d282eb7509f3a7808729de3a28fcc81698908433;addinfo=%7B%22chkadmin%22%3A1%2C%22chkarticle%22%3A1%2C%22levelname%22%3A%22%5Cu7ba1%5Cu7406%5Cu5458%22%2C%22userid%22%3A%221%22%2C%22useralias%22%3A%22byron%22%7D',
    'Accept': '*/*',
    'Host': 'blog.mgd2008.com',
    'Connection': 'keep-alive'
}

# 创建保存文件的目录
if not os.path.exists("./blog"):
    os.mkdir("./blog")

for id in range(1, 83):
    url = f"https://blog.mgd2008.com/zb_users/plugin/MQ_txt/save.php?act=download&id={id}&csrfToken=a3576308891c334c179ee89933df71da"
    response = requests.get(url, headers=headers)
    content_type = response.headers.get("Content-Type") or ""
    if "text" not in content_type:  # 判断响应的内容是否为文本，排除掉下载错误页面的情况
        filename_match = re.search('filename="([^"]+)"', response.headers.get("Content-Disposition", ""))
        if filename_match:
            file_name_txt = f"./blog/{filename_match.group(1)}"
            # 获取文件名和文件后缀
            file_name_without_ext, file_ext = os.path.splitext(file_name_txt)
            # 将文件后缀更改为 .md
            file_name = file_name_without_ext.encode('ISO-8859-1').decode('UTF8') + ".md"
        else:
            file_name = f"./blog/{id}.md"

        with open(file_name, "w", encoding="utf8") as f:
            f.write(response.text)
            # for chunk in response.iter_content(chunk_size=8192):  # 使用迭代的方式处理响应内容，以避免内存问题
            #     if chunk:
            #         f.write(response.text)
        print(f"ID为{id}，已下载文件：{file_name}")
    else:
        print(f"ID为{id}，文件下载失败")
