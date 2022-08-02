# OceanSearch 百川搜索

## 介绍
一个整合多内容平台的搜索接口，目前整合了b站、gitee搜索。

因为个人能力有限，目前暂时使用的都是API，若有更多内容平台的api欢迎评论或参与贡献

## 安装教程
首先，你要确定你电脑中已安装 `python3`及`pip3`，然后你需要在命令行中执行一下命令，即可完成安装：

```shell
git clone https://gitee.com/waterflames-team/ocean-search.git
cd ocean-search
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

> 最后一步若执行失败，可以直接执行 `pip3 install tornado`

## 使用说明

### 1. 运行服务
你需要进入 `ocean-search` 目录下，然后运行：

```shell
python3 run.py
```

随后服务便会启动，运行的端口会在运行时打印出来

### 2. 参数使用
本项目使用 get 请求

#### 请求内容
| 参数  |  含义  | 类型  |      内容      | 必要性 |
|:---:|:----:|:---:|:------------:|:---:|
|  q  | 搜索内容 | str | 例：lingrobotx |  是  |
|  m  |  类别  | str |  bili/gitee  |  是  |
|  n  | 索引序号 | int |     例：1      |  是  |

#### 返回内容

##### bili
|   参数   |    含义    | 类型  |
|:------:|:--------:|:---:|
|  code  |   返回码    | int |
| title  |  搜索结果标题  | str |
| arcurl |  搜索结果链接  | str |
| author |  搜索结果作者  | str |
|  pic   | 搜索结果封面链接 | str |

##### Gitee
|     参数      |  含义  | 类型  |
|:-----------:|:----:|:---:|
|    code     | 返回码  | int |
|    name     | 仓库名  | str |
|   arcurl    | 仓库地址 | str |
| description | 仓库介绍 | str |



## 联系

如果遇到了问题，或者是有一个好建议，欢迎联系我们：

- 你可以选择 [戳我](https://gitee.com/waterflames-team/ocean-search/issues "Issues") 来创建一个issue
- 也可以通过邮箱联系我们：[hi@waterflames.cn](mailto:hi@waterflames.cn)
- 如果你是一名**开发者**，可以加入在兔小巢里和我们面对面交流 [https://support.qq.com/product/420726](https://support.qq.com/product/420726)。
- 如果你是一名**用户**，可以加入我们的用户群（QQ）：825288633。

## 二次开发

如果你准备将其闭源并商业使用，那么请确认你知晓 WaterFlames水焰 不为任何使用了二次分发软件的 安全性，可用性，完整性 以及其可能带来的 其它风险及损失 承担责任。

其余或有冲突之处以 Apache License 2.0 开源协议为准

## 代码贡献

我们欢迎每一位创作者加入本项目的开源贡献中。欢迎每一位贡献者创建pr，并按照 [提交信息规范](https://xykong.feishu.cn/wiki/wikcnhQ6Eti6VZQI2avsLTSofve) 来为项目进行贡献！

感谢每一位贡献者！

## 支持

由于WaterFlames的小伙伴们还是处于九年义务教育的学生党们 ~~还是群鸽子~~ ，所以本项目可能不会经常活跃

欢迎有开发者向这个项目发起pr，这是对水焰的最大鼓励

如果您觉得我们的开源软件对你有所帮助，可以向 WaterFlames赞助,戳这里 -> [http://afdian.net/@epeiuss](http://afdian.net/@epeiuss)


<p align="center">
    <img src="./photo/afd.png" alt="爱发电二维码" width="200" height="275.2">
</p>


> 我们不营利，所有资金将花费到服务器与域名的购买，以及之后项目的制作中

## 加入我们

我们是一个非盈利的开源团队，无论您是否会编程，我们都欢迎您加入我们，与我们一起打造惊人的产品：
[https://xykong.feishu.cn/share/base/shrcnwMMP9rBl5aK6qJqaXc3Jph](https://xykong.feishu.cn/share/base/shrcnwMMP9rBl5aK6qJqaXc3Jph)