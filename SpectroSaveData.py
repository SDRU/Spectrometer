# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:45:33 2022

@author: Sandra Drusova

Save data from Ocean Optix HDX spectrometer with a custom format
"""

import seabreeze
seabreeze.use('pyseabreeze')
from seabreeze.spectrometers import Spectrometer, list_devices
import numpy as np
import datetime
from usb.core import USBTimeoutError
import time


# number of laser pulses
nr_pulses = 50
save_file = 1
folder = 'C:/Users/Hamed/Desktop/Sandra/'
# Add tissue type in the filename if needed 
filename_base = time.strftime("%Y%m%d-%H%M%S") + '-Meat' 


def init_spectrometer():
    spec = None
    
    # OPEN THE SPECTROMETER
    devices=list_devices()
    spec=Spectrometer(devices[0])
    # spec=Spectrometer.from_serial_number('HDX01068')
    
    spec.integration_time_micros(int(6e3))
    
    # External trigger: software 0, rising edge 1
    spec.trigger_mode(1)

    # Set acquisition delay in microseconds. Doesn't work.
    # spec.f.spectrometer.set_acq_delay(1)
    # print(spec.f.spectrometer.get_acq_delay())
    
    if 'spec' in locals():
        return spec
    else:
        print('The spectrometer was not initialized correctly')
        return None
    
def main_spectrometer(spec):
    
    global w, i, Spectra
    w=spec.wavelengths()
    
    Spectra = np.zeros([w.shape[0],nr_pulses+1])
    Spectra[:,0] = w
    
    for i in range(nr_pulses):  
        
        Spectra[:,i+1] = spec.intensities()
        print(datetime.datetime.now())
        
        
    if save_file == 1:
        filename = folder + filename_base + '.txt'
        with open(filename,'a') as f:
            np.savetxt(f,Spectra, delimiter='\t',fmt='%6.2f')
            print('saved')
            
            
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
    
except USBTimeoutError:
    print('Timeout')
    
except Exception as e:
    spec.close()
    print('I closed the connection for some reason')
    print(str(e))


