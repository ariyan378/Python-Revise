import numpy as np


arr = np.arange(100).tolist()
list_comprehension = [i for i in arr if i%10==0 and i!=0]

print(list_comprehension)

