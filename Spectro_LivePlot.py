# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:52:01 2021

@author: Sandora
"""

import seabreeze
seabreeze.use('pyseabreeze')
from seabreeze.spectrometers import Spectrometer, list_devices
import matplotlib.pyplot as plt
# import time
import numpy as np
import datetime



def init_spectrometer():
    spec = None
    # OPEN THE SPECTROMETER
    devices=list_devices()
    spec=Spectrometer(devices[0])
    # spec=Spectrometer.from_serial_number('HDX01068')
    
    spec.integration_time_micros(int(200e3))
    # External trigger rising edge
    spec.trigger_mode(1)
    if 'spec' in locals():
        return spec
    else:
        print('The spectrometer was not initialized correctly')
        return None
    
def main_spectrometer(spec):
    plt.plot(1,1)
    # to run GUI event loop
    plt.ion()
    # here we are creating sub plots
    figure, ax = plt.subplots(figsize=(10, 8))
    line1, = ax.plot(1, 1)
    
    
    global w, i
    w=spec.wavelengths()
    while True:            
        i=spec.intensities()
        plt.plot(w,i)
        
# updating data values
        line1.set_xdata(w)
        line1.set_ydata(i)
      
        # drawing updated values
        figure.canvas.draw()
      
        # This will run the GUI event
        # loop until all UI events
        # currently waiting have been processed
        figure.canvas.flush_events()
        
    plt.ioff()
    plt.show()
        
def close_spectrometer(spec):
    spec.close()
    





spec = init_spectrometer()

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


