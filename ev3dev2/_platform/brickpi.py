# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
# Copyright (c) 2015 Eric Pascual
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# -----------------------------------------------------------------------------

"""
An assortment of classes modeling specific features of the BrickPi.
"""

from collections import OrderedDict

OUTPUT_A = 'ttyAMA0:MA'
OUTPUT_B = 'ttyAMA0:MB'
OUTPUT_C = 'ttyAMA0:MC'
OUTPUT_D = 'ttyAMA0:MD'

INPUT_1 = 'ttyAMA0:S1'
INPUT_2 = 'ttyAMA0:S2'
INPUT_3 = 'ttyAMA0:S3'
INPUT_4 = 'ttyAMA0:S4'

BUTTONS_FILENAME = None
EVDEV_DEVICE_NAME = None

LEDS = OrderedDict()
LEDS['blue_led1'] = 'brickpi:led1:blue:ev3dev'
LEDS['blue_led2'] = 'brickpi:led2:blue:ev3dev'

LED_GROUPS = OrderedDict()
LED_GROUPS['LED1'] = ('blue_led1',)
LED_GROUPS['LED2'] = ('blue_led2',)

LED_COLORS = OrderedDict()
LED_COLORS['BLACK'] = (0,)
LED_COLORS['BLUE'] = (1,)
