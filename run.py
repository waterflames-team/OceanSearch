"""
本地运行：python3 run.py
"""
import tornado.ioloop
import tornado.web
import platform

from core import bili, gitee

WhatOs = platform.system()

if WhatOs == "windows":  # win环境下判定
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
else:
    pass

post = 5418

class MainHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass
    def get(self):
        self.render("index.html")

class APIHandler(tornado.web.RequestHandler):  # 主api进程
    def get(self):
        """
        数据引入
        """
        tq = self.get_argument('q', None)  # 搜索内容
        tm = self.get_argument('m', None)  # 类型
        tn = self.get_argument('n', None)  # 索引顺序
        tn = int(tn)

        """
        视频
        """
        if tm == "bili":
            ex = {"code": 0,
                  "title": str(bili.search(tq, tn, "title")),
                  "arcurl": "https://www.bilibili.com/video/"+str(bili.search(tq, tn, "bvid")),
                  "author": str(bili.search(tq, tn, "author")),
                  "pic": str(bili.search(tq, tn, "pic")),
                  }
        if tm == "gitee":
            ex = {"code": 0,
                  "name": str(gitee.search(tq, tn, "human_name")),
                  "arcurl": "https://gitee.com/"+str(gitee.search(tq, tn, "full_name")),
                  "description": str(gitee.search(tq, tn, "escription")),
                  }
        else:
            ex = {"code": 1, "text": tq, "model": tm, "num": tn}
        self.write(ex)

settings = {
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "template_path": "web",
    "debug": True
}


# debug决定是否实时加载(即调试模式

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/api", APIHandler), #路径这里添加，每次复制一个class然后改个名在这里添加就好了
    ], **settings)


print("server run in http://localhost:" + str(post) + "/")

app = make_app()
app.listen(post)
tornado.ioloop.IOLoop.current().start()
