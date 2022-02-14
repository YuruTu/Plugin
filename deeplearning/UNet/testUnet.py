'''
Descripttion: 
version: 
Author: yurutu
Date: 2021-12-22 14:54:45
LastEditors: yurutu
LastEditTime: 2021-12-22 20:43:26
'''
from  tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np



if __name__ == '__main__':
    
    model = keras.models.load_model('./UNetModel.h5')
    f_names =[]
    f_names.append("test2.png")
    f_names.append("test.png")
    f_names.append("testColor.png")
    img = [] 
    for i in range(len(f_names)):
        images = image.load_img(f_names[i], target_size=(256, 256,3))
        x = image.img_to_array(images)
        x = np.expand_dims(x, axis=0)
        img.append(x)
    print('loading no.%s image' % i)
    print("len(img)",len(img))
    print(img[0].shape)   
    # 把图片数组联合在一起
    x = np.concatenate([x for x in img])
    result = model.predict(x)
    count = 0
    for img in result:
        print(img)
        x = np.empty([256,256,1], dtype = np.float32)
        y = np.empty([256,256,1], dtype = np.float32) 
        for i in range(256):
            for j in range(256):
                x[i][j][0] = img[i][j][0]+img[i][j][1]
                y[i][j][0] = img[i][j][1]
        image.save_img('result'+str(count)+'.jpg', x)
        image.save_img('result'+str(count)+'Y.jpg', x)
        count=count+1
