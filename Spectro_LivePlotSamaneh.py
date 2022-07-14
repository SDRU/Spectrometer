# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:52:01 2021

@author: Sandra_modified by Samaneh
"""

import seabreeze
# seabreeze.use('pyseabreeze')
from seabreeze.spectrometers import Spectrometer, list_devices
import matplotlib.pyplot as plt
# import time
import numpy as np
import datetime
# from seabreeze.spectrometers import Spectrometer
# spec = Spectrometer.from_first_available()
# matplotlib qt


def init_spectrometer():
    spec = None
    # OPEN THE SPECTROMETER
    devices = list_devices()
    spec = Spectrometer(devices[0])
    # spec=Spectrometer.from_serial_number('HDX01068')

    spec.integration_time_micros(int(6000))
    # External trigger on demand
    spec.trigger_mode(0)
    if 'spec' in locals():
        return spec
    else:
        print('The spectrometer was not initialized correctly')
        return None

def main_spectrometer(spec):

    f=plt.figure()
    ax = f.add_subplot(111)
    
    
    global w, i
    w = spec.wavelengths()
    i = spec.intensities()
    line1, = ax.plot(w, i)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity (pixels)')
    plt.xlim(left=200, right=1100)
    plt.ylim(bottom=1300, top=2100)
    plt.show()

    # plt.xlabel('Wavelength (nm)')
    # plt.ylabel('Intensity (pixels)')
    # plt.xlim(left=800, right=900)
    # plt.ylim(bottom=0, top=16000)
    while True:            
        i = spec.intensities()

        # updating data values
        line1.set_xdata(w)
        line1.set_ydata(i)
        plt.draw()
        plt.show()
        plt.pause(0.1)

        
def close_spectrometer(spec):
    spec.close()
    

spec = init_spectrometer()
print(spec)
# main_spectrometer(spec)
# close_spectrometer(spec)
try:        
    if spec is not None:
        main_spectrometer(spec)
        close_spectrometer(spec)

except KeyboardInterrupt:
    spec.close()
    print('How dare you cancelling me!')
    
except:
    spec.close()
    print('I closed the connection for some reason')


