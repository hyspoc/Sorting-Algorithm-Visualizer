import matplotlib.pyplot as plt
import numpy as np
class Visualier():

    MIN_ARRAY_LENGTH = 1
    MAX_ARRAY_LENGTH = 50
    SORT_PAUSE = 0.2
    END_PAUSE = 10

    def __init__(self, array=[]):
        self.default_facecolor = 'gainsboro'
        self.default_edgecolor = None
        self.highlight_facecolor = 'grey'
        self.highlight_edgecolor = 'darkgrey'

        self.array = [n for n in array]
        self.length = len(self.array)

        self.fig, self.ax = plt.subplots()
        self.ax.yaxis.set_visible(False)
        self.ax.xaxis.set_visible(False)
        self.bars = self.ax.bar([str(n) for n in range(self.length)], self.array, facecolor=self.default_facecolor)

    def update(self, new_array, facecolors=[], edgecolors=[]):
        plt.pause(Visualier.SORT_PAUSE)

        for i, bar, num, new_num in zip(range(self.length), self.bars, self.array, new_array):
            bar.set_facecolor('white')
            bar.set_edgecolor('white')
            bar.set_height(new_num)

            if i in facecolors:
                bar.set_facecolor(self.highlight_facecolor)
            else:
                bar.set_facecolor(self.default_facecolor)

            if i in edgecolors:
                bar.set_edgecolor(self.highlight_edgecolor)
            else:
                bar.set_edgecolor(self.default_edgecolor)

        self.array= [n for n in new_array]

    def end(self):
        for bar in self.bars:
            bar.set_facecolor(self.default_facecolor)
            bar.set_edgecolor(self.default_edgecolor)

        plt.pause(Visualier.END_PAUSE)
