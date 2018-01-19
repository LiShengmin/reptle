

# 主要思路是， 将标签存储在同一种数据结构中， 使用表来创建
from enum import Enum, unique

@unique
class UrlPropertyEnum(Enum):
    unknowLink = 00
    mainLink = 10
    tabLink = 20
    videoLink = 01

class UrlStatusEnum(Enum):
    isVisited = 0x1
    unVisited = 0x10

class Url(): 
    url = ''
    linkProperty = UrlPropertyEnum.unknowLink
    status = UrlStatusEnum.isVisited

    def setUrl(self, url):
        self.url = url
        # 这里需要处理相应的标签类型

    def hash(self):
        return hash(url)

