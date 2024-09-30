import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def show_image(image_path):
    img = load_img(image_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

# Show the image
show_image('dataset/user2/1726733385733.jpg')
