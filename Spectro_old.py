# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:52:01 2021

@author: Sandora
"""

import seabreeze
seabreeze.use('cseabreeze')
from seabreeze.spectrometers import Spectrometer, list_devices
import matplotlib.pyplot as plt
import time
import numpy as np

print(list_devices())
devices=list_devices()
spec=Spectrometer(devices[0])


# api=seabreeze.pyseabreeze.SeaBreezeAPI()
# print(api.supported_models())
# devices=api.list_devices()
# s=devices[0]
# s.open()
# print(s.get_serial_number())



# spec=Spectrometer.from_serial_number('HDX01068')

# spec.integration_time_micros(6000)
# spec.trigger_mode(0)
start_time = time.time()
for i in range(5):
    start_time = time.time()
    w=spec.wavelengths()
    i=spec.intensities()
    s=np.sum(i[392:593])
    print(s)
    if s>300000:
        print('Habemos luz')

    elapsed = time.time()
    # print((elapsed - start_time)*1000)
plt.plot(w,i)


