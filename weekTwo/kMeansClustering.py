import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from pylab import figure
from pprint import pprint
import copy

'''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
RGB color; the keyword argument name must be a standard mpl colormap name.'''
# https://stackoverflow.com/questions/14720331/how-to-generate-random-colors-in-matplotlib
def get_cmap(n, name='hsv'):
    return plt.cm.get_cmap(name, n)

# point -> (x_p, y_p)
# center -> (x_c, y_c)
# distance between 2 random points (x_1, y_1),(x_2,y_2) in 2D space is
# sqrt((x_1-x_2)^2 + (y_1-y_2)^2)
def distanceToClusterCenter(X, c):
    n = X.shape[1]
    K = c.shape[1]
    D = np.zeros((n, K))
    for i, point in enumerate(X.T):
        for j, center in enumerate(c.T):
            distance = np.linalg.norm(point - center)
            D[i,j] = distance
    return D

# setup for plotting
fig, ax = plt.subplots()

# Generate n number of random points
# TODO: Generate n_d distict gaussian clusters to verify the algorithm is
# working where n_d < K
# Using a 2Xn matrix to represent the points, because it's easier to calcuate the distance to origin
# E.G. np.linalg.norm(X, axis=0) - norm relative to the columns

n = 500
K = 5
# X = np.random.random((2, n))
X = None
#[1,1],[6,6],[2,5],[1,-5],[3,4]
preDefinedCenters = np.array([[10,60,20,10,50],[10,60,50,-50,30]])

for i in range(0, K):
    # generate normal distribution random numbers to create clusters
    # X = np.random.normal(0, 1, (2, n/K))
    # offset the clusters by a random amount
    temp = np.tile(preDefinedCenters[:,i],(n/K,1)).T + np.random.normal(0, 5, (2, n/K))
    if X is None:
        X = temp
    else:
        X = np.concatenate((X,temp), axis=1)

# create a matrix for storing the distance variable for n number of points to K number of centers
D = np.zeros((n, K))

# create an array that stores the cluster ownship for n points
ownship = np.zeros(n)

# create a list of arrays for storing the points for K cluster centers
clusterMembers = [None]*K
isCompleted = False

# 1. Randomly select 'c' cluster centers.
# TODO: Select them uniform randomly within the range of the data
# find out the mean of the data and the range of the data
# range*np.random.random+datamean
dataRange = np.max(X, axis=1) - np.min(X, axis=1)
print dataRange
dataMean = np.mean(X, axis=1)
print dataMean

c = np.tile(dataRange,(K,1)).T*np.random.random((2, K))+np.tile(dataMean,(K,1)).T

# 2. Compute the distance between each data point and each cluster centers
D = distanceToClusterCenter(X, c)


iterationCounter = 0
while not isCompleted:
    iterationCounter = iterationCounter + 1
    print iterationCounter
    # previousOwnship = ownship
    # stupid python doesn't copy by value but copy the refence

    previousOwnship = copy.copy(ownship)
    # print "previousOwnship: {0}".format(previousOwnship)

    # 3 Assign each data point to its nearest cluster centers
    for i, points in enumerate(D):
        # print points
        # print i
        ownship[i] = np.where(points == points.min())[0]
        if clusterMembers[int(ownship[i])] is None:
            clusterMembers[int(ownship[i])] = []
        clusterMembers[int(ownship[i])].append(X[:,i])


    # print "clusterMembers: {0}".format(clusterMembers)
    # print "ownship: {0}".format(ownship)

        # save the points that belong to the same center
        # ownship[i] is a cluster number

    # 4. Recompute the new cluster centers using the formula:
    #   v_i = (1/c_i)\sum_{j=1}^{c_i} x_j
    #   where c_i is the number of data points in the i'th cluster# Recompute the distance between each data point and the new cluster centers
    for i, members in enumerate(clusterMembers):
        if members is not None:
            # print "sum: {0}".format(sum(members))
            clusterCenterPosition = sum(members)/len(members)
            # print "average: {0}".format(clusterCenterPosition)
            c[:,i] = clusterCenterPosition


    # 5.Recompute the distance between each data point and the new cluster centers
    D = distanceToClusterCenter(X, c)
    ax.scatter(X[0,:], X[1,:], c="white")
    randomColors = get_cmap(K)
    for i in range(0, K):
        ax.scatter(c[0, i], c[1, i], c=randomColors(i))
    fig.savefig("images/kMeanCluster"+ str(iterationCounter) +".png")

    # 6.If no data point was reassigned then stop else repeat from step 3
    print "previousOwnship: {0}".format(previousOwnship)
    print "current ownship: {0}".format(ownship)

    print "Compare previousOwnship with current ownship: {0}".format((previousOwnship == ownship).all())
    if (previousOwnship == ownship).all():
        isCompleted = True
