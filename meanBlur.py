from PIL import Image
import numpy 
import sys


imgDir = sys.argv[1]
out = sys.argv[2]
blurRadius = int(sys.argv[3]) 

img = Image.open(imgDir)
newImg = img 
h, w = img.size 
pixel_vals = numpy.array(list(img.getdata())).reshape((w, h, 3)) 
new_vals = newImg.load() 
print(pixel_vals[0][0]) 
progress_amount = 0
progress_width = 30 
sys.stdout.write("[%s]" % ("-" * progress_width))
sys.stdout.flush()
sys.stdout.write("\b" * (progress_width+1)) # return to start of line, after '['

for y in range(h): 
    for x in range(w): 
        adj_pxs = [] 
        r = [] 
        g = [] 
        b = [] 
        
        for i in range(-blurRadius, blurRadius): 
            for j in range(-blurRadius, blurRadius): 
                if (0 <= x+j < w) and (0 <= y+i < h): 
                    adj_pxs.append(pixel_vals[x+j][y+i]) 
                    # print(x+i, y+j) 
                    
        for px in adj_pxs: 
            r.append(px[0]) 
            g.append(px[1]) 
            b.append(px[2]) 
        
        # print(x,y) 
        new_vals[y,x] = (int(numpy.rint(sum(r)/len(r))), int(numpy.rint(sum(g)/len(g))), int(numpy.rint(sum(b)/len(b)))) 
        # print(f"ADJACENTS: \n {adj_pxs}", f"SUMS: \nR: {sum(r)/len(r)} \nG: {sum(g)/len(g)} \nB: {sum(b)/len(b)}")
    
    # update the bar
    if (round(progress_width*(y/h)) >= progress_amount) and progress_amount < 30: 
        sys.stdout.write("#")
        sys.stdout.flush()
        progress_amount += 1 
sys.stdout.write("]\n") # this ends the progress bar

newImg.save(out) 