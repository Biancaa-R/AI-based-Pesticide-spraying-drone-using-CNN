from PIL import Image
import tensorflow as tf
import numpy as np
import os

class_names = ['Anthracnose', 'Bacterial_Canker', 'Bud_Root_Dropping', 'Bud_Rot', 'Cutting_Weevil', 'Die_Back', 'Gall_Midge', 'Gray_Leaf_Spot', 'Healthy', 'Leaf_Rot', 'Powdery_Mildew', 'Sooty_Mould', 'Stem_Bleeding']

from PIL import Image
import tensorflow as tf
import numpy as np

class_names = ['Anthracnose', 'Bacterial_Canker', 'Bud_Root_Dropping', 'Bud_Rot', 'Cutting_Weevil', 'Die_Back', 'Gall_Midge', 'Gray_Leaf_Spot', 'Healthy', 'Leaf_Rot', 'Powdery_Mildew', 'Sooty_Mould', 'Stem_Bleeding']

def loading(image_path):
    def image_path_to_np_array(image_path, target_size=(256, 256)):
        try:
            image = Image.open(image_path)
            image = image.resize(target_size)  # Resize the image to target size
            image_array = np.array(image)
            if image_array.shape[-1] == 4:
                image_array = image_array[:, :, :3]
            return image_array
        except Exception as e:
            print(f"Error: {e}")
            return None
    model_path = "E:/mine/ZENITH24/CD3.h5"  # Use forward slashes in file paths
    loaded_model = tf.keras.models.load_model(model_path, compile=False)
    
    img_array = image_path_to_np_array(image_path)
    if img_array is not None:
        img_array = np.expand_dims(img_array, 0)
        predictions = loaded_model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions[0])]
        confidence = round(100 * np.max(predictions[0]), 2)
        return predicted_class, confidence
    else:
        return None






