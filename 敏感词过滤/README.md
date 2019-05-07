## 敏感词过滤：
1.敏感词文件存放路径：在当前文件夹:/data/sensitive_words.txt中，以换行符区分

测试代码：
import time
gfw = DFAFilter()                         # 过滤敏感词类
gfw.parse("./data/sensitive_words.txt")   # 加载敏感词文件（已默认设置，可以自定义加载敏感词）
t = time.time()
print(gfw.filter("法轮功 我操操操", "*"))  # 运行敏感词检测替换函数
print(gfw.filter("傻逼xxx"))
print(time.time() - t)