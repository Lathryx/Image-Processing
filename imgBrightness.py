from PIL import Image

imgDir = input("Path to image: ") 
outDir = input("Name the output file: ") 
im = Image.open(imgDir)
w, h = im.size 
pixels = im.load() 
for i in range(h): 
    for j in range(w): 
        vals = pixels[j,i] 
        newVals = [] 
        for val in vals: 
            if val < 206: 
                newVals.append(val+50) 
            else: 
                newVals.append(255) 
        
        pixels[j,i] = tuple(newVals) 
        
im.save(f"{outDir}.png") 