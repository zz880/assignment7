import numpy as np
import matplotlib.pyplot as plt

def question4():
    N_max = 50
    some_threshold = 50
    x = np.linspace(-2, 1, 500)
    y = np.linspace(-1.5, 1.5, 500)
    vx,vy = np.meshgrid(x,y)    
    c = vx + 1j*vy         
    z = c
    
    for v in range(N_max):
        with np.errstate(all ='ignore'):
            z = z**2 + c
            
    with np.errstate(all ='ignore'):
    	mask = (abs(z) < some_threshold)   
    plt.imshow(mask.T,extent=[-2,1,-1.5,1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')

