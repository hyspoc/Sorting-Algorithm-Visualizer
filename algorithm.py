import random
import visualizer as viz

class Sort():

    MIN_RANDOM_ELEMENT = 1
    MAX_RANDOM_ELEMENT = 100

    def __init__(self, unsorted_array=[]):
        self.array = unsorted_array

    def set_array(self, unsorted_array):
        self.array = unsorted_array

    def set_random_array(self, length):
        self.array = [random.randint(Sort.MIN_RANDOM_ELEMENT, Sort.MAX_RANDOM_ELEMENT) for _ in range(length)]
        random.shuffle(self.array)

    def sort(self):
        pass

# class InsertionSort(Sort):
#
#     def sort(self):
#         self.visualizer = viz.Visualier(self.array)
#         self.quick_sort(0, len(self.array)-1)
#         self.visualizer.end()
#
#     def insertion_sort(self):
#         for i in range(1, len(self.array)):
#             curr = self.array[i]
#             for j in range(i-1, -1, -1):
#                 if curr >= self.array[j]:
#                     self.array[j+1] = curr
#                     break
#                 else:
#                     self.array[j+1] = self.array[j]
#                     self.array[j] = curr
#
# 妹看懂这个class要怎么写 瞎写滴 为啥别人都分了好几个部分？ 太困了 我睡了 啾啾

class QuickSort(Sort):

    def sort(self):
        self.visualizer = viz.Visualier(self.array)
        self.quick_sort(0, len(self.array)-1)
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
        self.merge_sort(0, len(self.array)-1)
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
