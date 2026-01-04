import time
import numpy as np
x = np.random.choice(1000000)

# Case 1
start = time.time()
sum(x) / len(x)
print(time.time() - start)