
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already
        #  in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break
    print(arr)


class BubbleSort:
    """Initializer of class takes series parameter and returns Class Objects"""
    def __init__(self, arr):
        """Built in validation and exception"""
        self._arr = arr
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.bubble_sort()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);



    """Algorithm for building book series list, this id called from __init__"""
    def bubble_sort(self):
        f = bubbleSort(self._arr)

        """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return bubbleSort(self._arr)

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]



if __name__ == "__main__":
    '''Value for testing'''

    '''Constructor of Class object'''
    x = [2, 1, 64, 23, 7]
    bubbles = BubbleSort(x)




