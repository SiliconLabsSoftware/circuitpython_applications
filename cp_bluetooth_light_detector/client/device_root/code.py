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
import busio
from adafruit_ble import BLERadio
from ClientApp import ClientApp
from NeoPixelDisplay import Display

# A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
BRIGHTNESS_DEFAULT = 0.1

SPI = busio.SPI(clock = board.SCK, MOSI=board.PD0, MISO = board.MISO)

# Initialize application
application = ClientApp(
    display=Display(spi=SPI, brightness=BRIGHTNESS_DEFAULT),
    ble=BLERadio()
)

while True:
    application.main_function()
