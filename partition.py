import numpy as np

total = np.load("ALL.npy")

test_cutoff = int(0.2*np.shape(total)[0])
valid_cutoff = test_cutoff*2

test = total[0:test_cutoff]
valid = total[test_cutoff:valid_cutoff]
train = total[valid_cutoff:]

np.save("TEST_SET",test)
np.save("VALIDATION_SET",valid)
np.save("TRAINING_SET", train)
