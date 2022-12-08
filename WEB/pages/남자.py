import streamlit as st
import cv2
import os
import numpy as np
import tensorflow as tf

from PIL import Image

from keras.models import Model
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, Input, BatchNormalization, Concatenate, GlobalAveragePooling2D

from tensorflow.keras.applications.resnet50 import ResNet50

man_categories = [
    '견우','서준','수호','시호','준우','태양','태호','혜성'
]
nb_classes = len(man_categories)

st.header("닮은 웹툰 캐릭터 찾기 - 남자")
st.write("사진 입력 방식을 선택해주세요.")

tab1, tab2, tab3 = st.tabs([' ','직접 촬영','사진 업로드'])

with tab1:
    st.write(" ")

with tab2:
    img_file_buffer = st.camera_input("")

with tab3:
    uploaded_file = st.file_uploader("")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    cv2_img = cv2.resize(cv2_img, (256,256))    

    cv2_img_re = tf.convert_to_tensor(cv2_img)

    cv2_img_re = tf.image.resize(cv2_img_re, [256, 256])
    
    hdf5_file = "../MFMBest.hdf5"

    if os.path.exists(hdf5_file):
        resnet = ResNet50(weights='imagenet', include_top=False)
        
        for layer in resnet.layers:
            layer.trainable = False
            
        inputs = Input(shape=(256,256,3))
        res = resnet(inputs)
        gap = GlobalAveragePooling2D()(res)
        dense = Dense(128, activation='relu')(gap)
        outputs = Dense(nb_classes, activation='softmax')(dense)        

        model = Model(inputs=inputs, outputs=outputs)

        model.compile(loss='categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])

        model.load_weights(hdf5_file)
        img_pred = tf.expand_dims(cv2_img_re, axis=0)

        pred = model.predict(img_pred)

        result = man_categories[np.argmax(pred)]

        if result in man_categories:
            image = Image.open("../faces/대표/남자/{}_대표.png".format(result))
            st.image(cv2_img)
            st.image(image, caption=f'{result}')
    

elif img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    cv2_img = tf.convert_to_tensor(cv2_img)

    cv2_img = tf.image.resize(cv2_img, [256, 256])

    hdf5_file = "../MFMBest.hdf5"

    if os.path.exists(hdf5_file):
        resnet = ResNet50(weights='imagenet', include_top=False)
        
        for layer in resnet.layers:
            layer.trainable = False
            
        inputs = Input(shape=(256,256,3))
        res = resnet(inputs)
        gap = GlobalAveragePooling2D()(res)
        dense = Dense(128, activation='relu')(gap)
        outputs = Dense(nb_classes, activation='softmax')(dense)        

        model = Model(inputs=inputs, outputs=outputs)

        model.compile(loss='categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])

        model.load_weights(hdf5_file)
        img_pred = tf.expand_dims(cv2_img, axis=0)

        pred = model.predict(img_pred)

        result = man_categories[np.argmax(pred)]

        if result in man_categories:
            image = Image.open("../faces/대표/남자/{}_대표.png".format(result))
            st.image(image, caption=f'{result}')