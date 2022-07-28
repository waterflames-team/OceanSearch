import requests
import json

def search(text, number, which):

    print("bili 函数开始运行")
    url = "http://api.bilibili.com/x/web-interface/search/all/v2"
    params = {"keyword": text}

    res = requests.get(url=url, params=params)
    res =  res.text
    res = json.loads(res)

    code = res["code"]
    if code == 0:
        print("bili 返回正常")

    result = res["data"]["result"]
    video_list = result[10]["data"] #获取视频结果列表

    return video_list[number][which]

# https://github.com/SocialSisterYi/bilibili-API-collect/