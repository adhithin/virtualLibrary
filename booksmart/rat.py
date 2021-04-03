import random

function1 = ["1", "x", "x^2", "x^3", "x^4"]
function2 = ["1", "x", "x^2"]

class Rats:
    """Initializer of class takes series parameter and returns Class Objects"""
    def __init__(self, series):
        """Built in validation and exception"""
        if series < 0 or series > 6:
            raise ValueError("Series must be between 2 and 10")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.function_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);


    def function_series(self):
        limit = self._series
        f = [5]
        factorial = 1
        while limit > 0:
            self.set_data(f[0])
            for i in range(1,5 + 1):
                factorial = factorial*i
                list = f.append(factorial)
                print(factorial)
            #f = [f[0], f[1]*f[0]]
            limit -= 1

    """Method/Function to set Fibonacci data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1


    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]



if __name__ == "__main__":
    '''Value for testing'''
    n = 5
    '''Constructor of Class object'''
    functionseries = Rats(n/n)
    print(f"Here are some series members of e^x =" + Rats(n/n))
    #print (factorial)
#for i in range(n):
    #print(f"Fibonacci sequence {i + 1} = {functionseries.get_sequence(i)}")

