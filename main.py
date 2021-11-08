import numpy as np
import matplotlib.pyplot as plt

#calibration
#energy (keV), net area, net area rel. error
calibration = np.array([
    [238.52, 114086, 0.36e-2],
    [2613.25, 7075, 1.98e-2],
    [579.92, 25962, 0.83e-2],
    [906.96, 16829, 1.03e-2]
    ]).transpose()

#granite
#energy (keV), net area, net area rel. error
granite = np.array([
    [351.32, 36043, 0.48e-2],
    [999.07, 620, 2.09e-2],
    [186.69, 12230, 0.64e-2],
    [294.96, 23525, 0.56e-2],
    [1765.08, 4430, 1.44e-2],
    [1118.60, 5706, 1.17e-2],
    [242.14, 10554, 0.66e-2]
    ]).transpose()
    
#soil from nuclear explosion
#energy (keV), net area, net area rel. error
soil = np.array([
    [658.48, 407, 5.65e-2],
    [120.94, 437, 6.58e-2],
    [343.37, 172, 9.86e-2],
    [1405.34, 27, 22.83e-2],
    [776.66, 50, 22.45e-2],
    [244.89, 65, 14.60e-2]
    ]).transpose()

#intensity
#energy (MeV), eta, eta rel. error

eta = np.array([
    [0.122, 330.51e-4, 7.669e-2],
    [0.144, 405.09e-4, 9.160e-2],
    [0.186, 313.71e-4, 9.099e-2],
    [0.238, 269.13e-4, 9.275e-2],
    [0.242, 260.91e-4, 8.704e-2],
    [0.245, 254.73e-4, 9.466e-2],
    [0.295, 204.25e-4, 6.595e-2],
    [0.344, 164.80e-4, 8.173e-2],
    [0.351, 219.75e-4, 9.045e-2],
    [0.580, 128.66e-4, 9.067e-2],
    [0.609, 114.42e-4, 9.450e-2],
    [0.661, 110.82e-4, 8.559e-2],
    [0.778, 91.76e-4, 8.884e-2],
    [1.001, 84.57e-4, 7.572e-2],
    [1.118, 70.23e-4, 9.289e-2],
    [1.409, 45.23e-4, 8.897e-2],
    [1.765, 45.18e-4, 8.758e-2],
]).transpose()

plt.plot(eta[0], eta[1])
plt.show()
