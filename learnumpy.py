import numpy as np

line1 = np.array([32,21,21,5,33,30])
line2 = np.array([31,22,22,5,33,30])
tem = np.concatenate(line1,line2)
print(tem)