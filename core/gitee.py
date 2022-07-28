import requests
import json

def search(text, number, which):

    print("gitee 函数开始运行")
    url = "https://gitee.com/api/v5/search/repositories"
    params = {"q": text}

    res = requests.get(url=url, params=params)
    res = res.text
    res = json.loads(res)

    '''
    code = res["code"]
    if code == 0:
        print("bili 返回正常")

    result = res["data"]["result"]
    video_list = result[10]["data"] #获取视频结果列表
    '''
    res = res[number][which]
    return res
#TODO KeyError: 'escription'

# https://gitee.com/api/v5/swagger#/getV5SearchRepositories