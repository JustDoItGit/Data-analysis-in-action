from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np


# 生成词云
def create_word_cloud(f):
    print('根据词频计算词云')
    text = ' '.join(jieba.cut(f, cut_all=False, HMM=True))
    wc = WordCloud(
        font_path='./SimHei.ttf',
        max_words=100,
        width=2000,
        height=1200,
    )
    wordcloud = wc.generate(text)
    # 写词云图片
    wordcloud.to_file('wordcloud.jpg')
    # 显示词云文件
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


f = '数据分析全景图及修炼指南\
学习数据挖掘的最佳学习路径是什么？\
Python基础语法：开始你的Python之旅\Python科学计算：NumPy\
Python科学计算：Pandas\学习数据分析要掌握哪些基本概念？\
用户画像：标签化就是数据的抽象能力\
数据采集：如何自动化采集数据？\
数据采集：如何用八爪鱼采集微博上的“D&G”评论？\
Python爬虫：如何自动化下载王祖贤海报？\
数据清洗：数据科学家80%时间都花费在了这里？\
数据集成：这些大号一共20亿粉丝？\
数据变换：大学成绩要求正态分布合理么？\
数据可视化：掌握数据领域的万金油技能\
一次学会Python数据可视化的10种技能'

create_word_cloud(f)


# 去掉停用次
def remove_stop_words(f):
    stop_words = ['学会', '就是', '什么']
    for stop_word in stop_words:
        f = f.replace(stop_word, '')
    return f


f = remove_stop_words(f)
create_word_cloud(f)
