import numpy as np

import matplotlib.pyplot as plot

# Get x values of the sine wave

time= np.arange(0,5*2*3.14,0.001);

# Amplitude of the sine wave is sine of a variable like time
amplitude1= np.cos(time)
amplitude2 = np.sin(time)

# Plot a sine wave using time and amplitude obtained for the sine wave

plot.plot(time, amplitude2)
plot.plot(time, amplitude1)
# Give a title for the sine wave plot

plot.title('Sine wave')

# Give x axis label for the sine wave plot

plot.xlabel('Time')

# Give y axis label for the sine wave plot

plot.ylabel('Amplitude = sin(time)')

plot.grid(True, which='both')

plot.axhline(y=0, color='k')

plot.show()

# Display the sine wave

plot.show()