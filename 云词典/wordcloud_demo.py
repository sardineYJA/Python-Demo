import wordcloud
import matplotlib.pyplot as plt
from wordcloud import ImageColorGenerator

words_list = []
with open('words.txt', 'r', encoding='utf8') as fin:
    for line in fin.readlines():
        # line = line.strip('\n')  # 去掉符号\n
        words_list.append(line)

backgroud_Image = plt.imread('1.jpeg')
cloudobj = wordcloud.WordCloud(
    # font_path=myfont,     # 可传入本地安装的字体,若有中文代码必须，不然会出现方框
    width=1200,             # width,height图片宽高
    prefer_horizontal=0.5,  # 词语水平方向排版出现的概率
    height=800,
    mode='RGBA',            # 当参数为'RGBA' 并且backgroud_color不为空时，背景为透明
    background_color=None,
    stopwords='',           # 自定义的停用词，为空则使用内置
    max_words=3000,         # 要显示的词的最大个数
    random_state=30,        # 设置有多少种随机生成状态，即有多少种配色方案
    mask=backgroud_Image    # 背景图
).generate(' '.join(words_list))


# 改变字体颜色
img_colors = ImageColorGenerator(backgroud_Image)
# 字体颜色为背景图片的颜色
cloudobj.recolor(color_func=img_colors)

# cloudobj.to_file('save.png')
plt.axis('off')   # 是否显示x轴、y轴下标
plt.imshow(cloudobj)
plt.show()
