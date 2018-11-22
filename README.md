# Scrapy-Test

## Spider

### 执行顺序

1. 第一个被执行的函数是 `start_requests()`，如果不指定这个函数的话，将根据 `start_urls` 的值自动启动。
2. 迭代下载页面。
3. 在回调函数中，使用指定的解析器解析页面。
4. 数据保存到数据库中（使用 `item Pipeline`）或者写入文件。

### start_requests

`start_requests` 函数必须返回一个迭代器，整个过程中只会执行一次。

### parse

`parse(response)`，默认的回调函数，必须返回可迭代的 `Request` 或者 `Item` 对象。

### close

Spider 关闭时调用。

## Spider arguments

Scrapy 可以在 `crawl` 时添加 `-a` 选项，用于提供一些初始化时的参数。

Spider 可以在 `__init__` 中获得这些参数：

```bash
scrapy crawl myspider -a category=electronics
```

```python
import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'

    def __init__(self, category=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.example.com/categories/%s' % category]
        # ...
```

或者也可以写成这样：

```python
import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'

    def start_requests(self):
        yield scrapy.Request('http://www.example.com/categories/%s' % self.category)
```

需要注意，通过 `-a` 添加的参数只是字符串，如果不明确地对其进行解析的话，那么它毫无意义。
