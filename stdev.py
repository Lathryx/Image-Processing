import math 

exData = [7, 5, 4, 9, 12, 45] 

def mean(data): 
    n = len(data) 
    mean = sum(data) / n 
    return mean 
    
def variance(data): 
    n = len(data) 
    mean = sum(data) / n 
    
    deviations = [(x - mean) ** 2 for x in data] 
    variance = sum(deviations) / (n-1) 
    return variance 
    
def stdev(data): 
    var = variance(data) 
    std_dev = math.sqrt(var) 
    return std_dev 
    
print(f"Standard Deviation of dataset {exData}: {stdev(exData)}") 