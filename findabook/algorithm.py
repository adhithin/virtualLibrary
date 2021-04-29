class Pascal:
    def __init__(self, series):
        if series < 2 or series > 5:
            raise ValueError("Series must be between 2 and 5")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.calc_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);


    def calc_series(self):
        f = [1, 11]  # pascal starting array/list
        limit = self._series
        while limit > 0:
            self.set_data(f[0])
            f = [f[1], (f[1])*11]
            limit -= 1


    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1


    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]


    def get_lastnumber(self, nth):
        return self._list[nth]


# Tester Code
if __name__ == "__main__":
    n = 5
    pascal = Pascal(n)
    print(f"Pascal's number for {n} = {pascal.number}")
    print(f"Pascal's series for {n} = {pascal.list}")
    for i in range(n):
        print(f"Pascal's triangle: row {i + 1} = {pascal.get_lastnumber(i)}")
