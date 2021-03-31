import random

booklist1 = ["Fault in our Stars,", "Harry Potter Volume 1", "Percy Jackson", "Calculus 1 Textbook", "Scarlet Letter", "Romeo & Juliet"]

booklist2 = ["Fault in our Stars,", "Harry Potter Volume 1", "Romeo & Juliet"]



class Books:
    """Initializer of class takes series parameter and returns Class Objectg"""
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
        self.book_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building Fibonacci sequence, this id called from __init__"""
    def book_series(self):
        limit = self._series
        f = [random.choices(booklist1, k=1)]  # fibonacci starting array/list
        while limit > 0:
            self.set_data(f[0])
            f = [random.choices(booklist1, k=n)]
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

n = 2

#Tester Code
if __name__ == "__main__":
    '''Value for testing'''
    '''Constructor of Class object'''
bookrecs = Books(n)


   # printing book recs
print(f"Here are some book recomendations = {bookrecs.list}")

for i in range(n):
    print(f"Listing of Book Recs {i + 1}= {bookrecs.get_sequence(i)}")
