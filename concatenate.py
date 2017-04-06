import numpy as np
import glob

files = glob.glob("*.npy")


total =[]

for f in files:
    if total ==[]:
        total = np.load(f)

    else:
        total = np.vstack((total, np.load(f)))


np.save("ALL",total)
