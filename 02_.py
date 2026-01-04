import time
import numpy as np

x = np.random.choice(1000000, size=1000000)

start = time.time()
result = sum(x) / len(x)
print(result)
print(time.time() - start)
