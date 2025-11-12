class Two:
    def __init__(self, maximum):
        self.maximum = maximum
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.maximum:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

for num in Two(15):
    print(num)
