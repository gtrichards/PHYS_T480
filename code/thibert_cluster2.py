## Hierarchical Clustering Example: BAL Quasar UV Spectra (pre-reduced)
## Author: Nathalie C. M. Thibert (Saint Mary's University), modified from
## 	   code by Mark Daley (Western University)
##
## Method: Agglomerative Hierarchical Clustering
## Distance Metric: Complete Linkage
## Data: 100 BAL Quasar UV Spectra over ~1400-1550 Ang (i.e., the C IV BAL) 
##	 Spectra are already in rest-frame, normalized to the local continuum 
## 	 and emission lines, and resampled to a common wavelength grid. 


# Compute Pearson correlation matrix for 100 spectra. 
# Each element is a pairwise comparison b/w two spectra.
c = data.corr() # Should have 100 rows and 100 columns.

# Compute absolute-valued Pearson distance matrix.
dp = 1.0 - np.abs(c)

# Compute Euclidean distance matrix for the first dendrogram
de1 = squareform(pdist(dp,metric='euclidean')) 

# Do it again for the second dendrogram
de2 = squareform(pdist(dp.T,metric='euclidean'))

# Start the dendrogram plot.
f = plt.figure(figsize=(8, 8))

# Add the first dendrogram (on the left side)
ax1 = f.add_axes([0.09, 0.1, 0.2, 0.6])
Y = linkage(de1, method='complete') # This is where the hierarchical clustering takes place.
Z1 = dendrogram(Y, orientation='left',show_leaf_counts=False, no_labels=True) # Plots dendrogram.
ax1.set_xticks([])
ax1.set_yticks([])

# Add the second dendrogram (on the top)
ax2 = f.add_axes([0.3, 0.71, 0.6, 0.2])
Y = linkage(de2, method='complete')
Z2 = dendrogram(Y,show_leaf_counts=False, no_labels=True)
ax2.set_xticks([])
ax2.set_yticks([])

# Add the (main) plot of the (clustered) Euclidean distance matrix.
axmatrix = f.add_axes([0.3, 0.1, 0.6, 0.6])
idx1 = Z1['leaves']
idx2 = Z2['leaves']
D = de1[idx1, :]
D = D[:, idx2]
im = axmatrix.matshow(D, aspect='auto', origin='lower', cmap='hot')
axmatrix.set_xticks([])
axmatrix.set_yticks([])
    
axcolor = f.add_axes([0.91,0.1,0.02,0.6])
pylab.colorbar(im,cax=axcolor)
f.show()

## NOTE: The colours in the dendrograms correspond to a flat clustering given 
##	 the default distance threshold in Python.

