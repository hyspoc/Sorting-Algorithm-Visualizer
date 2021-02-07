import random
import visualizer as viz

class Sort():

    MIN_RANDOM_ELEMENT = 0
    MAX_RANDOM_ELEMENT = 50

    def __init__(self, unsorted_array=[]):
        self.array = unsorted_array

    def set_array(self, unsorted_array):
        self.array = unsorted_array

    def set_random_array(self, length):
        self.array = [random.randint(Sort.MIN_RANDOM_ELEMENT, Sort.MAX_RANDOM_ELEMENT) for _ in range(length)]

    def sort(self):
        self.visualizer = viz.Visualier(self.array)


class QuickSort(Sort):

    def sort(self):
        super().sort()
        self.quick_sort(0, len(self.array)-1)

    def quick_sort(self, low, high):
        if low<high:
            p = self.partition(low, high)

            self.quick_sort(low, p-1)
            self.quick_sort(p+1, high)

    def partition(self, low, high):
        pivot = self.array[high]

        i = low-1

        for j in range(low, high):
            if self.array[j] < pivot:
                i += 1
                self.swap(i, j)

        self.swap(i+1, high)

        return i+1

    def swap(self, x, y):
        self.array[x], self.array[y] = self.array[y], self.array[x]
        self.visualizer.update(self.array)
