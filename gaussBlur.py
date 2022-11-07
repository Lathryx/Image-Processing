from PIL import Image
import numpy as np 
import sys

if len(sys.argv) < 3: 
    print("Usage: python gaussBlur.py <path to image> <name of output file> <blur radius>") 
    sys.exit() 

imgDir = sys.argv[1]
out = sys.argv[2]
blurRadius = int(sys.argv[3]) 

img = Image.open(imgDir)
newImg = img 
h, w = img.size 
pixel_vals = np.array(list(img.getdata())).reshape((w, h, 3)) 
new_vals = newImg.load() 

progress_amount = 0
progress_width = 30 
sys.stdout.write("[%s]" % ("-" * progress_width))
sys.stdout.flush()
sys.stdout.write("\b" * (progress_width+1)) # return to start of line, after '['


def gauss2d(x, y, amplitude, centerX, centerY, sigX, sigY): 
    val = amplitude * np.exp(-((((x - centerX)**2)/(2*(sigX**2)))+(((y - centerY)**2)/(2*(sigY**2))))) 
    return val 
    
for y in range(h): 
    for x in range(w): 
        adj_pxs_vals = [] 
        adj_pxs_coords = []
        r = [] 
        g = [] 
        b = [] 
        
        for i in range(-blurRadius, blurRadius): # get adjacent pixels for current pixel 
            for j in range(-blurRadius, blurRadius): 
                if (0 <= x+i < w) and (0 <= y+j < h): 
                    adj_pxs_vals.append(pixel_vals[x+i][y+j]) 
                    adj_pxs_coords.append([x+i, y+j]) 
                    # print(x+i, y+j) 
                    
        # print(pixel_vals) 
        for px in adj_pxs_vals: # arrange RGB values for each pixel into separate arrays 
            r.append(px[0]) 
            g.append(px[1]) 
            b.append(px[2]) 
        
        weights = [gauss2d(coord[0], coord[1], 1, x, y, blurRadius, blurRadius) for coord in adj_pxs_coords] 
        new_vals[y,x] = (int(np.rint(np.average(r, weights=weights))), int(np.rint(np.average(g, weights=weights))), int(np.rint(np.average(b, weights=weights)))) 
        # print(f"ADJACENTS: \n {adj_pxs}", f"SUMS: \nR: {sum(r)/len(r)} \nG: {sum(g)/len(g)} \nB: {sum(b)/len(b)}")
    
    # update the bar 
    if (round(progress_width*(y/h)) >= progress_amount) and progress_amount < 30: 
        sys.stdout.write("#")
        sys.stdout.flush()
        progress_amount += 1 
sys.stdout.write("]\n") # this ends the progress bar 

newImg.save(out) 