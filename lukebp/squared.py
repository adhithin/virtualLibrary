class Squared:
    """Initializer of class takes series parameter and returns Class Objects"""
    def __init__(self, series):
        if series < 0 or series > 100:
            raise ValueError("Series must be between 0 and 100")
        series2 = series + 1
        self._series = series2
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.calc_series()

    """Algorithm for building Fibonacci sequence, this id called from __init__"""
    def calc_series(self):
        limit = self._series
        a = 0
        s = 0
        while limit > 0:
            self.set_data(s)
            s = [a**2]
            a += 1
            limit -= 1

    """Method/Function to set Fibonacci data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        self._list.append(num)
        self._dict = self._list.copy()
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
        return self._list[self._dictID-1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]


# Tester Code
if __name__ == "__main__":
    '''Value for testing'''
    n = 10
    '''Constructor of Class object'''
    squared = Squared(n)

    '''Using getters to obtain data from object'''
    print(f"Squared number for {n-1} = {squared.number}")
    print(f"Squared series for {n-1} = {squared.list}")

    '''Using method to get data from object'''
    for i in range(n):
        print(f"Squared =sequence {i} = {squared.get_sequence(i+1)}")