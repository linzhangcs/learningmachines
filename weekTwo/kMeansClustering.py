import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
import copy
def distanceToClusterCenter(X, c):
    n = X.shape[1]
    K = c.shape[1]
    D = np.zeros((n, K))
    for i, point in enumerate(X.T):
        for j, center in enumerate(c.T):
            distance = np.linalg.norm(point - center)
            D[i,j] = distance
            # point -> (x_p, y_p)
            # center -> (x_c, y_c)
            # distance between 2 random points (x_1, y_1),(x_2,y_2) in 2D space is
            # sqrt((x_1-x_2)^2 + (y_1-y_2)^2)
    # print D
    # print D.shape
    return D
# Generate n number of random points
# Using a 2Xn matrix to represent the points, because it's easier to calcuate the distance to origin
# E.G. np.linalg.norm(X, axis=0) - norm relative to the columns

n = 10
X = np.random.random((2, n))
K = 5

# create a matrix for storing the distance variable for n number of points to K number of centers
D = np.zeros((n, K))

# create an array that stores the cluster ownship for n points
ownship = np.zeros(n)

# create a list of arrays for storing the points for K cluster centers
clusterMembers = [None]*K
isCompleted = False

# just a suggestion: Initialize a list of None types using this:
# clusterMembers = [None]*K
# In the code below if you want to add points you can fin

# 1. Randomly select 'c' cluster centers.
c = np.random.random((2, K))
# 2. Compute the distance between each data point and each cluster centers
D = distanceToClusterCenter(X, c)
print("D after: {0}".format(D))
        # point -> (x_p, y_p)
        # center -> (x_c, y_c)
        # distance between 2 random points (x_1, y_1),(x_2,y_2) in 2D space is
        # sqrt((x_1-x_2)^2 + (y_1-y_2)^2)
while not isCompleted:
    # previousOwnship = ownship
    # stupid python doesn't copy by value but copy the refence

    previousOwnship = copy.copy(ownship)
    print "previousOwnship: {0}".format(previousOwnship)

    # 3 Assign each data point to its nearest cluster centers
    for i, points in enumerate(D):
        # print points
        # print i
        ownship[i] = np.where(points == points.min())[0]
        if clusterMembers[int(ownship[i])] is None:
            clusterMembers[int(ownship[i])] = []
        clusterMembers[int(ownship[i])].append(X[:,i])


    print "clusterMembers: {0}".format(clusterMembers)
    print "ownship: {0}".format(ownship)

        # save the points that belong to the same center
        # ownship[i] is a cluster number

    # 4. Recompute the new cluster centers using the formula:
    #   v_i = (1/c_i)\sum_{j=1}^{c_i} x_j
    #   where c_i is the number of data points in the i'th cluster# Recompute the distance between each data point and the new cluster centers
    print("cluster center")
    pprint(c)

    for i, members in enumerate(clusterMembers):
        print i
        print members
        if members is not None:
            print "sum: {0}".format(sum(members))
            clusterCenterPosition = sum(members)/len(members)
            print "average: {0}".format(clusterCenterPosition)
            c[:,i] = clusterCenterPosition
            # for member in members:
                # print member
                # print sum(members)
                # clusterCenterPosition = sum(member[0])
    print("Updated cluster center:")
    pprint(c)
    # 5.Recompute the distance between each data point and the new cluster centers
    D = distanceToClusterCenter(X, c)
    print("D recompute: {0}".format(D))

    # 6.If no data point was reassigned then stop else repeat from step 3
    print "previousOwnship: {0}".format(previousOwnship)
    print "current ownship: {0}".format(ownship)

    print "Compare previousOwnship with current ownship: {0}".format((previousOwnship == ownship).all())
    if (previousOwnship == ownship).all():
        isCompleted = True
