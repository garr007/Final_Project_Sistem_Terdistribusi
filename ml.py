import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

# Memuat model
model = tf.keras.models.load_model('model_rockpaperscissors_classification_tf')

# Gantilah dengan path gambar yang sesuai
path = "rock.png"
img = image.load_img(path, target_size=(150, 150))

imgplot = plt.imshow(img)
plt.show()

x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
images = np.vstack([x])

# Memprediksi kelas
classes = model.predict(images, batch_size=10)
predicted_class = np.argmax(classes)
print(predicted_class)

# Menentukan label kelas
if predicted_class == 0:
    label = 'paper'
elif predicted_class == 1:
    label = 'rock'
elif predicted_class == 2:
    label = 'scissors'

print(label)
