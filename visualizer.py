class Visualier():

    MIN_ARRAY_LENGTH = 1
    MAX_ARRAY_LENGTH = 20

    def __init__(self, array=[]):
        self.array = array
        print(self.array)

    def update(self, new_array):
        print(new_array)
