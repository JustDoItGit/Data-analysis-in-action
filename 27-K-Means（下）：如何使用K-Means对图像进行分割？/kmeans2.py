# 使用K-means对图像进行聚类，显示分割标识的可视化
from load_data import load_data
import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans
from skimage import color

# 加载图像，得到规范化的结果img，以及图像尺寸
img, width, height = load_data('./weixin.jpg')

# 用K-Means对图像进行16聚类
kmeans = KMeans(n_clusters=16)
kmeans.fit(img)
label = kmeans.predict(img)
# 将图像聚类结果，转化成图像尺寸的矩阵
label = label.reshape([width, height])
# 将聚类标识矩阵转化为不同颜色的矩阵
label_color = (color.label2rgb(label) * 255).astype(np.uint8)
label_color = label_color.transpose(1, 0, 2)
images = image.fromarray(label_color)
images.save('weixin_mark_color.jpg')
