"""
*****************************************************************************
Copyright 2023 Silicon Laboratories Inc. www.silabs.com
*****************************************************************************
SPDX-License-Identifier: Zlib

The licensor of this software is Silicon Laboratories Inc.

This software is provided \'as-is\', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not
   claim that you wrote the original software. If you use this software
   in a product, an acknowledgment in the product documentation would be
   appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be
   misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.

*****************************************************************************
# EXPERIMENTAL QUALITY
This code has not been formally tested and is provided as-is. It is not
suitable for production environments. In addition, this code will not be
maintained and there may be no bug maintenance planned for these resources.
Silicon Labs may update projects from time to time.
******************************************************************************
"""

import board
from SleepTimer import SleepTimer
from adafruit_as726x import AS726x_I2C
from adafruit_ble import BLERadio
from SensorApp import SensorApp
from LightSensingService import LightSensingService

# Configuration parameters
DEVICE_NAME = 'CP_LIGHT_SENSOR'

## Initialize application
i2c = board.I2C()
sensors = AS726x_I2C(i2c)

application = SensorApp(sensors,
                        LightSensingService(),
                        BLERadio())

application.configure_advertisement(DEVICE_NAME,
                                    connectable = True)

SleepTimer.setup_timer(application.main_function, 2)

while True:
    SleepTimer.main_function()

