import struct
import matplotlib.pyplot as plt

#fileName =   #完整路径
f = open("ergcurve.dat","rb")
rawData = f.read()
f.close()

iSampleCount = len(rawData) // 4
curveData = []
for i in range(iSampleCount):
    fValue, = struct.unpack("<f",rawData[i*4:i*4+4])
    curveData.append(fValue)

print(curveData)
plt.plot(curveData)
plt.show()