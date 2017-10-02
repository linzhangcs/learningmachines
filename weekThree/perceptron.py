# The Perceptron Algorithm
#
# 1.For every input, multiply that input by its weight.
# 2.Sum all of the weighted inputs.
# 3.Compute the output based on that sum passed through an activation function.
    #activation function: sgn(sumOfweightedInputs)
# Here, the activation function will be the sign of the sum.

import numpy as np

inputPts = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
ANDOutput = np.array([0, 0, 0, 1])
OROutput = np.array([0, 1, 1, 1])
XOROutput = np.array([0, 1, 1, 0])

learningRate = 0.5

class perceptron:
    def __init__(self, learningRate, input, desiredOutput):
        #intialize weight
        self.weight = self._train(learningRate, input, desiredOutput)

    def predict(wantToPredictPoints):
        for point in enumerate(inputPts):
            print point
            sumOfweightedInputs = np.dot(point,weight)
            output = np.sign(sumOfweightedInputs)
            print output
            # loop trough all of the points to get predictions and compare again the desiredOutput

    def _train(self, learningRate, input, desiredOutput):
        weight = np.zeros(inputPts.T.shape[0])
        sumOfweightedInputs = 0
        for i, point in enumerate(inputPts):
            sumOfweightedInputs = np.dot(point,weight)
            print "number of {0} , sumOfweightedInputs: {1}, point: {2}".format(i, sumOfweightedInputs, point)
            output = np.sign(sumOfweightedInputs)
            print output
            # Compare output to desiredOutput:
            # find out the difference and add it to the weight
            error = desiredOutput[i] - output
            print error
            delta = error*point
            weight = delta * learningRate + weight
            print weight
        return weight

ANDGatePerceptron = perceptron(learningRate, inputPts, ANDOutput)
ORGatePerceptron = perceptron(learningRate, inputPts, OROutput)
XORGatePerceptron = perceptron(learningRate, inputPts, XOROutput)
