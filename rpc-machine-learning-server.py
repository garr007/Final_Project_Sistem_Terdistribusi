#import package yang dibutuhkan
from xmlrpc.server import SimpleXMLRPCServer
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

#function machine learning 
def rpsClassification(path) :
    #load model yang telah dilatih sebelumnya di collab
    model = tf.keras.models.load_model('model_rockpaperscissors_classification_tf')

    img = image.load_img(path, target_size=(150, 150))

    #menampilkan gambar
    imgplot = plt.imshow(img)
    plt.show()

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])

    # Memprediksi kelas
    classes = model.predict(images, batch_size=10)
    predicted_class = np.argmax(classes)

    # Menentukan label kelas
    if predicted_class == 0:
        label = 'paper'
    elif predicted_class == 1:
        label = 'rock'
    elif predicted_class == 2:
        label = 'scissors'

    #Mengembalikan hasil
    return label
    
    
#mengatur koneksi RPC sebagai server
server = SimpleXMLRPCServer(("192.168.56.1",5000),allow_none=True)

#Status server
print("Server is Listening on Port 5000 ....")

#register function yang bisa diakses oleh client
server.register_function(rpsClassification)

#Menjalankan server
server.serve_forever()