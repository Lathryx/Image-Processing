# from mpl_toolkits import mplot3d 
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider 

fig = plt.figure() 
ax = plt.axes(projection='3d') 


def gauss2d(x, y, amplitude, centerX, centerY, sigX, sigY): 
    val = amplitude * np.exp(-((((x - centerX)**2)/(2*(sigX**2)))+(((y - centerY)**2)/(2*(sigY**2))))) # assuming (0, 0) is center 
    return val 

x, y = np.linspace(-6, 6, 60), np.linspace(-6, 6, 60) 
X, Y = np.meshgrid(x, y) 
Z = gauss2d(X, Y, 1, 0, 0, 2.5, 2.5) 

print(len(X), len(Y), len(Z)) 

ax.plot_surface(np.array(X), np.array(Y), np.array(Z), rstride=1, cstride=1, cmap='viridis', edgecolor='none') 
ax.scatter(0, 0, 5, c='r', marker='o', alpha=0) # fixed height Z axis 

axamp = plt.axes([0.1, 0.25, 0.0225, 0.63], facecolor='lightgoldenrodyellow') 
amp_slider = Slider(
    ax=axamp, 
    label="Amplitude", 
    valmin=0, 
    valmax=5, 
    valinit=1, 
    valstep=0.2, 
    orientation="vertical" 
)

axcenterx = plt.axes([0.25, 0.065, 0.65, 0.03], facecolor='lightgoldenrodyellow') 
centerx_slider = Slider(
    ax=axcenterx, 
    label="Center X", 
    valmin=-6, 
    valmax=6, 
    valinit=0, 
    valstep=0.2, 
    orientation="horizontal" 
)

axcentery = plt.axes([0.25, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow') 
centery_slider = Slider(
    ax=axcentery, 
    label="Center Y", 
    valmin=-6, 
    valmax=6, 
    valinit=0, 
    valstep=0.2, 
    orientation="horizontal" 
)

def update(val): 
    ax.clear() 
    Z = gauss2d(X, Y, amp_slider.val, centerx_slider.val, centery_slider.val, 2.5, 2.5)
    ax.plot_surface(np.array(X), np.array(Y), np.array(Z), rstride=1, cstride=1, cmap='viridis', edgecolor='none') 
    ax.scatter(0, 0, 5, c='r', marker='o', alpha=0) # fixed height Z axis 


amp_slider.on_changed(update) 
centerx_slider.on_changed(update) 
centery_slider.on_changed(update) 

# ax.scatter3D(X, Y, Z, c=Z, cmap='Greens') 
ax.set_title('2D Gaussian Distribution') 
plt.show() 