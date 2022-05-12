from matplotlib import pyplot as mp
import numpy as np

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.))) # f(x) = (-(x-mean)^2/(2*stdev^2))

x_values = np.linspace(-3, 3, 120)
for mu, sig in [(-1, 1), (0, 2), (2, 3)]:
    print(gaussian(x_values, mu, sig))
#     mp.plot(x_values, gaussian(x_values, mu, sig))

# mp.show() 
coordinates = [
        ["Pixel 1",  "Pixel 2",  "Pixel 3",  "Pixel 4",  "Pixel 5"], 
        
        ["Pixel 6",  "Pixel 7",  "Pixel 8",  "Pixel 9",  "Pixel 10"], 
        
        ["Pixel 11", "Pixel 12", "Pixel 13", "Pixel 14", "Pixel 15"], 
        
        ["Pixel 16", "Pixel 17", "Pixel 18", "Pixel 19", "Pixel 20"], 
        
        ["Pixel 21", "Pixel 22", "Pixel 23", "Pixel 24", "Pixel 25"] 
    ] 
    
centerX, centerY = 2, 2 

adj_pxs = [] 
for x in range(-2, 2+1): 
    for y in range(-2, 2+1): 
        adj_pxs.append([centerX+x, centerY+y]) 
        
# dists = [] 
# for i in range(len(adj_pxs)): 
#     xBigger = True if max(adj_pxs[i][0], adj_pxs[i][1]) == adj_pxs[i][0] else False 
#     if xBigger: 
#         dists.append(2-(adj_pxs[i][0]-centerX)) 
#     else: 
#         dists.append(2-(adj_pxs[i][1]-centerY)) 

# for i in range(len(adj_pxs)): 
#     print(f"{adj_pxs[i]} ({dists[i]})", end="\n\n\n" if (i+1)%5==0 else "  ") 
    
vals = [] 
sigX = 2 # np.std([k[0] for k in adj_pxs]) 
sigY = 2 # np.std([k[1] for k in adj_pxs])
for px in adj_pxs: 
    x = ((px[0] - 4)*(px[0]) - 4) / (2 * (sigX * sigX)) 
    y = ((px[1] - 4)*(px[1]) - 4) / (2 * (sigY * sigY)) 
    val = 1 * np.exp(-(x + y))
    vals.append(val) 
    
# normalize between 0 - 1: normVal = (val - min(vals)) / (max(vals) - min(vals)) 
normVals = [] 
for i in range(len(vals)): 
    newVal = (vals[i] - min(vals)) / (max(vals) - min(vals)) 
    normVals.append(newVal) 

for i in range(len(adj_pxs)): 
    print(f"{adj_pxs[i]} ({normVals[i]})", end="\n\n\n" if (i+1)%5==0 else "  ") 
    
print(adj_pxs) 
print(normVals) 
print([k[0] for k in adj_pxs], np.std([k[0] for k in adj_pxs])) 
print([k[1] for k in adj_pxs], np.std([k[1] for k in adj_pxs])) 