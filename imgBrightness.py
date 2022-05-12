from PIL import Image

imgDir = input("Path to image: ") 
im = Image.open(imgDir)
w, h = im.size 
pixels = im.load() 
for i in range(h): 
    for j in range(w): 
        vals = pixels[i,j] 
        newVals = [] 
        for val in vals: 
            if val < 206: 
                newVals.append(val+50) 
            else: 
                newVals.append(255) 
        
        pixels[i,j] = tuple(newVals) 
        
im.save("img_brightness.png") 