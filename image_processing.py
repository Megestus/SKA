import cv2

def load_image(image_path):
    image = cv2.imread(image_path)
    return image

def process_image(image):
    # 进行图像处理，例如灰度化
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image
