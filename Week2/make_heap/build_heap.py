# python3

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        self.MakeHeap()
        #print(self._data)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

    def LeftChild(self, i):
        return 2*i + 1

    def RightChild(self, i):
        return 2*(i + 1)

    def Parent(self, i):
        return int((i - 1)/2)

    def MakeHeap(self):
        i = int(len(self._data)/2)
        while i >= 0:
            self.SiftDown(i)
            i -= 1

    def SiftDown(self, i):
        min_index = i
        l = self.LeftChild(i)
        if l < len(self._data) and self._data[l] < self._data[min_index]:
            min_index = l
        r = self.RightChild(i)
        if r < len(self._data) and self._data[r] < self._data[min_index]:
            min_index = r
        if i != min_index:
            self._swaps.append((i, min_index))
            self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
            self.SiftDown(min_index)


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
