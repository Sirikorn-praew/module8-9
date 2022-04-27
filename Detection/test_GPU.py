import tensorflow as tf
from tensorflow.python.client import device_lib
from keras.preprocessing import image
import numpy as np
import os
import cv2
def sort_dir(dirname):
	new = list()
	for file in os.listdir(dirname):
		if file.split('.')[0].isdigit():
			new.append(file)
	return sorted(new, key=lambda f: int(f.split('.')[0]))

def load_all_images(folder):
    images = []
    filenames = sort_dir(folder)
    list_of_filename=[]
    print('filenames',filenames)
    for filename in filenames:
        print(filename)
        img = cv2.imread(os.path.join(folder, filename))
        list_of_filename.append(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images,list_of_filename

class EfficientNetModel:
    def __init__(self, checkpoint_file_path, list_of_target_name, input_shape):
        #loading trained model
        self.checkpoint_file_path = checkpoint_file_path
        self.model = tf.keras.models.load_model(self.checkpoint_file_path)
        self.model.summary()
        self.target = sorted(list_of_target_name.copy())
        # print(self.target)
        self.input_shape = input_shape
    def read_image(self, image_path):
        return cv2.imread(image_path)
    def resize_image(self, image):
        return cv2.resize(image, (self.input_shape[1], self.input_shape[0]), interpolation=cv2.INTER_CUBIC)
    def make_prediction(self, image):
        resized_image = self.resize_image(image)
        image_array = np.array([resized_image])
        return tf.argmax(self.model.predict(image_array),axis = 1)
        
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
device_lib.list_local_devices()

file_crop_side='D:\Year4_2\module89\AI detection\Demo\side_crop/'
checkpoint_file_path='D:\Year4_2\module89\AI detection\Demo\checkpoint_hyper'
images,list_of_filename=load_all_images(file_crop_side)
input_shape=(380,380)
modelE4=EfficientNetModel(checkpoint_file_path, list_of_filename, input_shape)

ans=[]
for img in images :
    # image_to_predict = modelE4.read_image(name)
    # image_to_predict = modelE4.resize_image(image_to_predict)
    ans.append(modelE4.make_prediction(img))
    pred=tf.concat(ans, axis=0)
mappings = {0: 'e', 1: 'e', 2: 'k',3: 'n',4: 'p',5: 'q',6: 'r'}
pred=[mappings[i] for i in pred]

print('test',pred)
# test_image = image.load_img(file_crop_side, target_size = (380, 380)) 
# test_image = image.img_to_array(test_image)
# test_image = np.expand_dims(test_image, axis = 0)


# model=tf.keras.models.load_model('D:\Year4_2\module89\AI detection\Demo\checkpoint_hyper')
# print(model.summary())

# imageee = model.predict(test_image)

# print('predixt')
# print(imageee)