from image_processing import load_image, process_image

def main():
    image_path = 'path/to/your/image.png'  # 替换为实际图像路径
    image = load_image(image_path)
    processed_image = process_image(image)
    cv2.imshow('Processed Image', processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
