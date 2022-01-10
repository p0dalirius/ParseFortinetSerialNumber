#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : batch_test.py
# Author             : Podalirius (@podalirius_)
# Date created       : 10 Jan 2022

import os

serial_numbers = ['FG080D0000000000', 'FG100A0000000000', 'FG100C0000000000', 'FG100D0000000000', 'FG100E0000000000', 'FG101E0000000000', 'FG10CH0000000000', 'FG140D0000000000', 'FG1K2D0000000000', 'FG1K5D0000000000', 'FG1KBD0000000000', 'FG200A0000000000', 'FG200B0000000000', 'FG200D0000000000', 'FG200E0000000000', 'FG201E0000000000', 'FG20CA0000000000', 'FG224B0000000000', 'FG240D0000000000', 'FG300A0000000000', 'FG300B0000000000', 'FG300C0000000000', 'FG30DP0000000000', 'FG311B0000000000', 'FG36000000000000', 'FG3H0E0000000000', 'FG3H1E0000000000', 'FG3K0B0000000000', 'FG3K1B0000000000', 'FG3K6C0000000000', 'FG3K8A0000000000', 'FG3K910000000000', 'FG3K9B0000000000', 'FG400A0000000000', 'FG5A250000000000', 'FG5H0E0000000000', 'FG5H1E0000000000', 'FG600B0000000000', 'FG600C0000000000', 'FG60DP0000000000', 'FG621B0000000000', 'FG800C0000000000', 'FG800D0000000000', 'FG80CM0000000000', 'FG90DP0000000000', 'FGT1000000000000', 'FGT1KA0000000000', 'FGT1KB0000000000', 'FGT1KC0000000000', 'FGT1KD0000000000', 'FGT1KX0000000000', 'FGT2000000000000', 'FGT20C0000000000', 'FGT30B0000000000', 'FGT30D0000000000', 'FGT30E0000000000', 'FGT3HD0000000000', 'FGT40C0000000000', 'FGT4HD0000000000', 'FGT50A0000000000', 'FGT50B0000000000', 'FGT50E0000000000', 'FGT51E0000000000', 'FGT5HD0000000000', 'FGT60B0000000000', 'FGT60C0000000000', 'FGT60D0000000000', 'FGT60E0000000000', 'FGT61E0000000000', 'FGT6HD0000000000', 'FGT70D0000000000', 'FGT8000000000000', 'FGT80C0000000000', 'FGT80E0000000000', 'FGT81E0000000000', 'FGT90D0000000000', 'FGT90E0000000000', 'FGT92D0000000000', 'FGVM000000000000', 'FGVM020000000000', 'FGVM2V0000000000', 'FW60CM0000000000', 'FW60DC0000000000', 'FW80CM0000000000', 'FWF20C0000000000', 'FWF30B0000000000', 'FWF30D0000000000', 'FWF30E0000000000', 'FWF40C0000000000', 'FWF50B0000000000', 'FWF50E0000000000', 'FWF60A0000000000', 'FWF60B0000000000', 'FWF60C0000000000', 'FWF60D0000000000', 'FWF60E0000000000', 'FWF61E0000000000', 'FWF90D0000000000']

c = 0
for fsn in serial_numbers:
    data = os.popen('./ParseFortinetSerialNumber.py %s' % fsn).read()
    if "Unknown model" in data:
        c += 1
        print("unk: %s" %fsn)
    else:
        pass


print("[>] Parsed  :", len(serial_numbers) - c)
print("[>] Missing :", c)