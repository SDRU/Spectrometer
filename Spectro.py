# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:52:01 2021

@author: Sandora
"""

import seabreeze
seabreeze.use('pyseabreeze')
from seabreeze.spectrometers import Spectrometer, list_devices
import numpy as np
import datetime
from usb.core import USBTimeoutError

# print(list_devices())
# devices=list_devices()
# spec=Spectrometer(devices[0])

# api=seabreeze.pyseabreeze.SeaBreezeAPI()
# print(api.supported_models())
# devices=api.list_devices()
# s=devices[0]
# s.open()
# print(s.get_serial_number())



def init_spectrometer():
    spec = None
    
    # OPEN THE SPECTROMETER
    devices=list_devices()
    spec=Spectrometer(devices[0])
    # spec=Spectrometer.from_serial_number('HDX01068')
    
    spec.integration_time_micros(int(200e3))
    
    # External trigger: software 0, rising edge 1
    spec.trigger_mode(1)
    
    spec.f.spectrometer.set_acq_delay(2000)
    
    if 'spec' in locals():
        return spec
    else:
        print('The spectrometer was not initialized correctly')
        return None
    
def main_spectrometer(spec):
    
    global w, i
    w=spec.wavelengths()
    while True:    
        
        i=spec.intensities()
        print(datetime.datetime.now())
        s=np.sum(i[392:593])
        print(s)

        
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
    
except:
    spec.close()
    print('I closed the connection for some reason')


