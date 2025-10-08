class BubbleSorter:
    def __init__(self, data_list):
        self.data = data_list
        self.n = len(data_list)
    def sort(self):
        for i in range(self.n - 1):
            swapped = False
            for j in range(self.n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    swapped = True
            print(f"After round {i + 1}: {self.data}")
            if not swapped:
                break
    def display(self):
        print(f"current data {self.data}")


nums = [64, 34, 25, 12, 22, 11, 90]
sorter = BubbleSorter(nums)
print("Before sorting:")
sorter.display()
sorter.sort()
print("After sorting:")
sorter.display()
