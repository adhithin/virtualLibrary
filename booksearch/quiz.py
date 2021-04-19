import numpy as np

def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

class NeuralNetwork:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4)
        self.weights2   = np.random.rand(4,1)
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2


if __name__ == "__main__":
    X = np.array([[0,0,1],#these are our inputs. first number: if they eat bananas. second: strawberries; third: blueberries
                  [0,1,0],
                  [1,0,0],
                  [1,1,1]])
    y = np.array([[0],[0],[0],[0]])
    nn = NeuralNetwork(X,y)

    for i in range(1500):
        nn.feedforward()
        nn.backprop()

    for i in nn.output:
        if (i < 1):
            print("you read books really slowly, particpate in book clubs, and also reread books; this means that you...")
        else:
            print("very cool")
    #print(nn.output)
    ## if the number is higher, they're not that healthy; if they have a higher number, they're not healthy.
    ## first value is worth the least: do you read books slowly? yes = 1, no = 1
    ## the second value is worth the 2nd most: do you reread books?
    ## the third value is worth the most: do you participate in book clubs?