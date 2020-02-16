from keras.models import load_model
from keras.datasets import mnist
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import random

(x_train, y_train), (x_test, y_test) = mnist.load_data()

model = load_model('./save/minst_model.h5')
for i in range(10):
    image_index = random.randrange(x_test.shape[0])
    plt.imshow(x_test[image_index].reshape(28, 28),cmap='Greys')
    plt.show()
    pred = model.predict(x_test[image_index].reshape(1, 28, 28, 1))
    print(pred.argmax())

