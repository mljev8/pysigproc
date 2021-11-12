import numpy as np
import matplotlib.pyplot as plt
import filtering

n = 200
w = 2.*np.random.standard_normal(size=n)
x = 10.*np.cos(2*np.pi*0.01*np.arange(n))*np.sin(4*np.pi*0.033*np.arange(n))
signal = x + w

AR = filtering.AR_filter([3/10,2/10,1/10])
AR.init(x[0])
y = np.zeros(n)
for i in range(n):
    y[i] = AR.filter(signal[i])

fig,ax = plt.subplots()
ax.plot(signal)
ax.plot(y,label='AR')
ax.legend(loc=0)

plt.show()
