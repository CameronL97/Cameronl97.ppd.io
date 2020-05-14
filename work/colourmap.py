import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

rainbow = cm.get_cmap('rainbow', 21)
print('rainbow(range(12))', rainbow(range(21)))
