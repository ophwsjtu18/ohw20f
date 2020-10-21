from cv2 import cv2

# 4.1 读取图像
imagePath = './zhihu.jpg'
image = cv2.imread(imagePath, 0)

# 4.2 显示图像
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4.3 保存图像
savePath = './save.jpg'
cv2.imwrite(savePath, image)  # 按s保存，Esc退出但不保存
