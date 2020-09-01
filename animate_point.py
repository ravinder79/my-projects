import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = 4,3
from matplotlib.animation import FuncAnimation

# create a figure with an axes
fig, ax = plt.subplots()
ax.axis([-1.5,1.5,-1.5,1.5])
ax.set_aspect("equal")

# create a point in the axes
point, = ax.plot(0,1, marker="o")

#create text objects
text = ax.text(0, 1.2, "")
text1 = ax.text(0, 1.1, "")
r = 1 # radius of circle

# Updating function, to be repeatedly called by the animation
def update(i):
   
    t = 2.*np.pi*(i/100)
    x = r*np.cos(t)
    y = r*np.sin(t)
    
    # set point's coordinates
    point.set_data(x,y)

    # set text values
    text.set_position((-1, 1.3))
    text.set_text(f"t = {round(t,1)}")
    text1.set_position((0, 1.3))
    text1.set_text(f"Frame = {i}")

    return point,

# create animation with 10ms interval
ani = FuncAnimation(fig, update, interval=10, frames= 600)

#save animation as .mp4
# ani.save('circle.mp4', fps = 15.0, dpi=600)
plt.show()