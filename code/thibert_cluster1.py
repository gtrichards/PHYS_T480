## Hierarchical Clustering Example: BAL Quasar UV Spectra (pre-reduced)
## Author: Nathalie C. M. Thibert (Saint Mary's University), modified from
## 	   code by Mark Daley (Western University)
##
## Method: Agglomerative Hierarchical Clustering
## Distance Metric: Complete Linkage
## Data: 100 BAL Quasar UV Spectra over ~1400-1550 Ang (i.e., the C IV BAL) 
##	 Spectra are already in rest-frame, normalized to the local continuum 
## 	 and emission lines, and resampled to a common wavelength grid. 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab

# import clustering algorithms from scipy
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import pdist, squareform

# Import pickled BAL quasar data.
data = pd.read_pickle('./data/balquasar_data.pkl') # Should have 500 wavelength values and 100 spectra.

# Over plot some example spectra
wl = np.arange(1400.1,1549.8,0.3)
spec0 = data.T.iloc[0] # You can change the index to see different spectra (choose 0,1,2,...,99).
spec5 = data.T.iloc[5]
spec7 = data.T.iloc[7]
plt.figure() 
plt.plot(wl,spec0)
plt.plot(wl,spec5)
plt.plot(wl,spec7)
plt.show()
