# 使用K-means对图像进行聚类，并显示聚类压缩后的图像
from load_data import load_data
import PIL.Image as image
from sklearn.cluster import KMeans

# 加载图像，得到规范化的结果imgData，以及图像尺寸
img, width, height = load_data('./weixin.jpg')
# 用K-Means对图像进行16聚类
kmeans = KMeans(n_clusters=16)
label = kmeans.fit_predict(img)
# 将图像聚类结果，转化成图像尺寸的矩阵
label = label.reshape([width, height])
# 创建个新图像img，用来保存图像聚类压缩后的结果
img = image.new('RGB', (width, height))
for x in range(width):
    for y in range(height):
        c1, c2, c3 = kmeans.cluster_centers_[label[x, y]]
        img.putpixel((x, y), (int(c1 * 256 - 1), int(c2 * 256 - 1), int(c3 * 256 - 1)))
img.save('weixin_new.jpg')
