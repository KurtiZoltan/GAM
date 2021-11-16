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
graniteTime = 1000
#energy (keV), net area, net area rel. error, I, eta, eta rel. error
granite = np.array([
    [351.32, 36043, 0.59e-2, 3.68936e-1, 219.75e-4, 9.045e-2], #214Pb
    [999.07, 620, 14.24e-2, 5.89230e-3 ,  84.57e-4, 7.572e-2], #234Pa
    [186.69, 12230, 1.11e-2, 3.28000e-2, 313.71e-4, 9.099e-2], #226Ra
    [294.96, 23525, 0.88e-2, 1.91873e-1, 204.25e-4, 6.595e-2], #214Pb
    [1765.08, 4430, 1.91e-2, 1.61967e-1, 45.18e-4, 8.758e-2], #214Bi 
    [1118.60, 5706, 2.02e-2, 1.54967e-1, 70.23e-4, 9.289e-2], #214Bi
    [242.14, 10554, 1.74e-2, 7.45288e-2, 260.91e-4, 8.704e-2] #214Pb
    ])

graniteElements = [
    "$^{214}\\text{Pb}$", 
    "$^{234}\\text{Pa}$", 
    "$^{226}\\text{Ra}$", 
    "$^{214}\\text{Pb}$", 
    "$^{214}\\text{Bi}$", 
    "$^{214}\\text{Bi}$", 
    "$^{214}\\text{Pb}$", 
]
    
#soil sample from nuclear explosion
soilTime = 911
#energy (keV), net area, net area rel. error, I, eta, eta rel. error
soil = np.array([
    [658.48 , 407, 5.65e-2, 0.899800, 110.82e-4, 8.559e-2], #134Cs (gamma coming from 134Ba)
    [120.94 , 437, 6.58e-2, 0.284320, 330.51e-4, 7.669e-2], #152Eu
    [343.37 , 172, 9.86e-2, 0.264880, 164.80e-4, 8.173e-2], #152Eu
    [1405.34, 27, 22.83e-2, 0.207470, 45.23e-4, 8.897e-2], #152Eu
    [776.66 , 50, 22.45e-2, 0.127410, 91.76e-4, 8.884e-2], #152Eu
    [244.89 , 65, 14.60e-2, 0.074935, 254.73e-4, 9.466e-2] #152Eu
    ])

soilElements = [
    "$^{134}\\text{Cs}$ ($^{134}\\text{Ba}$)",
    "$^{152}\\text{Eu}$", 
    "$^{152}\\text{Eu}$", 
    "$^{152}\\text{Eu}$", 
    "$^{152}\\text{Eu}$", 
    "$^{152}\\text{Eu}$", 
    ]

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

def intensity(x, t):
    I = x[:,1] / (x[:,3] * x[:,4] * t)
    dI = I * np.sqrt(x[:,2]**2 + x[:,5]**2)
    return np.array([I, dI]).transpose()

def printTable(table, isotopes):
    for row, isotope in zip(table, isotopes):
        print(f"            ${row[0]:.1f}$ & ${int(row[1]):d}$ & ${row[2]*100:.1f}\\%$ & {row[3]:.3e} & ${row[4]*100:.4f}\\%$ & ${row[5]*100:.1f}\\%$ & {isotope} \\\\")

print("Granite data:")
printTable(granite, graniteElements)
print("Soil data:")
printTable(soil, soilElements)

def printPeakActivity(data, t, dataElements):
    A = intensity(data, t)
    for row, isotope, a in zip(data, dataElements, A):
        print(f"            ${row[0]:.1f}$ & ${a[0]/1000:.1f}$ & ${a[1]/1000:.1f}$ & {isotope} \\\\")

print("Granite peaks:")
printPeakActivity(granite, graniteTime, graniteElements)

def printPeakActivity(data, t, dataElements):
    A = intensity(data, t)
    for row, isotope, a in zip(data, dataElements, A):
        print(f"            ${row[0]:.1f}$ & ${a[0]:.1f}$ & ${a[1]:.1f}$ & {isotope} \\\\")

print("Soil peaks:")
printPeakActivity(soil, soilTime, soilElements)

granitePeaks = intensity(granite, graniteTime)
pbPeaks = np.array([granitePeaks[0], granitePeaks[3], granitePeaks[6]])
biPeaks = np.array([granitePeaks[4], granitePeaks[5]])
beforeRnPeaks = np.array([granitePeaks[1], granitePeaks[2]])
afterRnPeaks = np.array([granitePeaks[0], granitePeaks[3], granitePeaks[4], granitePeaks[5], granitePeaks[6]])

def average(data):
    avg = np.sum(data[:, 0] / data[:, 1]**2) / np.sum(1 / data[:, 1]**2)
    sigma = 1 / np.sqrt(np.sum(1 / data[:, 1]**2))
    return avg, sigma

pb, dpb = average(pbPeaks)
print("Pb: ", pb, "+/-", dpb)
bi, dbi = average(biPeaks)
print("Bi: ", bi, "+/-", dbi)
beforeRn, dbeforeRn = average(beforeRnPeaks)
print("Before Rn: ", beforeRn, "+/-", dbeforeRn)
afterRn, dafterRn = average(afterRnPeaks)
print("After Rn-: ", afterRn, "+/-", dafterRn)

print("Table of averages:")
print(f"            $^{{214}}\\text{{Pb}}$ & {pb:.0f} & {dpb:.0f} \\\\")
print(f"            $^{{214}}\\text{{Bi}}$ & {bi:.0f} & {dbi:.0f} \\\\")
print(f"            Before $^{{222}}\\text{{Rn}}$ & {beforeRn:.0f} & {dbeforeRn:.0f} \\\\")
print(f"            After $^{{222}}\\text{{Rn}}$ & {afterRn:.0f} & {dafterRn:.0f} \\\\")

plt.errorbar(np.arange(0, pbPeaks.shape[0]), pbPeaks[:, 0], yerr=pbPeaks[:, 1], fmt="o", label="Lead peaks activity")
plt.errorbar(pbPeaks.shape[0], pb, yerr=dpb, fmt="o", label="Averaged lead activity")
plt.errorbar(np.arange(0, biPeaks.shape[0]) + pbPeaks.shape[0] + 1, biPeaks[:, 0], yerr=biPeaks[:, 1], fmt="o", label="Bizmuth peaks activity")
plt.errorbar(biPeaks.shape[0] + pbPeaks.shape[0] + 1, bi, yerr=dbi, fmt="o", label="Averaged bismuth activity")
plt.errorbar(biPeaks.shape[0] + pbPeaks.shape[0] + 2, afterRn, yerr=dafterRn, fmt="o", label="Averaged activity after radon")
plt.errorbar(biPeaks.shape[0] + pbPeaks.shape[0] + 3, granitePeaks[1, 0], yerr=granitePeaks[1, 1], fmt="o", label="Protactinium activity")
plt.errorbar(biPeaks.shape[0] + pbPeaks.shape[0] + 4, granitePeaks[2, 0], yerr=granitePeaks[2, 1], fmt="o", label="Radium activity")
plt.errorbar(biPeaks.shape[0] + pbPeaks.shape[0] + 5, beforeRn, yerr=dbeforeRn, fmt="o", label="Averaged activity before radon")
plt.legend()
plt.grid()
plt.ylabel("A [$Bq$]")
plt.savefig("./figs/graniteactivities.pdf")
plt.show()

escapeRatio = (beforeRn - afterRn) / beforeRn
descapeRatio = afterRn / beforeRn * np.sqrt((dbeforeRn / beforeRn)**2 + (dafterRn / afterRn)**2)
print("Radon escape ratio: ", escapeRatio, "+/-", descapeRatio)

T12 = 1.41e17
decayRate = np.log(2) / T12
N = beforeRn / decayRate
dN = dbeforeRn / decayRate
print(f"# U238: {N:.2e}+/-{dN:.1e}")
mol = 6.02214076e23
amass = 238.051
mass = N / mol * amass
dmass = dN / mol * amass
print(f"U238 mass: {mass:.3f}+/-{dmass:.3f}")

lambda238 = decayRate
lambda235 = np.log(2) / (7.04e8 * 365 * 24 * 3600)

print("235 contribution to 186keV peak:", 0.007 * lambda235 / (0.007 * lambda235 + 0.993 * lambda238))
print("186keV peak rel. error:", granitePeaks[2, 1] / granitePeaks[2, 0])