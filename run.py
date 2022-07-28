"""
本地运行：python3 run.py
"""
import tornado.ioloop
import tornado.web
import json
import platform

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
        text = self.get_argument('q', None)  # 必须的module项

        """
        判定
        """
        if text == "test":
            ex = {
                "state": 200,
                "data": True,
            }
        else:
            ex = {
                "error": None
            }
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
