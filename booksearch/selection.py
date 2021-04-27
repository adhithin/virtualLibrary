import random


booklist1 = ["Fault in our Stars,", "Harry Potter Volume 1", "Percy Jackson", "Calculus 1 Textbook", "Scarlet Letter", "Romeo & Juliet", "Sesame Street", "Coding for Kids"]

booklist2 = ["Fault in our Stars,", "Harry Potter Volume 1", "Romeo & Juliet"]



class Books:
    """Initializer of class takes series parameter and returns Class Objects"""
    def __init__(self, recs):
        """Built in validation and exception"""
        if recs < 0 or recs > 6:
            raise ValueError("Series must be between 0 and 6")
        self._recs = recs
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.book_recs()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building book series list, this id called from __init__"""
    def book_recs(self):
        f = [(random.sample((booklist1), k=self._recs))]
        self.set_data(f[0])
        f = [f[0]] ## play with this = do we need f(0)

    """Method/Function to set data: list, dict, and dictID are instance variables of Class"""
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

    '''Constructor of Class object'''
    bookrecs = Books(3)
    print(f"Here are some book recomendations = {bookrecs.list}")

#for i in range(a):
    #print(f"Listing of Book Recs {i}= {bookrecs.get_sequence(i)}")
