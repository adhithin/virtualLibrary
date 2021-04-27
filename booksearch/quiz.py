import numpy as np

def sigmoid(x): ##defining the sigmoid function
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x) ##defining the derivative of the sigmoid function, which tells us the gradient

class NeuralNetwork: ##initializing the neural network class
    def __init__(self, x, y):
        self.input      = x

        ##the weights were random, but we want the weighting in the network to be consistent
        self.weights1   = np.random.rand(self.input.shape[1],1)
        self.weights2   = np.random.rand(1,1)

        self.y          = y
        self.output     = np.zeros(self.y.shape)
        self._list = []

    def feedforward(self): ##a procedure that we're using to determine the output.
        #calculating the dot products using numpy, then inputting that into our sigmoid function.
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))
        ## here, we're using a sigmoid function. there's lots of other functions, like ReLu, tanh, and so on.

    def backprop(self): ##another procedure
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2


    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return

    @property
    def list(self):
        return nn.output

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]

if __name__ == "__main__":
    X = np.array([[0,0,1],#these are our inputs. first number: if they eat bananas. second: strawberries; third: blueberries
                  [0,1,0],
                  [1,0,0],
                  [1,1,1]])
    y = np.array([[0],[0],[0],[0]])
    ## the shapes of the X and y have to be the same; otherwise, we wouldn't be able to do matrix multiplication.
    ## X is 3x4, and y is 4x1. rows by columns.
    nn = NeuralNetwork(X,y)

    for i in range(1500): ##our iteration algorithm
        nn.feedforward() ## calling our procedure
        nn.backprop() ##calling our next procedure.

    bookquiz = NeuralNetwork(X, y) ##creating an object.
    print(f"Here are your statistics = {bookquiz.list}") ##using the object here in the print statement.

    ## analysis of the results produced by the neural network.

    for i in nn.output:
        if (i < 0.005):
            print("you read books really slowly, particpate in book clubs, and also reread books; this means that you're really comprehensive, and like the feel of books. This ability will be really applicable in real life discussions. ")
        else:
            print("you might like to read fast, find new things, and not think a lot about what you are reading.")
    #print(nn.output)
    ## if the number is higher, they're not that healthy; if they have a higher number, they're not healthy.
    ## first value is worth the least: do you read books slowly? yes = 1, no = 1
    ## the second value is worth the 2nd most: do you reread books?
    ## the third value is worth the most: do you participate in book clubs?