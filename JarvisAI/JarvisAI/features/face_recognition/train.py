import matplotlib.pyplot as plt
import os
import warnings

warnings.simplefilter("ignore")
import pathlib
import glob
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential


class Classifier:
    def __init__(self, data_dir='datasets', batch_size=32, img_height=128, img_width=128, epochs=10,
                 model_path='model'):
        self.data_dir = pathlib.Path(data_dir)
        self.image_count = len(list(glob.glob(data_dir + '/*/*.png')))
        self.batch_size = batch_size
        self.img_height = img_height
        self.img_width = img_width
        self.num_classes = len(os.listdir(pathlib.Path(data_dir)))
        self.class_names = None
        self.train_ds = None
        self.val_ds = None
        self.epochs = epochs
        self.data_augmentation = None
        self.model_path = model_path

    def dataloader(self):
        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            self.data_dir,
            validation_split=0.2,
            subset="training",
            seed=123,
            image_size=(self.img_height, self.img_width),
            batch_size=self.batch_size)

        val_ds = tf.keras.preprocessing.image_dataset_from_directory(
            self.data_dir,
            validation_split=0.2,
            subset="validation",
            seed=123,
            image_size=(self.img_height, self.img_width),
            batch_size=self.batch_size)

        self.class_names = train_ds.class_names
        self.train_ds = train_ds
        self.val_ds = val_ds

    def data_augmentation_fun(self):
        data_augmentation = keras.Sequential(
            [
                layers.experimental.preprocessing.RandomFlip("horizontal",
                                                             input_shape=(self.img_height,
                                                                          self.img_width,
                                                                          3)),
                layers.experimental.preprocessing.RandomRotation(0.1),
                layers.experimental.preprocessing.RandomZoom(0.1),
            ]
        )
        self.data_augmentation = data_augmentation

    def model_create(self):
        self.data_augmentation_fun()
        model = Sequential([
            self.data_augmentation,
            layers.experimental.preprocessing.Rescaling(1. / 255, input_shape=(self.img_height,
                                                                               self.img_width, 3)),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(self.num_classes)
        ])

        model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])
        return model

    def train(self, model):
        history = model.fit(
            self.train_ds,
            validation_data=self.val_ds,
            epochs=self.epochs
        )
        if not os.path.exists(self.model_path):
            os.makedirs(self.model_path)

        model.save(f'{self.model_path}/model.h5')
        return history

    def visualize_results(self, history):
        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']

        loss = history.history['loss']
        val_loss = history.history['val_loss']

        epochs_range = range(self.epochs)

        plt.figure(figsize=(8, 8))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')
        plt.show()

    def start(self):
        self.dataloader()
        print("Dataset Dir: ", self.data_dir)
        print("Number of class: ", self.num_classes)
        print("Total Images: ", self.image_count)
        print("batch_size: ", self.batch_size)
        print("img_width: ", self.img_width)
        print("img_height: ", self.img_height)
        print("class_names: ", self.class_names)
        print("Model Directory: ", self.model_path + '/model.h5')
        print("================================================")
        print("================= Starting Training =================")
        model = self.model_create()
        model.summary()
        history = self.train(model)

        self.visualize_results(history)


if __name__ == '__main__':
    obj = Classifier()
    obj.start()
