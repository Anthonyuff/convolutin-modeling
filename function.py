import numpy as np
import matplotlib.pyplot as plt

modeling = np.linspace(500, 4000, 250000).reshape(500, 500)
modeling[0:250,:]=1500
modeling[250:,:]=3000
print(modeling)
plt.imshow(modeling,aspect='auto', cmap='viridis')
plt.show() 