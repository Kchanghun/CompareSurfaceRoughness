import io
import cv2
import base64 
import glob
import os
import numpy as np
from PIL import Image

datapath = './DataImage/*'

# from image to base64
# img = cv2.imread(filepath)
# jpg_img = cv2.imencode('.jpg',img)
# b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
# print(jpg_img)

# # from base64 to image
# imgdata = base64.b64decode(b64_string)
# dataBytesIO = io.BytesIO(imgdata)
# image = Image.open(dataBytesIO)

# camera image size = (4032,3024)
# print(np.array(image).shape)

# resize image
files = glob.glob(datapath)
for f in files:
    try:
        img = Image.open(f)
        img_resize = img.resize((256,256))
        LAN_img_resize = img.resize((256,256),Image.LANCZOS)
        title,ext = os.path.splitext(f)
        img_resize.save(title+ext)
        LAN_img_resize.save(title+'asdf'+ext)
        print(title)
    except:
        print('eror')
        pass




# show image
# cv2.imshow('이게됨?',cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB))
# cv2.waitKey()
# cv2.destroyAllWindows()