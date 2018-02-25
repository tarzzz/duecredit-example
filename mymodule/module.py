from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import pdist
from sklearn.datasets import make_blobs

def my_function():
	print("I: Simulating 4 blobs")
	data, true_label = make_blobs(centers=4)

	dist = pdist(data, metric='euclidean')

	Z = linkage(dist, method='single')
