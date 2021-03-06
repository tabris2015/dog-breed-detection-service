import cv2
import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds
from PIL import Image
from .utils import build_model, format_label


class Predictor(object):
    IMG_SIZE = 224
    def __init__(self, cats_dogs_file, dogs_file):
        self.dogs_file = dogs_file
        self.cats_dogs_file = cats_dogs_file
        # obtener etiquetas
        _, self.dogs_info = tfds.load(
            'stanford_dogs', with_info=True, as_supervised=True
        )
        _, self.cats_dogs_info = tfds.load(
            'cats_vs_dogs', with_info=True, as_supervised=True
        )
        # cargar modelos
        dogs_optimizer = tf.keras.optimizers.Adam(learning_rate=1e-2)

        self.cats_dogs_model = build_model(num_classes=2)
        self.cats_dogs_model.load_weights(self.cats_dogs_file)

        self.dogs_model = tf.keras.models.load_model(self.dogs_file, compile=False)
        self.dogs_model.compile(
            optimizer=dogs_optimizer, loss="categorical_crossentropy", metrics=["accuracy"]
        )
        print('iniciado Sercicio de prediccion')

    def predict_file(self, file, model, ds_info):
        img = np.array(Image.open(file).resize((self.IMG_SIZE, self.IMG_SIZE)), dtype=np.float32)
        pred = model.predict(img.reshape(-1, 224, 224, 3))
        if ds_info.features['label'].num_classes > 3:
            top3 = np.argsort(pred, axis=1)[0, -3:]
            for label in top3:
                print(f'{format_label(label, ds_info)}: {pred[0, label]}')
        pred_label = format_label(np.argmax(pred), ds_info)
        return pred_label

    def predict_img(self, img, model, ds_info, return_dict=False):
        img = img.resize((self.IMG_SIZE, self.IMG_SIZE))
        img = img.convert('RGB')
        img_array = np.asarray(img, dtype=np.float32)[:, :, :3]
        print(f'received size: {img.size} final size: {img_array.shape}')

        pred = model.predict(img_array.reshape(-1, 224, 224, 3))
        res_dict = {}
        if ds_info.features['label'].num_classes > 3:
            top3 = np.argsort(pred, axis=1)[0, -3:]
            for i, label in enumerate(top3):
                text = format_label(label, ds_info)
                confidence = pred[0, label]
                res_dict[str(3 - i)] = text + ': ' + str(confidence)
                print(f'{text}: {confidence}')

        pred_label = format_label(np.argmax(pred), ds_info)
        if return_dict:
            res_dict['main'] = pred_label
            return res_dict
        return pred_label

    def predict(self, img):
        res = self.predict_img(img, self.cats_dogs_model, self.cats_dogs_info)
        breed = {'main': 'cat '}
        if res == 'dog':
            breed = self.predict_img(img, self.dogs_model, self.dogs_info, return_dict=True)
        return {'animal': res, 'raza': breed}



class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



