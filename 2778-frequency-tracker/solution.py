class FrequencyTracker:

    def __init__(self):
        self.freq = {}
        self.freq_val = {}

    def add(self, number: int) -> None:
        old = self.freq.get(number, 0)

        if old > 0:
            self.freq_val[old] -= 1

        new = old + 1
        self.freq[number] = new
        self.freq_val[new] = self.freq_val.get(new, 0) + 1

    def deleteOne(self, number: int) -> None:
        if number not in self.freq:
            return

        old = self.freq[number]
        self.freq_val[old] -= 1

        new = old - 1

        if new == 0:
            del self.freq[number]
        else:
            self.freq[number] = new
            self.freq_val[new] = self.freq_val.get(new, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_val.get(frequency, 0) > 0
