
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

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
        return self.bubble_sort

    @property
    def list(self):
        return self._arr

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]






    arr = ["C", "E", "D", "B", "A"]
    n = len(arr)
    # Traverse through all array elements

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if swapped == False:
            break
    print(arr)

    arr = [4, 2, 543, 23, 531, 13, 24]
    n = len(arr)
    # Traverse through all array elements

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if swapped == False:
            break
    print(arr)





