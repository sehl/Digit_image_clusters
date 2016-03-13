# Sara E. Hansen-Lund
# For use with Kaggle Digit Recognizer data
# Uses python 2.7, numpy, & sklearn.cluster.KMeans
# March 8, 2016
import numpy as np
from scipy.misc import imsave
from scipy.misc import imresize
from sklearn.cluster import KMeans

TRAIN = 'data/train.csv'

NUM_CLUSTERS = 20
MAX_ITER = 100

# retrieves a dict mapping categories to training data. Data is presented
# as a list of images represented as 1-d python list objects.
def get_train_data(filename):
	data = dict(zip([ i for i in range(10) ], [ [] for i in range(10)]))
	with open(filename) as f:
		header = f.readline()
		for line in f:
			d = line[:-1].split(',')

			data[int(d[0])].append([ int(n) for n in d[1:] ])
			
	return data

# data is a dict mapping categories to a list of data values
# function finds 10 clusters for each label using the K-means clustering
# algorithm and saves their images to a local file
def find_clusters(data):
	learner = KMeans(n_clusters=NUM_CLUSTERS, random_state=52)
	image = list()
	for cat in data:
		learner.fit(data[cat])
		
		sub_image = list()
		for i in range(NUM_CLUSTERS):
			cluster = [ 255 - n for n in learner.cluster_centers_[i] ]
			img = imresize(np.reshape(cluster, (28,28)), 4.0)
			sub_image.append(img)

		image.append(np.hstack(sub_image))
	
	image = np.vstack(image)

	imsave('digit_clusters_' + str(NUM_CLUSTERS) + '.png', image)

def main():
	training = get_train_data(TRAIN)
	# train the kmeans learner and save the image results
	find_clusters(training)


if __name__ == '__main__':
	main()


