import random
import visualizer as viz

def create_algorithm(algorithm_name):
    if algorithm_name=='Quick Sort':
        sort_algo = QuickSort()
    elif algorithm_name=='Merge Sort':
        sort_algo = MergeSort()
    elif algorithm_name=='Bubble Sort':
        sort_algo = BubbleSort()
    else:
        sort_algo = Sort()
    return sort_algo

class Sort():

    MIN_RANDOM_ELEMENT = 1
    MAX_RANDOM_ELEMENT = 200

    def __init__(self, unsorted_array=[]):
        self.array = unsorted_array
        self.length = len(self.array)

    def set_array(self, unsorted_array):
        self.array = unsorted_array
        self.length = len(self.array)

    def set_random_array(self, length):
        self.array = [random.randint(Sort.MIN_RANDOM_ELEMENT, Sort.MAX_RANDOM_ELEMENT) for _ in range(length)]
        self.length = len(self.array)
        random.shuffle(self.array)

    def sort(self):
        pass


class QuickSort(Sort):

    def sort(self):
        self.visualizer = viz.Visualier(self.array)
        self.quick_sort(0, self.length-1)
        self.visualizer.end()

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
                self.swap(i, j, high)

        self.swap(i+1, high, high)

        return i+1

    def swap(self, x, y, pivot):
        self.array[x], self.array[y] = self.array[y], self.array[x]
        self.visualizer.update(self.array, facecolors=[x,y], edgecolors=[pivot])


class MergeSort(Sort):

    def sort(self):
        self.visualizer = viz.Visualier(self.array)
        self.merge_sort(0, self.length-1)
        self.visualizer.end()

    def merge_sort(self, l, r):
        if l<r:
            m = l + (r-l)//2
            self.merge_sort(l, m)
            self.merge_sort(m+1, r)
            self.merge(l, m, r)

    def merge(self, l, m, r):
        i, j = l, m+1

        while i<=r and j<=r:
            if self.array[i]>self.array[j]:
                self.swap(i, j)
                j+=1
            else:
                self.visualizer.update(self.array, edgecolors=[i,j])
            i+=1

    def swap(self, i, j):
        self.array[i], self.array[i+1:j+1] = self.array[j], [n for n in self.array[i:j]]
        self.visualizer.update(self.array, facecolors=[i], edgecolors=[i,j])

class BubbleSort(Sort):

    def sort(self):
        self.visualizer = viz.Visualier(self.array)
        self.bubble_sort()
        self.visualizer.end()

    def bubble_sort(self):
        for i in range(self.length):
            for j in range(self.length-i-1):
                self.swap(j, j+1)

    def swap(self, x, y):
        if self.array[x] > self.array[y]:
            self.array[x], self.array[y] = self.array[y], self.array[x]
            self.visualizer.update(self.array, facecolors=[x,y], edgecolors=[x,y])
        else:
            self.visualizer.update(self.array, facecolors=[], edgecolors=[x,y])
