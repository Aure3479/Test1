import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)

plt.plot(x,y)
plt.xlabel('x values from 0 to 4pi')  # string must be enclosed with quotes '  '
plt.ylabel('sin(x)')
plt.title('Plot of sin from 0 to 4pi')
plt.legend(['sin(x)']) 
plt.savefig('sin_picture.png')




