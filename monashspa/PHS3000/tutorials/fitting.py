# Copyright 2019 School of Physics & Astronomy, Monash University
#
# This file is part of monashspa.
#
# monashspa is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# monashspa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with monashspa.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np

from ...PHS2061.fitting_tutorial import data as part_b_data

__raw_c1_data = np.array([
    2.3210,
    3.2540,
    2.8190,
    1.7080,
    1.5000,
    1.9310,
    2.5550,
    2.4900,
    3.4440,
    4.3850,
    2.1090,
    2.4150,
    3.9860,
    2.4270,
    2.6140,
    3.9260,
    3.6750,
    1.9290,
    3.0790,
    1.5350,
    1.7230,
    2.8590,
    2.7770,
    2.2610,
    3.2300,
    2.3950,
    3.6690,
    1.5050,
    3.4200,
    1.7920,
    3.0490,
    2.9440,
    4.6050,
    1.9620,
    2.3350,
    3.0540,
    2.9890,
    1.5280,
    2.6240,
    4.1070,
    1.0210,
    3.2830,
    2.3570,
    1.6570,
    1.9720,
    2.9710,
    2.3450,
    2.9370,
    1.5700,
    3.2290,
    3.1370,
    2.2270,
    1.6970,
    3.5110,
    3.0590,
    2.0740,
    1.8730,
    2.9080,
    2.8470,
    1.7010,
    2.7510,
    3.7900,
    2.5210,
    3.2980,
    3.7300,
    2.7190,
    2.3580,
    2.9980,
    2.2230,
    2.6950,
    2.3160,
    2.9220,
    2.3300,
    4.7440,
    1.6960,
    2.6530,
    3.1330,
    2.3250,
    3.4680,
    3.8280,
    2.8100,
    3.0550,
    3.7650,
    4.5610,
    4.2640,
    6.4830,
    4.9900,
    6.2290,
    5.8900,
    7.8910,
   10.5630,
   11.5250,
   13.7320,
   16.6170,
   19.5790,
   19.6190,
   19.6830,
   18.3080,
   16.8990,
   15.4810,
   13.2950,
   11.0590,
    9.1750,
    9.6960,
    6.0640,
    6.6160,
    6.1250,
    3.5670,
    3.3140,
    3.4540,
    3.1770,
    4.5830,
    2.5490,
    2.8940,
    3.1350,
    4.6270,
    2.7840,
    2.8260,
    2.5680,
    3.2630,
    2.6800,
    2.2510,
    2.2510,
    3.1350,
    1.9210,
    1.1020,
    3.0240,
    2.1440,
    2.3620,
    1.4600,
    3.2830,
    1.4970,
    1.8430,
    4.8610,
    2.4190,
    1.1790,
    1.3360,
    1.9030,
    2.0920,
    1.7590,
    2.3070,
    1.5590,
    2.3870,
    2.3960,
    4.1840,
    3.0650,
    2.3720,
    2.9650,
    2.4610,
    3.0940,
    2.9960,
    4.5100,
    3.5310,
    3.6650,
    4.8230,
    4.2260,
    6.8550,
    7.3950,
    7.9090,
    9.3960,
   10.5430,
   11.7120,
   15.2650,
   15.7370,
   18.6460,
   17.4950,
   15.9550,
   14.6230,
   12.0540,
    8.8200,
    8.4490,
    5.6530,
    6.7680,
    5.4740,
    4.6360,
    4.3780,
    2.7450,
    3.9500,
    3.3450,
    2.3530,
    2.7540,
    3.5760,
    3.2350,
    2.8320,
    1.6710,
    2.5010,
    2.0600,
    2.4690,
    1.5990,
    3.0130,
    0.6470,
    2.0270,
    2.5120,
    2.0790,
    2.6500,
    2.2200,
    2.7150,
    1.6960,
    1.7790,
    1.3410,
    2.6360,
    3.1050,
    1.6440,
    2.3820,
    4.2680,
    1.8370,
    2.5510,
    0.7880,
    2.9420,
    0.7160,
    2.0600,
    1.8260,
    2.0880,
    3.0550,
    4.1650,
    1.0730,
    2.4130,
    3.0190,
    1.7070,
    3.0370,
    2.3430,
    2.2560,
])

part_c1_data = np.zeros((__raw_c1_data.shape[0],2))
part_c1_data[:,0] = np.arange(0, __raw_c1_data.shape[0])
part_c1_data[:,1] = __raw_c1_data
