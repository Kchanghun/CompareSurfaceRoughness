import io
import cv2
import base64 
import glob
import os
import numpy as np
from PIL import Image
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
# datapath = './DataImage/*'

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
# files = glob.glob(datapath)
# for f in files:
#     try:
#         img = Image.open(f)
#         img_resize = img.resize((256,256))
#         LAN_img_resize = img.resize((256,256),Image.LANCZOS)
#         title,ext = os.path.splitext(f)
#         img_resize.save(title+ext)
#         LAN_img_resize.save(title+'asdf'+ext)
#         print(title)
#     except:
#         print('eror')
#         pass

def sine_generator(fs, sinefreq, duration):
    print(fps,sine_fq,duration)
    T = duration
    n = fs * T
    w = 2. * np.pi * sinefreq
    t_sine = np.linspace(0, T, n, endpoint = False)
    y_sine = np.sin(w * t_sine)
    result = pd.DataFrame({"data" : y_sine} ,index = t_sine)
    return result

def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype = "high", analog = False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

fps = 30
sine_fq = 10
duration = 10
sine_5Hz = sine_generator(fps,sine_fq,duration)
sine_fq = 1
duration = 10
sine_1Hz = sine_generator(fps,sine_fq,duration)
sine = sine_5Hz + sine_1Hz
filtered_sine = butter_highpass_filter(sine.data, 10, fps)
plt.figure(figsize = (20, 10))

print(sine.values.shape)
plt.plot(range(len(sine.values)), sine.values,'-',color='black')
plt.title("Generated Signal")

print(filtered_sine)
plt.plot(range(len(filtered_sine)), filtered_sine)
plt.title("Filtered Signal")
plt.show()


# show image
# cv2.imshow('이게됨?',cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB))
# cv2.waitKey()
# cv2.destroyAllWindows()