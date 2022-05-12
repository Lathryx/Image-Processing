# from time import sleep as wait 

# for i in range(100): 
#     print(f"Processing... {round((i/100)*100)}%", end="\r") 
#     wait(0.05) 
# print("100%") 
import time
import sys

toolbar_width = 30

# setup toolbar
sys.stdout.write("[%s]" % ("-" * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("#")
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar