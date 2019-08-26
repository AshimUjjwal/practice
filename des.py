

import numpy as np
from matplotlib import pyplot as plt

x=np.arange(1,15)
y=2*x+5
plt.title('Demo')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,'ob')
plt.show()