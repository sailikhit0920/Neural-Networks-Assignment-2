import numpy as np

random_vector = np.random.uniform(1, 20, size=20)
reshaped_array = random_vector.reshape(4, 5)
max_indices = np.argmax(reshaped_array, axis=1)
col_indices = np.arange(5)
reshaped_array[np.arange(4)[:, np.newaxis], max_indices] = 0
print(reshaped_array)
